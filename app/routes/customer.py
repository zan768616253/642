import uuid
from datetime import date
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from sqlalchemy.orm import joinedload

from app import db
from ..models import Customer, Veggie, PremadeBox, Order, OrderLine, CreditCardPayment, DebitCardPayment, Item, Payment, \
    WeightedVeggie, UnitPriceVeggie, PackVeggie
from ..models.credit_card_payment import CardType
from ..models.item import ItemType
from ..models.veggie import VeggieType

customer_bp = Blueprint('customer', __name__, url_prefix='/customer')


@customer_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard_customer.html')


@customer_bp.route('/items')
def view_items():
    try:
        veggies = Veggie.query.all()
        premade_boxes = PremadeBox.query.all()
    except Exception as e:
        flash('Error retrieving items.', 'danger')
        return redirect(url_for('customer.dashboard'))

    return render_template('items.html', veggies=veggies, premade_boxes=premade_boxes)


@customer_bp.route('/order', methods=['GET', 'POST'])
def place_order():
    try:
        veggies = Veggie.query.all()
        premade_boxes = PremadeBox.query.all()
    except Exception as e:
        flash('Error retrieving items for order.', 'danger')
        return redirect(url_for('customer.view_items'))

    if request.method == 'POST':
        user_id = session.get('user_id')

        new_order = Order(
            order_customer_id=user_id,
            order_date=date.today(),
            order_number=f"ORD-{uuid.uuid4()}",
            order_status="Pending"
        )
        db.session.add(new_order)
        db.session.flush()

        try:
            for veg in veggies:
                qty = int(request.form.get(f'veggie_qty_{veg.id}', 0))
                if qty > 0:
                    order_line = OrderLine(order_id=new_order.id, item_number=veg.id, amount=qty)
                    db.session.add(order_line)

            for box in premade_boxes:
                qty = int(request.form.get(f'box_qty_{box.id}', 0))
                if qty > 0:
                    order_line = OrderLine(order_id=new_order.id, item_number=box.id, amount=qty)
                    db.session.add(order_line)

            db.session.commit()
            flash('Order placed successfully! Please proceed to checkout.', 'success')
            return redirect(url_for('customer.checkout', order_id=new_order.id))
        except Exception as e:
            db.session.rollback()
            flash('Error placing order.', 'danger')

    return render_template('place_order.html', veggies=veggies, premade_boxes=premade_boxes)


@customer_bp.route('/checkout/<int:order_id>', methods=['GET', 'POST'])
def checkout(order_id):
    try:
        order = Order.query.get(order_id)
    except Exception as e:
        flash('Error retrieving order.', 'danger')
        return redirect(url_for('customer.view_orders'))

    if request.method == 'POST':
        payment_type = request.form['payment_type']
        amount = float(request.form['amount'])

        try:
            if payment_type == 'CREDIT_CARD':
                card_number = request.form['card_number']
                card_expiry_date = request.form['card_expiry_date']
                card_type = request.form['card_type']

                payment = Payment(payment_customer_id=order.order_customer_id, payment_date=date.today(),
                                  payment_amount=amount, type=payment_type)
                credit_card_payment = CreditCardPayment(payment_customer_id=order.order_customer_id,
                                                        payment_date=date.today(),
                                                        payment_amount=amount,
                                                        card_number=card_number,
                                                        card_expiry_date=card_expiry_date,
                                                        card_type=CardType[card_type].value)
                db.session.add(payment)
                db.session.add(credit_card_payment)

            elif payment_type == 'DEBIT_CARD':
                bank_name = request.form['bank_name']
                debit_card_number = request.form['debit_card_number']

                payment = Payment(payment_customer_id=order.order_customer_id, payment_date=date.today(),
                                  payment_amount=amount, type=payment_type)
                debit_card_payment = DebitCardPayment(payment_customer_id=order.order_customer_id,
                                                      payment_date=date.today(),
                                                      payment_amount=amount,
                                                      bank_name=bank_name,
                                                      debit_card_number=debit_card_number)
                db.session.add(payment)
                db.session.add(debit_card_payment)

            order.order_status = 'Paid'
            db.session.commit()
            flash('Payment successful!', 'success')
            return redirect(url_for('customer.view_order', order_id=order.id))
        except Exception as e:
            db.session.rollback()
            flash('Error processing payment.', 'danger')

    order_lines = OrderLine.query.filter_by(order_id=order_id).all()

    total_amount = 0.0
    for order_line in order_lines:
        item = Item.query.get(order_line.item_number)

        if item.type == ItemType.VEGGIE.value:
            veggie = Veggie.query.get(item.id)
            total_amount += veggie.price_per_unit * order_line.amount
        elif item.type == ItemType.PREMADE_BOX.value:
            premade_box = PremadeBox.query.get(item.id)
            total_amount += premade_box.prize * order_line.amount

    return render_template('checkout.html', order=order, amount=total_amount)


@customer_bp.route('/order/<int:order_id>')
def view_order(order_id):
    try:
        order = Order.query.get(order_id)
    except Exception as e:
        flash('Error retrieving order.', 'danger')
        return redirect(url_for('customer.dashboard'))

    if not order:
        flash('Order cannot be found.', 'danger')
        return redirect(url_for('customer.dashboard'))

    try:
        order_lines = OrderLine.query.filter_by(order_id=order.id).all()
        items = []
        total_amount = 0.0

        for order_line in order_lines:
            item = Item.query.get(order_line.item_number)
            items.append({'order_line': order_line, 'item': item})

            if item.type == ItemType.VEGGIE.value:
                veggie = Veggie.query.get(item.id)
                total_amount += veggie.price_per_unit * order_line.amount
            elif item.type == ItemType.PREMADE_BOX.value:
                premade_box = PremadeBox.query.get(item.id)
                total_amount += premade_box.prize * order_line.amount
    except Exception as e:
        flash('Error retrieving order details.', 'danger')
        return redirect(url_for('customer.dashboard'))

    return render_template('view_order.html', order=order, items=items, total_amount=total_amount)


@customer_bp.route('/order/<int:order_id>/cancel', methods=['POST'])
def cancel_order(order_id):
    try:
        order = Order.query.get(order_id)
        if order and order.order_status == "Pending":
            order.order_status = "Cancelled"
            db.session.commit()
            flash('Order cancelled successfully!', 'success')
        else:
            flash('Order cannot be cancelled.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash('Error cancelling order.', 'danger')

    return redirect(url_for('customer.view_order', order_id=order.id))


@customer_bp.route('/orders/previous')
def previous_orders():
    user_id = session.get('user_id')
    try:
        previous_orders = Order.query.filter_by(order_customer_id=user_id).filter(Order.order_status != "Pending").all()
    except Exception as e:
        flash('Error retrieving previous orders.', 'danger')
        return redirect(url_for('customer.dashboard'))

    return render_template('previous_orders_customer.html', orders=previous_orders)


@customer_bp.route('/orders/pending')
def pending_orders():
    user_id = session.get('user_id')
    try:
        pending_orders = Order.query.filter_by(order_customer_id=user_id).filter(Order.order_status == "Pending").all()
    except Exception as e:
        flash('Error retrieving pending orders.', 'danger')
        return redirect(url_for('customer.dashboard'))

    return render_template('pending_orders_customer.html', orders=pending_orders)


@customer_bp.route('/account')
def account_details():
    user_id = session.get('user_id')
    try:
        customer = Customer.query.get(user_id)
    except Exception as e:
        flash('Error retrieving account details.', 'danger')
        return redirect(url_for('customer.dashboard'))

    return render_template('account_details.html', customer=customer)

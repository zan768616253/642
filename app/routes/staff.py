from datetime import date, timedelta
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app import db
from ..models import Staff, Customer, Order, Veggie, PremadeBox, OrderLine, Payment, Item

staff_bp = Blueprint('staff', __name__, url_prefix='/staff')

@staff_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard_staff.html')

# 1. View all vegetables and premade boxes
@staff_bp.route('/inventory', methods=['GET'])
def view_inventory():
    try:
        veggies = Veggie.query.all()
        premade_boxes = PremadeBox.query.all()
        return render_template('inventory.html', veggies=veggies, premade_boxes=premade_boxes)
    except Exception as e:
        flash(f'An error occurred while retrieving inventory: {str(e)}', 'error')
        return redirect(url_for('staff.dashboard'))

# 2. View all current orders and their details
@staff_bp.route('/orders/current', methods=['GET'])
def view_current_orders():
    try:
        current_date = date.today()
        current_orders = Order.query.filter(Order.order_date == current_date).all()
        orders_with_details = []

        for order in current_orders:
            order_lines = OrderLine.query.filter_by(order_id=order.id).all()
            order_items = []
            total_price = 0.0  # Initialize total price

            for ol in order_lines:
                item = Veggie.query.get(ol.item_number) or PremadeBox.query.get(ol.item_number)
                order_items.append({'order_line': ol, 'item': item})

                # Calculate total price
                if item.type == 'VEGGIE':
                    total_price += item.price_per_unit * ol.amount
                elif item.type == 'PREMADE_BOX':
                    total_price += item.prize * ol.amount

            orders_with_details.append({'order': order, 'order_items': order_items, 'total_price': total_price})

        return render_template('current_orders.html', orders=orders_with_details)
    except Exception as e:
        flash(f'An error occurred while retrieving current orders: {str(e)}', 'error')
        return redirect(url_for('staff.dashboard'))

# 3. View all previous orders and their details
@staff_bp.route('/orders/previous', methods=['GET'])
def view_previous_orders():
    try:
        previous_orders = Order.query.filter(Order.order_date < date.today()).all()
        orders_with_details = []

        for order in previous_orders:
            order_lines = OrderLine.query.filter_by(order_id=order.id).all()
            order_items = []
            total_price = 0.0  # Initialize total price

            for ol in order_lines:
                item = Veggie.query.get(ol.item_number) or PremadeBox.query.get(ol.item_number)
                order_items.append({'order_line': ol, 'item': item})

                # Calculate total price
                if item.type == 'VEGGIE':
                    total_price += item.price_per_unit * ol.amount
                elif item.type == 'PREMADE_BOX':
                    total_price += item.prize * ol.amount

            orders_with_details.append({'order': order, 'order_items': order_items, 'total_price': total_price})

        return render_template('previous_orders_admin.html', orders=orders_with_details)
    except Exception as e:
        flash(f'An error occurred while retrieving previous orders: {str(e)}', 'error')
        return redirect(url_for('staff.dashboard'))

@staff_bp.route('/orders/update/<int:order_id>', methods=['GET', 'POST'])
def update_order_status(order_id):
    try:
        order = Order.query.get_or_404(order_id)  # Fetch the order by ID
        if request.method == 'POST':
            new_status = request.form.get('order_status')  # Get the new status from the form
            order.order_status = new_status  # Update the order status
            db.session.commit()  # Commit the change to the database
            flash('Order status updated successfully!', 'success')  # Flash a success message
            return redirect(request.args.get('next', url_for('staff.view_current_orders')))  # Redirect to the appropriate page
        return render_template('update_order_status.html', order=order)  # Render the form template
    except Exception as e:
        flash(f'An error occurred while updating order status: {str(e)}', 'error')
        return redirect(url_for('staff.view_current_orders'))

@staff_bp.route('/customers', methods=['GET'])
def view_customers():
    try:
        customers = Customer.query.all()
        return render_template('view_customers.html', customers=customers)
    except Exception as e:
        flash(f'An error occurred while retrieving customers: {str(e)}', 'error')
        return redirect(url_for('staff.dashboard'))

@staff_bp.route('/customers/<int:customer_id>', methods=['GET'])
def view_customer_details(customer_id):
    try:
        customer = Customer.query.get_or_404(customer_id)  # Fetch the customer by ID or return a 404 error
        return render_template('view_customer_details.html', customer=customer)  # Pass the customer to the template
    except Exception as e:
        flash(f'An error occurred while retrieving customer details: {str(e)}', 'error')
        return redirect(url_for('staff.view_customers'))

@staff_bp.route('/sales', methods=['GET'])
def total_sales():
    try:
        current_date = date.today()
        week_start = current_date - timedelta(days=current_date.weekday())
        month_start = current_date.replace(day=1)
        year_start = current_date.replace(month=1, day=1)

        weekly_sales = db.session.query(db.func.sum(Payment.payment_amount)).filter(Payment.payment_date >= week_start).scalar() or 0
        monthly_sales = db.session.query(db.func.sum(Payment.payment_amount)).filter(Payment.payment_date >= month_start).scalar() or 0
        yearly_sales = db.session.query(db.func.sum(Payment.payment_amount)).filter(Payment.payment_date >= year_start).scalar() or 0

        return render_template('sales_report.html', weekly_sales=weekly_sales, monthly_sales=monthly_sales, yearly_sales=yearly_sales)
    except Exception as e:
        flash(f'An error occurred while retrieving sales data: {str(e)}', 'error')
        return redirect(url_for('staff.dashboard'))

@staff_bp.route('/popular-items', methods=['GET'])
def popular_items():
    try:
        popular_items = db.session.query(
            OrderLine.item_number,
            db.func.sum(OrderLine.amount).label('total_quantity')
        ).group_by(OrderLine.item_number).order_by(db.desc('total_quantity')).limit(10).all()

        items = []
        for item_id, total_quantity in popular_items:
            item = Item.query.get(item_id)
            items.append({'item': item, 'total_quantity': total_quantity})

        return render_template('popular_items.html', items=items)
    except Exception as e:
        flash(f'An error occurred while retrieving popular items: {str(e)}', 'error')
        return redirect(url_for('staff.dashboard'))

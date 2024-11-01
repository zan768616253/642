from datetime import datetime

from faker import Faker
from app import create_app, db
from app.models import (
    Person, Customer, Staff, CorporateCustomer, Veggie, Item,
    WeightedVeggie, PackVeggie, UnitPriceVeggie, PremadeBox,
    Order, Payment, CreditCardPayment, DebitCardPayment, OrderLine
)
import random

from app.models.payment import PaymentMethod

fake = Faker()


# Helper functions
def create_person(person_type):
    person = Person(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        username=fake.unique.user_name(),
        password="password",
        type=person_type
    )
    return person


def create_customer():
    person = create_person('customer')
    customer = Customer.create_customer_with_person(
        person=person,
        cust_address=fake.address(),
        cust_balance=fake.random_number(digits=4),
        max_owing=fake.random_number(digits=4)
    )
    return customer


def create_staff():
    person = create_person('staff')
    staff = Staff.create_staff_with_person(
        person=person,
        date_joined=fake.date_this_decade(),
        dept_name=fake.company_suffix()
    )
    return staff


def create_corporate_customer():
    customer = create_customer()
    corp_customer = CorporateCustomer.create_corporate_customer_with_customer(
        customer=customer,
        discount_rate=fake.random_number(digits=2),
        max_credit=fake.random_number(digits=5),
        min_balance=fake.random_number(digits=3)
    )
    return corp_customer


def create_order(customer_id):
    order = Order(
        order_customer_id=customer_id,
        order_date=fake.date_this_year(),
        order_number=fake.unique.bothify(text='ORD-#####'),
        order_status=random.choice(['Pending', 'Completed', 'Shipped'])
    )
    return order


def create_payment(customer_id, type):
    payment = Payment(
        payment_customer_id=customer_id,
        payment_date=fake.date_this_year(),
        payment_amount=fake.random_number(digits=4),
        type=type
    )
    return payment


def get_fake_expiry_date():
    expiry_date_str = fake.credit_card_expire()
    return datetime.strptime(expiry_date_str, "%m/%y").date().replace(day=1)


def create_credit_card_payment(customer_id):
    payment = create_payment(customer_id, PaymentMethod.CREDIT_CARD.value)
    credit_card_payment = CreditCardPayment.create_credit_card_payment_with_payment(
        payment=payment,
        card_number=fake.credit_card_number(),
        card_expiry_date=get_fake_expiry_date(),
        card_type=random.choice(['VISA', 'MASTERCARD', 'AMEX'])
    )
    return credit_card_payment


def create_debit_card_payment(customer_id):
    payment = create_payment(customer_id, PaymentMethod.DEBIT_CARD.value)
    debit_card_payment = DebitCardPayment.create_debit_card_payment_with_payment(
        payment=payment,
        bank_name=fake.company(),
        debit_card_number=fake.bban()
    )
    return debit_card_payment


def create_premade_box(size):
    premade_box = PremadeBox(
        box_size=size,
        prize=fake.random_number(digits=3)
    )
    return premade_box



def create_weighted_veggie():
    weighted_veggie = WeightedVeggie.create_weighted_veggie_with_veggie(
        veg_name=fake.word(),
        price_per_unit=fake.random_number(digits=2)
    )
    return weighted_veggie


def create_pack_veggie():
    pack_veggie = PackVeggie.create_pack_veggie_with_veggie(
        veg_name=fake.word(),
        price_per_unit=fake.random_number(digits=3)
    )
    return pack_veggie


def create_unit_price_veggie():
    unit_price_veggie = UnitPriceVeggie.create_unit_price_veggie_with_veggie(
        veg_name=fake.word(),
        price_per_unit=fake.random_number(digits=2)
    )
    return unit_price_veggie


def create_order_line(order_id, item_id):
    order_line = OrderLine(
        order_id=order_id,
        item_number=item_id,
        amount=random.randint(1, 10)
    )
    return order_line


def create_test_user():
    person_customer = Person(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        username="test_customer",
        password="password",
        type="customer"
    )
    customer = Customer.create_customer_with_person(
        person=person_customer,
        cust_address=fake.address(),
        cust_balance=fake.random_number(digits=4),
        max_owing=fake.random_number(digits=4)
    )

    person_staff = Person(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        username="test_staff",
        password="password",
        type="staff"
    )

    staff = Staff.create_staff_with_person(
        person=person_staff,
        date_joined=fake.date_this_decade(),
        dept_name=fake.company_suffix()
    )
    return customer, staff

def seed_data():
    for _ in range(5):
        customer = create_customer()
        db.session.add(customer)
        db.session.commit()

        staff = create_staff()
        db.session.add(staff)
        db.session.commit()

        corporate_customer = create_corporate_customer()
        db.session.add(corporate_customer)
        db.session.commit()

        order = create_order(customer.cust_id)
        db.session.add(order)
        db.session.commit()

        if random.choice(['credit_card', 'debit_card']) == 'credit_card':
            credit_card_payment = create_credit_card_payment(customer.cust_id)
            db.session.add(credit_card_payment)
            db.session.commit()
        else:
            debit_card_payment = create_debit_card_payment(customer.cust_id)
            db.session.add(debit_card_payment)
            db.session.commit()

        subtype = random.choice(['weighted_veggie', 'pack_veggie', 'unit_price_veggie'])
        if subtype == 'weighted_veggie':
            item = create_weighted_veggie()
            db.session.add(item)
            db.session.commit()
        elif subtype == 'pack_veggie':
            item = create_pack_veggie()
            db.session.add(item)
            db.session.commit()
        else:
            item = create_unit_price_veggie()
            db.session.add(item)
            db.session.commit()

        order_line = create_order_line(order.id, item.id)
        db.session.add(order_line)
        db.session.commit()

    box1 = create_premade_box('L')
    box2 = create_premade_box('S')
    db.session.add(box1)
    db.session.commit()

    db.session.add(box2)
    db.session.commit()

    test_user, test_staff = create_test_user()
    db.session.add(test_user)
    db.session.add(test_staff)
    db.session.commit()



if __name__ == "__main__":
    app = create_app()  # Instantiate your Flask app
    with app.app_context():
        db.create_all()  # Ensure all tables are created
        seed_data()  # Run your data creation function
        db.session.commit()  # Commit the changes to the database
        print("Database seeding completed.")

from app import db
import enum


class PaymentMethod(enum.Enum):
    CREDIT_CARD = "CREDIT_CARD"
    DEBIT_CARD = "DEBIT_CARD"


class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    payment_customer_id = db.Column(db.Integer, db.ForeignKey('customers.cust_id'), nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    payment_amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(100), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'payment',
        'polymorphic_on': type
    }

    def __init__(self, payment_customer_id, payment_date, payment_amount, type):
        self.payment_customer_id = payment_customer_id
        self.payment_date = payment_date
        self.payment_amount = payment_amount
        self.type = type

import enum
from sqlalchemy import Enum

from app import db
from .payment import Payment, PaymentMethod

class CardType(enum.Enum):
    VISA = "VISA"
    MASTERCARD = "MASTERCARD"
    AMEX = "AMEX"  # You can add more card types if needed

class CreditCardPayment(Payment):
    __tablename__ = 'credit_card_payments'

    id = db.Column(db.Integer, db.ForeignKey('payments.id'), primary_key=True)
    card_number = db.Column(db.String(50), nullable=False)
    card_expiry_date = db.Column(db.Date, nullable=False)
    card_type = db.Column(Enum(CardType), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': PaymentMethod.CREDIT_CARD.value
    }

    def __init__(self, payment_customer_id, payment_date, payment_amount, card_number, card_expiry_date, card_type):
        super().__init__(payment_customer_id, payment_date, payment_amount, PaymentMethod.CREDIT_CARD.value)
        self.card_number = card_number
        self.card_expiry_date = card_expiry_date
        self.card_type = card_type

    @staticmethod
    def create_credit_card_payment_with_payment(payment, card_number, card_expiry_date, card_type):
        return CreditCardPayment(
            payment_customer_id=payment.payment_customer_id,
            payment_date=payment.payment_date,
            payment_amount=payment.payment_amount,
            card_number=card_number,
            card_expiry_date=card_expiry_date,
            card_type=card_type
        )

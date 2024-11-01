from .customer import Customer
from .payment import Payment, PaymentMethod

from app import db

class DebitCardPayment(Payment):
    __tablename__ = 'debit_card_payments'

    id = db.Column(db.Integer, db.ForeignKey('payments.id'), primary_key=True)
    bank_name = db.Column(db.String(100), nullable=False)
    debit_card_number = db.Column(db.String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': PaymentMethod.DEBIT_CARD.value
    }

    def __init__(self, payment_customer_id, payment_date, payment_amount, bank_name, debit_card_number):
        super().__init__(payment_customer_id, payment_date, payment_amount, PaymentMethod.DEBIT_CARD.value)
        self.bank_name = bank_name
        self.debit_card_number = debit_card_number

    @staticmethod
    def create_debit_card_payment_with_payment(payment, bank_name, debit_card_number):
        return DebitCardPayment(
            payment_customer_id=payment.payment_customer_id,
            payment_date=payment.payment_date,
            payment_amount=payment.payment_amount,
            bank_name=bank_name,
            debit_card_number=debit_card_number
        )

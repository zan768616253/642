from .customer import Customer

from app import db

class CorporateCustomer(Customer):
    __tablename__ = 'corporate_customers'

    corp_id = db.Column(db.Integer, db.ForeignKey('customers.cust_id'), primary_key=True)  # Changed to corp_id
    discount_rate = db.Column(db.Float, nullable=False)
    max_credit = db.Column(db.Float, nullable=False)
    min_balance = db.Column(db.Float, nullable=False)

    __mapper_args__ = {'polymorphic_identity': 'corporate_customer'}

    def __init__(self, first_name, last_name, username, password, cust_address, cust_balance, max_owing, discount_rate, max_credit, min_balance):
        super().__init__(first_name, last_name, username, password, cust_address, cust_balance, max_owing)
        self.discount_rate = discount_rate
        self.max_credit = max_credit
        self.min_balance = min_balance

    @staticmethod
    def create_corporate_customer_with_customer(customer, discount_rate, max_credit, min_balance):
        return CorporateCustomer(
            first_name=customer.first_name,
            last_name=customer.last_name,
            username=customer.username,
            password=customer.password,
            cust_address=customer.cust_address,
            cust_balance=customer.cust_balance,
            max_owing=customer.max_owing,
            discount_rate=discount_rate,
            max_credit=max_credit,
            min_balance=min_balance
        )


    def apply_discount(self, amount):
        return amount * (1 - self.discount_rate / 100)
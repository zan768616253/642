from app import db
from .person import Person, PersonType


class Customer(Person):
    __tablename__ = 'customers'

    cust_id = db.Column(db.Integer, db.ForeignKey('persons.id'), primary_key=True)
    cust_address = db.Column(db.String(200), nullable=False)
    cust_balance = db.Column(db.Float, nullable=False)
    max_owing = db.Column(db.Float, nullable=False)

    __mapper_args__ = {'polymorphic_identity': PersonType.CUSTOMER.value, 'inherit_condition': cust_id == Person.id}

    def __init__(self, first_name, last_name, username, password, cust_address, cust_balance, max_owing):
        super().__init__(first_name, last_name, username, password, PersonType.CUSTOMER.value)
        self.cust_address = cust_address
        self.cust_balance = cust_balance
        self.max_owing = max_owing


    @staticmethod
    def create_customer_with_person(person, cust_address, cust_balance, max_owing):
        return Customer(
            first_name=person.first_name,
            last_name=person.last_name,
            username=person.username,
            password=person.password,
            cust_address=cust_address,
            cust_balance=cust_balance,
            max_owing=max_owing
        )

from app import db

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_customer_id = db.Column(db.Integer, db.ForeignKey('customers.cust_id'), nullable=False)
    order_date = db.Column(db.Date, nullable=False)
    order_number = db.Column(db.String(100), nullable=False, unique=True)  # Added unique constraint
    order_status = db.Column(db.String(50), nullable=False)

    def __init__(self, order_customer_id, order_date, order_number, order_status):
        self.order_customer_id = order_customer_id
        self.order_date = order_date
        self.order_number = order_number
        self.order_status = order_status

    def update_status(self, new_status):
        self.order_status = new_status

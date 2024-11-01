from app import db

class OrderLine(db.Model):
    __tablename__ = 'order_lines'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    item_number = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False, default=1)

    # Add the relationship to the Item model
    item = db.relationship('Item', backref='order_lines')

    def __init__(self, order_id, item_number, amount):
        self.order_id = order_id
        self.item_number = item_number
        self.amount = amount

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


import logging
logging.basicConfig()
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.DEBUG)

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/642'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret_key'

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        from .models import Person

        return Person.query.get(int(user_id))

    with app.app_context():
        from .models import (
            person, staff, customer, corporate_customer, order, order_line, item, veggie,
            weighted_veggie, pack_veggie, unit_price_veggie, premade_box, payment, credit_card_payment, debit_card_payment
        )
        # Create database tables if they don't exist
        db.create_all()

        from .routes import auth, customer, staff

        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(customer.customer_bp)
        app.register_blueprint(staff.staff_bp)

    return app

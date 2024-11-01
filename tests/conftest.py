import pytest
from app import create_app, db as _db

@pytest.fixture(scope='session')
def app():
    app = create_app()
    app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI='sqlite:///:memory:',  # Use an in-memory SQLite database for testing
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    with app.app_context():
        _db.create_all()  # Create tables

    yield app  # This will be the app used for tests

    with app.app_context():
        _db.drop_all()  # Clean up the database after tests


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

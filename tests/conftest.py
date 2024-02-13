import pytest

from pythonvilag_website import app, db
from tests.db_setup import setup_db


@pytest.fixture(scope="session")
def client():
    app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        },
    )
    with app.test_client() as client:  # noqa: SIM117
        with app.app_context():
            db.create_all()
            setup_db()

            yield client

            db.session.remove()
            db.drop_all()

import pytest
from pythonvilag_website import app


@pytest.fixture(scope="session")
def client():
    app.config.update({"TESTING": True})
    with app.test_client() as client:  # noqa: SIM117
        with app.app_context():
            yield client

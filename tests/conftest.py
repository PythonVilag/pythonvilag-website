import pytest

from pythonvilag_website import app, db
from pythonvilag_website.models import Assessment, Category, Lesson, Mentors


@pytest.fixture(scope="session")
def client():
    with app.test_client() as client:
        yield client

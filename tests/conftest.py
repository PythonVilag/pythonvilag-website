import pytest

from pythonvilag_website import app, db  # noqa: F401
from pythonvilag_website.models import Assessment  # noqa: F401
from pythonvilag_website.models import Category  # noqa: F401
from pythonvilag_website.models import Lesson  # noqa: F401
from pythonvilag_website.models import Mentors  # noqa: F401


@pytest.fixture(scope="session")
def client():
    with app.test_client() as client:
        yield client

"""
Database structures.

Type ignores are needed because of: https://github.com/python/mypy/issues/8603

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

from datetime import UTC, datetime

from pythonvilag_website import db


class Category(db.Model):  # type: ignore[name-defined, misc]
    """Category properties."""

    id = db.Column(db.Integer, primary_key=True)  # noqa: A003
    order = db.Column(db.Integer)
    category = db.Column(db.String(50), nullable=False)
    subcategory = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    image = db.Column(db.String(50), nullable=False, default="default.png")
    lessons = db.relationship("Lesson", backref="Category", lazy=True)

    def __repr__(self) -> str:  # noqa: ANN101, D105
        return f'Category("{self.category}", "{self.title}")'


class Lesson(db.Model):  # type: ignore[name-defined, misc]
    """Lesson properties."""

    id = db.Column(db.Integer, primary_key=True)  # noqa: A003
    order = db.Column(db.Integer)
    date_posted = db.Column(db.String(25), nullable=False, default=datetime.now(tz=UTC).strftime("%Y-%m-%d"))
    title = db.Column(db.String(50), unique=True, nullable=False)
    url = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    secret_word = db.Column(db.String(30), unique=True)
    image = db.Column(db.String(50), nullable=False, default="default.png")

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    assessments = db.relationship("Assessment", backref="Lesson", lazy=True)

    def __repr__(self) -> str:  # noqa: ANN101, D105
        return f'Lesson("{self.title}", "{self.date_posted}")'


class Assessment(db.Model):  # type: ignore[name-defined, misc]
    """Assessment properties."""

    id = db.Column(db.Integer, primary_key=True)  # noqa: A003
    order = db.Column(db.Integer)
    question = db.Column(db.String(500), nullable=False)
    options = db.Column(db.String(5000), nullable=False)
    answer = db.Column(db.String(500), nullable=False)

    lesson_id = db.Column(db.Integer, db.ForeignKey("lesson.id"), nullable=False)

    def __repr__(self) -> str:  # noqa: ANN101, D105
        return f'Assessment("{self.question}", "{self.answer}")'


class Mentors(db.Model):  # type: ignore[name-defined, misc]
    """Mentor properties."""

    id = db.Column(db.Integer, primary_key=True)  # noqa: A003
    order = db.Column(db.Integer)
    channel_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    image = db.Column(db.String(50), nullable=False, default="default.png")
    youtube_link = db.Column(db.String(1000))

    def __repr__(self) -> str:  # noqa: ANN101, D105
        return f'Mentor("{self.channel_name}")'

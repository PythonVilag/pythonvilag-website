"""
Available website URLs.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from flask import abort, render_template, request, send_file
from werkzeug.exceptions import HTTPException

import pythonvilag_website.modules.checkmark.routes  # noqa: F401, RUF100
import pythonvilag_website.modules.private_lecture_automation.routes  # noqa: F401
from pythonvilag_website import app, db
from pythonvilag_website.models import Assessment, Category, Lesson, Mentors

if TYPE_CHECKING:
    from flask.wrappers import Response


# Basic
@app.route("/")
def open_home() -> str:
    """Home page of the website."""
    return render_template("site/home.html", title="Python Világ")


@app.route("/daniel-mizsak")
def open_cv() -> Response:
    """My not most up-to-date CV, without contact information."""
    cv_document = (Path(__file__).parent / "static/documents/daniel-mizsak-cv.pdf").resolve()
    return send_file(cv_document, download_name="daniel-mizsak-cv.pdf")


@app.route("/mentors")
def open_mentors() -> str:
    """A collection of content creators that helped me understand different topics."""
    mentors = db.session.execute(db.select(Mentors).order_by(Mentors.order)).scalars()
    return render_template("site/mentors.html", mentors=mentors, title="Mentoraim")


@app.route("/faq")
def open_faq() -> str:
    """Frequently asked questions about the website or me."""
    return render_template("site/faq.html", title="Gyakran Ismételt Kérdések")


# Categories, subcategories, lessons and assessments
@app.route("/pv/<category>/")
def open_category(category: str) -> str:
    """Page of the queried category. Lists the available subcategories within the category."""
    subcategories = (
        db.session.execute(
            db.select(Category).filter_by(category=category).order_by(Category.order),
        )
        .scalars()
        .all()
    )
    if len(subcategories) != 0:
        return render_template(
            "site/category.html",
            category=category,
            subcategories=subcategories,
            title=f"{category.title()} | Python Világ",
        )
    return abort(404)


@app.route("/pv/<category>/<subcategory>/")
def open_subcategory(category: str, subcategory: str) -> str:
    """Page of the queried subcategory. Lists the available lessons within the subcategory."""
    all_posts = db.session.execute(db.select(Category)).scalars().all()
    all_categories = {post.category for post in all_posts}
    all_subcategories = {post.subcategory for post in all_posts}

    if (category in all_categories) and (subcategory in all_subcategories):
        category_id = db.session.execute(
            db.select(Category.id).filter_by(category=category, subcategory=subcategory),
        ).scalar_one()
        lessons = (
            db.session.execute(
                db.select(Lesson).filter_by(category_id=category_id).order_by(Lesson.order),
            )
            .scalars()
            .all()
        )
        title = db.session.execute(
            db.select(Category.title).filter_by(id=category_id),
        ).scalar_one()
        return render_template(
            "site/subcategory.html",
            category=category,
            subcategory=subcategory,
            title=f"{title} | Python Világ",
            lessons=lessons,
        )
    return abort(404)


@app.route("/pv/<category>/<subcategory>/<url>/")
def open_lesson(category: str, subcategory: str, url: str) -> str:
    """Page of the queried lesson. Contains the lesson's content."""
    category_id = db.session.execute(
        db.select(Category.id).filter_by(category=category, subcategory=subcategory),
    ).scalar_one()
    lesson = db.session.execute(
        db.select(Lesson).filter_by(category_id=category_id, url=url),
    ).scalar_one()
    if lesson:
        title = f'{lesson.title.split("(")[0]} ' + "| Python Világ"
        return render_template(
            f"post/{category}/{subcategory}/{url}.html",
            category=category,
            subcategory=subcategory,
            title=title,
            lesson=lesson,
        )
    return abort(404)


@app.route("/pv/<category>/<subcategory>/<url>/assessment/", methods=["GET", "POST"])
def open_assessment(category: str, subcategory: str, url: str) -> str:
    """Page of the queried assessment. Contains the assessment's content."""
    category_id = db.session.execute(
        db.select(Category.id).filter_by(category=category, subcategory=subcategory),
    ).scalar_one()
    lesson_id = db.session.execute(
        db.select(Lesson.id).filter_by(category_id=category_id, url=url),
    ).scalar_one()

    questions = (
        db.session.execute(db.select(Assessment).filter_by(lesson_id=lesson_id).order_by(Assessment.order))
        .scalars()
        .all()
    )
    title = db.session.execute(db.select(Lesson.title).filter_by(id=lesson_id)).scalar_one()
    if len(questions) != 0:
        secret_word = db.session.execute(
            db.select(Lesson.secret_word).filter_by(category_id=category_id, url=url),
        ).scalar_one()
        for index, _ in enumerate(questions):
            questions[index].options = questions[index].options.split("\n")

        answers = {}
        if request.method == "POST":
            for question in questions:
                answers[question.question] = request.form.get(question.question)

        return render_template(
            "site/assessment.html",
            title=title,
            questions=questions,
            answers=answers,
            secret_word=secret_word,
        )
    return abort(404)


# Error handler
@app.errorhandler(HTTPException)  # type: ignore[type-var]
def error_handler(error: HTTPException) -> tuple[str, int | None]:
    """Error handler for the website."""
    return render_template(f"errors/{error.code}.html"), error.code

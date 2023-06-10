"""
Available website URLs.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""
# mypy: no-warn-return-any
# Ignore warn-return-any because abort() returns Any

from __future__ import annotations

import os

from checkmark.server.routes import checkmark_page
from flask import abort, flash, render_template, request, send_file  # noqa: F401
from flask.wrappers import Response
from private_lecture_automation import send_introduction_email
from werkzeug.exceptions import HTTPException

from pythonvilag_website import app, cache, csrf
from pythonvilag_website.forms import PrivateLectureInfoForm
from pythonvilag_website.models import Assessment, Category, Lesson, Mentors


# Basic
@app.route("/")
@cache.cached(timeout=86400)
def open_home() -> str:
    """Home page of the website."""
    return render_template("site/home.html", title="Python Világ")


@app.route("/daniel-mizsak")
def open_cv() -> Response:
    """My not most up-to-date CV, without contact information."""
    cv_document = os.path.join(os.path.dirname(__file__), "static/documents/daniel-mizsak-cv.pdf")
    return send_file(cv_document, download_name="daniel-mizsak-cv.pdf")


@app.route("/mentors")
def open_mentors() -> str:
    """A collection of content creators that helped me understand different topics."""
    mentors = Mentors.query.order_by(Mentors.order).all()
    return render_template("site/mentors.html", mentors=mentors, title="Mentoraim")


@app.route("/faq")
def open_faq() -> str:
    """Frequently asked questions about the website or me."""
    return render_template("site/faq.html", title="Gyakran Ismételt Kérdések")


# Categories, subcategories, lessons and assessments
@app.route("/pv/<category>/")
@cache.cached(timeout=86400)
def open_category(category: str) -> str:
    """Page of the queried category. Lists the available subcategories within the category."""
    subcategories = Category.query.order_by(Category.order).filter_by(category=category).all()
    if len(subcategories) != 0:
        return render_template(
            "source/category.html",
            category=category,
            subcategories=subcategories,
            title=f"{category.title()} | Python Világ",
        )
    return abort(404)


@app.route("/pv/<category>/<subcategory>/")
@cache.cached(timeout=86400)
def open_subcategory(category: str, subcategory: str) -> str:
    """Page of the queried subcategory. Lists the available lessons within the subcategory."""
    all_posts = Category.query.all()
    all_categories = set([post.category for post in all_posts])
    all_subcategories = set([post.subcategory for post in all_posts])

    if (category in all_categories) and (subcategory in all_subcategories):
        category_id = (
            Category.query.filter_by(category=category, subcategory=subcategory).first().id
        )
        lessons = Lesson.query.filter_by(category_id=category_id).all()
        title = Category.query.filter_by(id=category_id).first().title
        return render_template(
            "source/subcategory.html",
            category=category,
            subcategory=subcategory,
            title=f"{title} | Python Világ",
            lessons=lessons,
        )
    return abort(404)


@app.route("/pv/<category>/<subcategory>/<url>/")
@cache.cached(timeout=86400)
def open_lesson(category: str, subcategory: str, url: str) -> str:
    """Page of the queried lesson. Contains the lesson's content."""
    category_id = Category.query.filter_by(category=category, subcategory=subcategory).first().id
    lesson = Lesson.query.filter_by(category_id=category_id, url=url).first()
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
    category_id = Category.query.filter_by(category=category, subcategory=subcategory).first().id
    lesson_id = Lesson.query.filter_by(category_id=category_id, url=url).first().id

    questions = Assessment.query.order_by(Assessment.order).filter_by(lesson_id=lesson_id).all()
    title = Lesson.query.filter_by(id=lesson_id).first().title
    if len(questions) != 0:
        secret_word = Lesson.query.filter_by(category_id=category_id, url=url).first().secret_word
        for index, _ in enumerate(questions):
            questions[index].options = questions[index].options.split("\n")

        answers = {}
        if request.method == "POST":
            for question in questions:
                answers[question.question] = request.form.get(question.question)

        return render_template(
            "source/assessment.html",
            title=title,
            questions=questions,
            answers=answers,
            secret_word=secret_word,
        )
    return abort(404)


# Projects
# checkmark
csrf.exempt(checkmark_page)
app.register_blueprint(checkmark_page, url_prefix="/checkmark")


# private-lecture-automation
@app.route("/private-lecture", methods=["GET", "POST"])
def private_lecture() -> str:
    """Sends out an email including the information about my private lectures."""
    form = PrivateLectureInfoForm()
    if request.method == "POST" and form.validate_on_submit():
        try:
            send_introduction_email(
                recipient_email=form.email.data,
                values_to_replace={"NAME": form.name.data},
            )
            flash("Az üzenetet sikeresen elküldtük!", "flash-success")
        except Exception:  # TODO: Specify exception
            flash("Az üzenetet nem sikerült elküldeni!", "flash-error")
    return render_template("site/private_lecture.html", title="Különóra", form=form)


# Error handler
# mypy: no-warn-unused-ignores
# Ignore the type because mypy does not recognize the error handler decorator.
@app.errorhandler(HTTPException)  # type: ignore
def error_handler(error: HTTPException) -> tuple[str, int | None]:
    """Error handler for the website."""
    return render_template(f"errors/{error.code}.html"), error.code

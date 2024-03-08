"""
Import and add the private lecture automation module to the app.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

from flask import flash, render_template, request  # noqa: I001

from pythonvilag_website import app, csrf
from pythonvilag_website.modules.private_lecture_automation.forms import PrivateLectureInfoForm

if app.config["PRIVATE_LECTURE_AUTOMATION"]:
    from private_lecture_automation import send_introduction_email

    @app.route("/private-lecture", methods=["GET", "POST"])
    @csrf.exempt  # type: ignore[misc]
    def private_lecture() -> str:
        """Sends out an email including the information about my private lectures."""
        form = PrivateLectureInfoForm()
        if request.method == "POST":  # TODO: Should use form.validate_on_submit(), but currently csrf breaks
            try:
                send_introduction_email(
                    recipient_email=form.email.data,
                    included_images=["logo.png"],
                    values_to_replace={"NAME": form.name.data, "PRICE": "10000 HUF"},
                )
                flash("Az üzenetet sikeresen elküldtük!", "flash-success")
            except Exception:  # noqa: BLE001
                # TODO: Specify exception
                flash("Az üzenetet nem sikerült elküldeni!", "flash-error")
        return render_template(
            "modules/private_lecture_automation/private_lecture.html",
            title="Különóra",
            form=form,
        )

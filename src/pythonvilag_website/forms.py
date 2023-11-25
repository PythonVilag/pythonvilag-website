"""
Forms used in the website.

@author "Dániel Lajos Mizsák" <info@pythonvilag.hu>
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class PrivateLectureInfoForm(FlaskForm):  # type: ignore [misc]
    """Form for information about private lecture request."""

    name = StringField("Név", validators=[DataRequired()])
    email = StringField("E-mail cím", validators=[DataRequired(), Email()])

    submit = SubmitField("Küldés")

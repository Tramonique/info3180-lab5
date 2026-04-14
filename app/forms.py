from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileRequired

class MovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    poster = FileField(
        "Poster",
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "jpeg", "png", "gif", "webp"], "Images only!")
        ]
    )
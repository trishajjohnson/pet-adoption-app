from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import NumberRange, Optional, InputRequired, URL, number_range, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding a new pet."""

    name = StringField("Name", validators=[InputRequired(message="Please enter a name")])
    species = StringField("Species", validators=[InputRequired(message="Please enter a species"), AnyOf(("cat", "dog", "porcupine"), message="Species must be either 'cat', 'dog' or 'porcupine'", values_formatter=None)])
    photo_url = StringField("Image URL", validators=[Optional(), URL(require_tld=True, message="Must be a valid URL")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")


class EditPetForm(FlaskForm):
    """For, editing pet detail."""

    photo_url = StringField("Image URL", validators=[Optional(), URL(require_tld=True, message="Must be a valid URL")])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")

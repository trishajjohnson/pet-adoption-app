from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class AddPetForm(FlaskForm):
    """Form for adding a new pet."""

    name = StringField("Name")
    species = StringField("Species")
    photo = StringField("Image URL")
    age = IntegerField("Age")
    notes = StringField("Notes")
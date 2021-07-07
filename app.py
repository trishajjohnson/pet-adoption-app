"""Pet Adoption application."""

from re import A
from flask import Flask, render_template, redirect
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_db(app)

# db.drop_all()
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)



@app.route("/")
def show_homepage():
    """Shows homepage, welcome message and link to all users page"""
    pets = Pet.query.all()

    return render_template("base.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def new_pet_form():
    """Shows new pet form."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data or None
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)

        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('add-pet-form.html', form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def show_edit_pet_detail(pet_id):
    """Displays pet dail page and edit form"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        
        pet.photo_url = form.photo_url.data or None
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return redirect(f"/")

    else:

        return render_template('pet-detail.html', pet=pet, form=form)

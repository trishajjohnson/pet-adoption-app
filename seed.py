"""Seed file to make sample data for pet_adoption_db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
# User.query.delete()

# Add sample users
pet1 = Pet(name="Lou", species="Miniature Dachschund", photo_url="https://scontent-hou1-1.xx.fbcdn.net/v/t1.6435-9/31416937_10108206631316876_2469879101716955136_n.jpg?_nc_cat=109&ccb=1-3&_nc_sid=730e14&_nc_ohc=PSCpuFqsMKgAX-xvu6E&_nc_ht=scontent-hou1-1.xx&oh=03813adeef274cb29219a9d05cfa3d4b&oe=60E79306", age=10, notes="Sweet as pie!", available=False)
pet2 = Pet(name="Whiskers", species="Scottish Fold", photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Adult_Scottish_Fold.jpg/1200px-Adult_Scottish_Fold.jpg", age=2, notes="Soft and cuddly!", available=True)
pet3 = Pet(name="Porky", species="Hedgehog", photo_url="https://media-be.chewy.com/wp-content/uploads/2019/10/22152634/hedgehog-ball.jpg", age=1, notes="The only love you'll ever need!", available=True)
pet4 = Pet(name="Shelby", species="Potbelly Pig", age=2, notes="Some of the most lovable and friendly pets you can have!", available=True)

# Add new objects to session, so they'll persist
db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)
db.session.add(pet4)

# Commit--otherwise, this never gets saved!
db.session.commit()
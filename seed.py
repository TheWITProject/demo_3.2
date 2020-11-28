from models import Animal

def seed(sessionmaker):
    session = sessionmaker()

    # if you changed your models, you may need to fix this!
    wilbur = Animal(
        name="Wilbur",
        species="pig",
        sound="oink",
    )

    session.add(wilbur) # great, we added one... but how can we be add more and be efficient?
    session.commit()
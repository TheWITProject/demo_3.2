## Summary
You will be demoing how to create and seed models for our zoo schema using SQLAlchemy.

## Installation
```
# in your postgres cluster, create a database named "zoo"
createdb zoo

# clone this repo
git clone <this repo's remote url>

# enter directory
cd demo_3.2

# create a virtual environment for this project & activate
virtualenv env
source env/bin/activate

# install the requirments
pip install -r requirements.txt

# run application
python app.py
```

## Instructions

**Table Definition**
- We have already defined a `Zoo` and `Animal` models. Use these to demo the basic syntax for model and relationship definitions.
- Extend this by extracting some to their own tables (e.g., `Species` and `Address`). Let students dictate the syntax to you to define these and their relationships.

**Final Schema**
- You should have the following tables: `Zoo`, `Animal`, `Species`, & `Address`
- `Zoos` and `Address` are one-to-one
- `Zoos` and `Animals` are one-to-many
- `Species` and `Animals` are one-to-many

**Seeding**
- Show students how you can use SQLAlchemy to seed the database. There is one example already set up in `seed.py`. It might need to be edited if `species` and `sound` were extracted.
- Show students how lists and loops can be utilized to seed more efficiently.
- Optional: it might be helpful to demo an association method to set data about relationships.

**Demoing**
- Make sure to show changes to the tables in Postico.


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship

Base = declarative_base()

# MANY-TO-MANY
# AnimalZoo = Table(
#     'AnimalZoo',
#     Base.metadata,
#     Column('animal_id', Integer, ForeignKey("animals.id")),
#     Column('zoo_id', Integer, ForeignKey("zoos.id"))
# )

class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String) # optional: extract to new Species Table
    sound = Column(String) # optional: extract to new Species Table
    birthday = Column(Date) 

    # ONE-TO-ONE
    zoo_id = Column(Integer, ForeignKey("zoos.id"))
    zoo = relationship("Zoo", back_populates="animal")

    # ONE-TO-MANY
    # zoo_id = Column(Integer, ForeignKey("zoos.id"))
    # zoo = relationship("Zoo", back_populates="animal")


class Zoo(Base):
    __tablename__ = "zoos"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String) # optional: extract to new Address table

    # ONE-TO-ONE
    animal = relationship("Animal", back_populates="zoo", uselist=False)

    # ONE-TO-MANY
    # animals = relationship("Animal", back_populates="zoo")

    # #MANY-TO-MANY
    # animals = relationship("Animal", secondary=AnimalZoo, back_populates="zoos")

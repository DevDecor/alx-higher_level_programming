#!/usr/bin/python3
"""use SQLAlchemy


"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """States class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship(State, back_populates='cities')


State.cities = relationship(City,
                            order_by=City.id,
                            back_populates="state",
                            cascade="all, delete, delete-orphan")

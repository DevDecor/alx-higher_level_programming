#!/usr/bin/python3
"""use SQLAlchemy


"""
from sqlalchemy import Column, Integer, String
from model_city import Base, City
from sqlalchemy.orm import relationship


class State(Base):
    """States class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', order_by=City.id,
                          back_populates="state")


City.state = relationship('State', back_populates='cities')

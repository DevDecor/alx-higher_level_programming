#!/usr/bin/python3
"""use SQLAlchemy


"""
from sqlalchemy import Column, Integer, String
from relationship_city import City, Base
from sqlalchemy.orm import relationship

class State(Base):
    """States class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(City,
                                order_by=City.id,
                                back_populates="state",
                                cascade="all, delete, delete-orphan")


City.state = relationship('State', back_populates='cities')

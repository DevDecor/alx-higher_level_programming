#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
#from relationship_state import Base, State
from relationship_state import City, State, Base

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)
    cali = State(name='California')
    Session.add(cali)
    Session.commit()
    #cali = Session.query(State).filter_by(name=cali.name).first()
    Session.add(City(name='San Francisco', state_id=cali.id))
    Session.commit()

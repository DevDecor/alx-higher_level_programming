#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_city import Base, State, City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)()
    users = Session.query(City).join(State).all()
    for user in users:
        print(f'{user.state.name}: ({user.id}) {user.name}')

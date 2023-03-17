#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    rows = session.query(State).first()

    if rows:
        print("{}: {}".format(rows.__dict__['id'], rows.__dict__['name']))
    else:
        print("Nothing")

    session.close()

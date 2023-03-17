#!/usr/bin/python3
"""
prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    rows = session.query(State).all()
    rp = "''"

    for i in rows:
        if state in i.__dict__['name']:
            rp = i.__dict__['id']
    if rp != "":
        print(rp)
    else:
        print('Not Found')

    session.close()

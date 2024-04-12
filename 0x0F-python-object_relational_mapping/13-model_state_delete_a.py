#!/usr/bin/python3
'''lists all State objects from the database hbtn_0e_6_usa'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    states_to_delete = session.query(State)\
                              .filter(State.name.like('%a%')).all()
    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)
        session.commit
    session.close()

#!/usr/bin/python3
"""
A script to connect to the database
and get first row from the state table
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, MetaData, Column, String, Integer

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()

    if state is not None:
        print(f"{state.id}: {state.name}")
    else:
        print(f"Nothing")

    session.close()

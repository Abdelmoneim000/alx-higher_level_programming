#!/usr/bin/python3
"""
A file that contains the class
definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import MetaData, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ A class to retrieve the State table"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)

#!/usr/bin/python3
'''Python file that contains the class definition of a City and an instance'''
from sqlalchemy import Column, Integer, String
from model_state import Base


class City(Base):
    '''City class that inherits from Base'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))

#!/usr/bin/python3
from sqlalchemy import column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class state(Base):
    __tablename__ = "states"
    id = column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = column(String(128), nullable=False)
        

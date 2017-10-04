__author__ = 'Alex'
import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'Users'

    UserID = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String)
    LastName = Column(String)
    UserName = Column(String)
    Password = Column(String)

    def __repr__(self):
        return "<User(FirstName='%s', LastName='%s', UserName='%s', Password='%s')>" % (
            self.FirstName, self.LastName, self.UserName, self.Password)
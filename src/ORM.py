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

Base.metadata.create_all(engine)
ed_user = User(FirstName='Alex', LastName='Simpson', UserName='asimpson440', Password='password')

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()
session.add(ed_user)
our_user = session.query(User).filter_by(FirstName='Alex').first()
session.add_all([
    User(FirstName='Tom', LastName='Harry', UserName='tharry123', Password='123456'),
    User(FirstName='Jen', LastName='Caron', UserName='jcaron456', Password='ajkldas'),
    User(FirstName='Brady', LastName='Candy', UserName='bcandy789', Password='asdf')])
ed_user.Password = "alotoftime"
print(session.new)
session.commit()
print(ed_user.UserID)
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    # print object representation, used for printing(debugging)
    def __repr__(self):
        return "<User (name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)

Base.metadata.create_all(engine)

# add new user
u = User(name='Bojan', fullname='BojanF', nickname='bojan')
session.add(u)

# query user
our_user = session.query(User).filter_by(name='Bojan').first() 

# change user parameter
our_user.nickname = 'bojan bojan'

# commit changes to DB
session.commit()

print(our_user)


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

# multiple insertions
session.add_all([
    User(name='Bojan1', fullname='BojanF1', nickname='bojan1'),
    User(name='Bojan2', fullname='BojanF2', nickname='bojan2'),
    User(name='Bojan3', fullname='BojanF3', nickname='bojan3'),
    User(name='Bojan4', fullname='BojanF4', nickname='bojan4'),
    User(name='Bojan5', fullname='BojanF5', nickname='bojan5')]
    )

# multiple querying
for instance in session.query(User).order_by(User.id):
    print(instance)


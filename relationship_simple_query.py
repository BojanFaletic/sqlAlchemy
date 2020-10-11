import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# basic one to many relationship


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


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)

    # relationship with User db
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='addresses')

    def __repr__(self):
      return f"<Address(email_address={self.email_address}"

# connect user to address
User.addresses = relationship("Address", order_by=Address.id, back_populates="user")

Base.metadata.create_all(engine)

# create new user
jack = User(name='jack', fullname='Jack Bean', nickname='gjffdd')

# add address to user
jack.addresses = [
  Address(email_address='jack@google.com'),
  Address(email_address='j25@yahoo.com')]


session.add(jack)
session.commit()

# query jack by jack's address
jack = session.query(User).join(Address).filter(Address.email_address=='jack@google.com').all()

print(jack)
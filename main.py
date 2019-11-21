from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import fire


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<User(name='%s')>" % self.name


def create_database():
    engine = create_engine('sqlite:///users.db')
    Base.metadata.create_all(engine)


def create_user():
    engine = create_engine('sqlite:///users.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    me = User(name='gotcha')
    session.add(me)
    session.commit()


def query_user():
    engine = create_engine('sqlite:///users.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    print(session.query(User).filter_by(name='gotcha').first())


if __name__ == '__main__':
    fire.Fire()

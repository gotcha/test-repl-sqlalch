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
        return "<User(id='%s', name='%s')>" % (self.id, self.name)


def create_database():
    engine = create_engine('sqlite:///users.db')
    Base.metadata.create_all(engine)


def create_user(name='gotcha'):
    engine = create_engine('sqlite:///users.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    me = User(name=name)
    session.add(me)
    session.commit()


def query_user(name='gotcha'):
    engine = create_engine('sqlite:///users.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    print(session.query(User).filter_by(name=name).all())


if __name__ == '__main__':
    fire.Fire()

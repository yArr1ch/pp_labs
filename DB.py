from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, ForeignKey

engine = create_engine("mysql+mysqlconnector://root:mysql123@localhost:3306/Dbpp6")
engine.connect()

SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)
Base = declarative_base()

class Tag(Base):
    __tablename__ = 'Tag'
    idTag = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(20), nullable=False)

class User(Base):
    __tablename__ = 'User'
    idUser = Column(Integer, nullable=False, primary_key=True)
    username = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False)
    User = relationship("Note", backref='User')
    Tag_idTag = Column(Integer, ForeignKey('Tag.idTag'))
    Tag = relationship("Note", backref='Tag')

class Note(Base):
    __tablename__ = 'Note'
    idNote = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(20), nullable=False)
    text = Column(String(20), nullable=False)
    idOwner = Column(Integer, nullable=False)

class NoteStatistics(Base):
    __tablename__ = 'NoteStatistics'
    time = Column(String(20), nullable=False)
    idNote = Column(Integer, ForeignKey('Note.idNote'), primary_key=True)
    Note = relationship("NoteStatistics", backref='Note')

if __name__ == "__main__":
    Base.metadate.create_all(engine)

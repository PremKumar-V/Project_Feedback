from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from .models import Base

engine = create_engine("sqlite:///db.db")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

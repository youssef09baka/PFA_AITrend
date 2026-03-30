from sqlalchemy import Column, Integer, String, Float
from database import Base

class Trend(Base):
    __tablename__ = "trends"

    id = Column(Integer, primary_key=True)
    topic = Column(String)
    growth = Column(Integer)
    competition = Column(Integer)
    score = Column(Float)
from __init__ import Base

from sqlalchemy import *


class Vozilo (Base):
    __tablename__ = "vozila"
    ID_vozila = Column(Integer, primary_key = True)
    marka = Column(String(50))
    model =Column(String(50))
    godina =Column(Integer)
    registracijska_oznaka =Column(String(50))
    dostupno =Column(String(10))
    cijena_najma = Column(Integer)
    
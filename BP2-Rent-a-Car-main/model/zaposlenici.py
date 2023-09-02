from __init__ import Base

from sqlalchemy import *


class Zaposlenik (Base):
    __tablename__ = "zaposlenici"
    ID_zaposlenika = Column(Integer, primary_key = True)
    ime = Column(String(50))
    prezime =Column(String(50))
    email = Column(String(50))
    broj_telefona=Column(Integer)
    radno_mjesto = Column(String(50))

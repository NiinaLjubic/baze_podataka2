from __init__ import Base
from sqlalchemy import *


class Korisnik (Base):
    __tablename__ = "korisnici"
    ID_korisnika = Column(Integer, primary_key = True)
    ime = Column(String(50))
    prezime =Column(String(50))
    email = Column(String(50))
    password=Column(String(50))
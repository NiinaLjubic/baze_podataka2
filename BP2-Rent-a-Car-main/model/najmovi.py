from __init__ import Base
from datetime import datetime
from sqlalchemy import *


class Najam (Base):
    __tablename__ = "najam"
    ID_najma = Column(Integer, primary_key = True)
    vozilo_id = Column(Integer, ForeignKey('vozila.ID_vozila'))
    korisnik_id = Column(Integer, ForeignKey('korisnici.ID_korisnika'))
    datum_najma = Column(DateTime, default=datetime.now)
    datum_povrata = Column(DateTime)
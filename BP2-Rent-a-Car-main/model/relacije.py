
from sqlalchemy.orm import relationship
from korisnici import Korisnik
from najmovi import Najam
from vozila import Vozilo
from zaposlenici import Zaposlenik
from recenzije import Recenzija
from __init__ import Base
from __init__  import engine


Korisnik.najam = relationship('Najam', back_populates='korisnik')
Vozilo.najam = relationship('Najam', back_populates='vozila')
Korisnik.recenzija = relationship("Recenzija", back_populates="korisnik")
Najam.recenzija = relationship("Recenzija", back_populates="najam")


Base.metadata.bind = engine
Base.metadata.create_all(bind=engine)
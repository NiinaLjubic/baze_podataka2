from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("mysql+pymysql://ednevnik:csdigital@mysql:3306/ednevnik") 

""" engine = create_engine("mysql+pymysql://root:@localhost:3306/rentcar") """

Session = sessionmaker(bind=engine)

Session = Session()

Base = declarative_base()
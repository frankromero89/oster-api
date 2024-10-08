from sqlalchemy import Column, Date, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.environ.get("DATABASE_URI")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    paternal_lastname = Column(String(64), nullable=False)
    maternal_lastname = Column(String(64), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    mobile_phone = Column(String(20), nullable=False)
    land_line = Column(String(20), nullable=True)
    street = Column(String(256), nullable=False)
    block = Column(String(64), nullable=False)
    postal_code = Column(String(20), nullable=False)
    locality = Column(String(64), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(1), nullable=False)
    ticket_folio = Column(String(64), nullable=False)
    purchase_date = Column(Date, nullable=False)
    purchase_amount = Column(Float, nullable=False)
    store = Column(String(64), nullable=False)
    terminal = Column(String(20), nullable=False)
    seller = Column(String(64), nullable=False)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

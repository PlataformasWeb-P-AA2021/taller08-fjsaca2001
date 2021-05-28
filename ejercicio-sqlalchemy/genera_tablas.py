from ast import Str
from cgitb import strong
from itertools import count
from re import L
from sqlalchemy import column, create_engine, false, null, true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Mundial(Base):
    __tablename__ = 'mundial'
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer, nullable=false)
    fifaDisplayName = Column(String, nullable=false)
    country = Column(String, nullable=false)
    lastName = Column(String, nullable=false)
    firstName = Column(String, nullable=false)
    shirtName = Column(String, nullable=false)
    pos = Column(String, nullable=false)
    height = Column(Integer,nullable=false)
    caps = Column(Integer, nullable=false)
    goals = Column(Integer, nullable=false)

    def __repr__(self) -> str:
        return "Jugador: Número: %d - FIFANombre: %s - Country: %s - LastName: %s - FirstName: %s - ShirtName: %s - Pos: %s - Height: %d - Caps: %d - Goals: %d"\
            % (
                self.numero,
                self.fifaDisplayName,
                self.country,
                self.lastName,
                self.firstName,
                self.shirtName,
                self.pos,
                self.height,
                self.caps,
                self.goals
            )

Base.metadata.create_all(engine)
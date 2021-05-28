from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Mundial
from configuracion import cadena_base_datos

import csv

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo provincia

# leer el archivo de datos

with open('data/mundial2018.csv') as File:
    read = csv.reader(File, delimiter='|')
    next(read)
    for x in read:
        jugador = Mundial(numero=x[0],fifaDisplayName=x[1], country=x[2], lastName=x[3], firstName=x[4], shirtName=x[5], pos=x[6], height=x[7], caps=x[8], goals=x[9])
        session.add(jugador)
            
session.commit()


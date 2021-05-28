from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Mundial

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine('sqlite:///mundial2018.db')


Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad mundial 
jugadores = session.query(Mundial).order_by(desc(Mundial.height)).all()

print("Presentación de todos los jugadores ordenados por su altura")
print("\n", jugadores,"\n")

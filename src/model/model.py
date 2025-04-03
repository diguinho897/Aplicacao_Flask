# 1) Realizar a criação das tabelas dos bancos de dados.
from flask_sqlalchemy import SQLAlchemy


# Instanciar database
db = SQLAlchemy()

# criar classes

class Sensor(db.Model):
    # cria as "colunas da classe"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String, nullable = False) 
    status = db.Column(db.String, nullable = False) 

    # Define uma exibição, ao realizar o print da classe
    def __repr__(self) -> str:
        return f"<- Sensor: {self.nome} -> "
    
class Comodo(db.Model):
    # cria as "colunas da classe"
    id = db.Column(db.Integer, primary_key = True, autoincrement =True)
    nome = db.Column(db.String, nullable = False)
    
    # Cria um id referencia para casa, como um foreign key
    casa_id = db.Column(db.Integer, db.ForeignKey('casa.id'), nullable = False)

    # Define uma exibição, ao realizar o print da classe
    def __repr__(self) -> str:
        return f"<- Comodo: {self.nome} Referencia casa_id: {self.casa_id} ->"
    
class Casa(db.Model):
    # cria as "colunas da classe"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    endereco = db.Column(db.String, nullable = False) 
    cidade = db.Column(db.String, nullable = False)
    
    # cria o relacionamento de casa com comodo 
    comodo = db.relationship('Comodo', backref='casa', lazy=True)
    
    # Define uma exibição, ao realizar o print da classe
    def __repr__(self) -> str:
        return f"<- Endereco: {self.endereco}->"

# Cria relação nxn entre comodo e sensores
comodo_x_sensores = db.Table('helper_table_comodo_x_sensores', 
                             db.Column('comodo_id', db.Integer, db.ForeignKey('comodo.id'), primary_key = True),
                             db.Column('sensor_id', db.Integer, db.ForeignKey('sensor.id'), primary_key = True)
)

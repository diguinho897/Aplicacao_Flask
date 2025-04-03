# 2) Instanciar o banco de dados para verificar se esta tudo ok

# importa a instancia de db das tabelas da classe model 2)
from src.model.model import db 

# importa o flask 2)
from flask import Flask 

# importa o arquivo de rotas 6) 
from src.routes.routes import routes

# 3) Instanciar e configurar o mqtt
# realiza importação do mqtt 3)
from paho.mqtt import client 

# conecta um client ao broker 3)
sender_log = client.Client(client_id="sender_log")

# definir uma função para quando realizar a conexão ao broker 3)
def when_connected_to_broker(client, userdata, flags, rc):
    print("Você realizou uma conexão com o broker.")

# passa a função de conexão ao broker 3)
sender_log.on_connect = when_connected_to_broker
# realiza a conexão 3)
sender_log.connect("localhost", 1883)


# realiza configuração do flask e do sqlite 2)
# instancia app do flask 2)
app = Flask(__name__)

# configura o sqlite 2)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nome_database.db'

# inclui o arquivo routes.py ao flask 6)
app.register_blueprint(routes)

# inicia o banco de dados com flask 2)
db.init_app(app)

# roda o arquivo completo 
with app.app_context():
    # cria todas as tabelas
    db.create_all()



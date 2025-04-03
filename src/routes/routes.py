# 5) Quinto passo, realizar a criação das rotas

# importar os arquivos necessários do flask
from flask import jsonify, Blueprint, request, json

# importar as tabelas do banco de dados
from src.model.model import Casa, Comodo, Sensor, db

# acoplando as rotas do arquivo routes.py ao flask do arquivo main.py
routes = Blueprint("routes", __name__)


# Define alguns codigo para sucesso e erro
CODE_INSERT_SUCESS = 201
CODE_UPDATE_SUCESS = 201
CODE_GET_SUCESS = 200

CODE_ERROR = 404
 
# definindo as rotas
@routes.route("/api/v1/insert-insert-new-casa/<topic>", methods = ["GET", "POST"])
def inser_new_casa(topic):
    # aqui, precisaremos realizar um "lazy import" para podermos ao realizar a requisição na uri, também publicar a mesmsa em um topico.
    from main import sender_log
    URI = "/api/v1/insert-insert-new-casa/<topic>"
    
    # verificamos se é um POST
    if request.method == "POST":
        # pegamos o json passado no corpo.
        new_casa = json.loads(request.data)
        # mostra o dado passado no terminal 
        print(new_casa)
        # cria um novo dado para ser encaminhado para o banco de dados
        new_data = Casa(
            endereco = new_casa['endereco'],
            cidade = new_casa['cidade']
        )
        # realiza tratamento de erros
        try:
            db.session.add(new_data)
            db.session.commit()
            
            # cria uma mensagem para exibir no terminal do mqtt
            message_success = f"{URI} | Insercao de nova casa realizada com sucesso | Code: {CODE_INSERT_SUCESS}"
            # realiza a publicação do mesmo no terminal do mqtt de acordo com o <topic> passado
            sender_log.publish(topic, message_success)
            
            # realiza um retorno para a web 
            return jsonify({
                "Message": message_success,
                "Code":CODE_INSERT_SUCESS,
            }), CODE_INSERT_SUCESS
            
        except Exception as ex:
            # Em caso de erros:
            message_error = f"{URI} | Erro ao realizar inserção de nova casa | Code: {CODE_ERROR}"
            return jsonify({
                "Message":message_error,
                "Message_Interno": ex
            }), CODE_ERROR
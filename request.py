# 7) Realizar um request 
import requests as req
import getpass as gp
import json 
# cria um dado para inserção de uma nova casa
nova_casa = {
    "endereco":"Rua 999, jardim abc - SP",
    "cidade": "Araras",
    "comodo":"Quarto"
}

"""
NO CASO DE RODAR ISSO NA FACULDADE, PRECISAREMOS CRIAR UMA FUNÇÃO DE PROXY 
"""
def proxies():
    user = input("User: ")
    password = gp.getpass("Senha: ")

    url = "http://" + user + ":" + password + "@127.0.0.1:5000"

    proxies = {
        'http': url, 
        'https': url,
    }

    return proxies


# para realizar um post
topico = "casa"
URL = f"api/v1/insert-insert-new-casa/{topico}"
# CODIGO PARA REALIZAR REQUEST NA FACULDADE
# resp = req.post(f"http://localhost:5000/{URL}", data=json.dumps(nova_casa), proxies=proxies())

# Codigo para executar fora da faculdade
resp = req.post(f"http://localhost:5000/{URL}", data=json.dumps(nova_casa))

# mostra qual foi o status code de retorno
print(resp.status_code)

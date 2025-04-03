# Instruções para desenvolvimento da MA - Sistemas Distribuidos

- Primeiro passo:
    Realizar a criação das tabelas dos bancos de dados (Arquivo: model.py)
- Segundo passo:
    Instanciar a classe do banco de dados para verificar se esta tudo ok (Arquivo: main.py)
    OBS: Se tudo estiver ok, ao rodar, ira criar uma nova pasta (instance) com um arquivo defino na configuração do sqlite

- Terceiro passo:
    Instancia e configurar o mqtt (Arquivo: main.py)
- Quarto Passo:
    Iniciar o mosquitto no terminal (entrar dentro da pasta do mesmo e iniciar de acordo com as configurações necessárias)
    - Iniciar o mosquitto:
        .\mosquitto.exe -v
    - Realizar um subscribe (inscrição) no mosquitto:
        .\mosquitto_sub.exe -h localhost -p 1883 -t "topico"
    - Realizar um publisher (publicação) no mosquitto:
        .\mosquitto_pub.exe -h localhost -p 1883 -t "topico" -m "mensagem"

- Quinto Passo:
    Realizar as configurações das rotas, onde será necessário definir as URL de acesso, como get, post, update, delete ... (Arquivo: routes.py)

- Sexto Passo:
    Incluir o arquivo routes.py ao main.py 

- Sétimo passo:
    Realiza um request na uri criada para teste, por ex, a uri criada foi a:
    uri = "/api/v1/insert-insert-new-casa/<topic>"
    logo, para realizar o request na mesma, precisaremos:
    - Criar um novo arquivo na raiz do projeto com o nome de request.py

- Oitavo passo:
    Realizar o request no terminal.
        Abrir um novo terminar e rodar o código, por ex:
            python request.py


RETORNO ESPERADO AO REALIZAR A REQUISIÇAÕ DO REQUEST.PY
![alt text](Retorno_Esperado.png)

ORGANIZAÇÃO FINAL DOS ARQUIVOS:
![alt text](Organizacao_Pastas_Arquivos.png)


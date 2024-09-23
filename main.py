# do modulo flask importamos a classe Flask
# url_for -> serve para monstar urls internas do nosso servidor web
# de acordo com o nome da funcao da rota que voce deseja
from flask import Flask
from routes.home import home_route
from routes.cliente import cliente_route

# criando a variavel que recebe a classe flask
app = Flask(__name__) # o name identifica e organiza os recursos que construimos no nosso projeto

app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')

# chamando a funcao responsavel por executar nosso servidor web
# debug=True -> estamos indicando ao flask que estamos no modo desenvolvedor
# assim ele sempre recarrega o servidor web quando editamos e salvamos um arquivo
app.run(debug=True)
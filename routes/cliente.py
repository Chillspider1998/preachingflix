from flask import Blueprint, render_template

# o primeiro parametro recebe o nome da nossa blueprint e em seguida o parametro padrao do flask
cliente_route = Blueprint('cliente', __name__)

# definindo nossas rotas usando blueprint
@cliente_route.route('/')
def listar_clientes():
    """ listar os clientes """
    return render_template('listar_clientes.html')

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ inserir os dados do cliente no bd """
    pass

@cliente_route.route('/new')
def form_novo_cliente():
    """ formulario de cadastro de clientes """
    return render_template('form_novo_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ exibe informacoes de um cliente especifico """
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_editar_cliente(cliente_id):
    """ editar informacoes de um cliente especifico """
    return render_template('form_editar_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ atualizar informacoes de um cliente especifico """
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """ deletar informacoes de um cliente especifico """
    pass
from flask import Blueprint, render_template

# o primeiro parametro recebe o nome da nossa blueprint e em seguida o parametro padrao do flask
home_route = Blueprint('home', __name__)

# definindo nossa rota
@home_route.route('/')
def home():
    return render_template('index.html')
from flask import Flask
from database import db
from flask_migrate import Migrate, migrate
from jogotecaproject import blueprint_jogos


app = Flask(__name__)

conexao = "sqlite:///meubanco.sqlite"

app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(blueprint_jogos, url_prefix='/jogoteca')

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from database import db


class Jogo(db.Model):
    __tablename__ = 'jogo'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    plataforma = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    avaliacao = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def __init__(self, titulo, plataforma, categoria, descricao, avaliacao, preco):
        self.titulo = titulo
        self.plataforma = plataforma
        self.categoria = categoria
        self.descricao = descricao
        self.avaliacao = avaliacao
        self.preco = preco

    def __repr__(self):
        return 'Jogo: {}'.format(self.titulo)

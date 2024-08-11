from flask import Blueprint
from flask import redirect
from flask import request
from flask.templating import render_template

from database import db
from models import Jogo

blueprint_jogos = Blueprint('jogos', __name__, template_folder='templates', static_folder='static')


@blueprint_jogos.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('jogo_create.html')

    if request.method == 'POST':
        titulo = request.form.get("titulo")
        plataforma = request.form.get("plataforma")
        categoria = request.form.get("categoria")
        descricao = request.form.get("descricao")
        avaliacao = request.form.get("avaliacao")
        preco = request.form.get("preco")

        jogo = Jogo(titulo, plataforma, categoria, descricao, avaliacao, preco)
        db.session.add(jogo)
        db.session.commit()

    return redirect('/jogoteca/recovery')


@blueprint_jogos.route('/recovery')
def recovery():
    jogos = Jogo.query.all()
    return render_template('jogo_recovery.html', jogos=jogos)


@blueprint_jogos.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    jogo = Jogo.query.get(id)

    if request.method == 'GET':
        return render_template('jogo_update.html', jogo=jogo)

    if request.method == 'POST':
        titulo = request.form.get("titulo")
        plataforma = request.form.get("plataforma")
        categoria = request.form.get("categoria")
        descricao = request.form.get("descricao")
        avaliacao = request.form.get("avaliacao")
        preco = request.form.get("preco")

        jogo.titulo = titulo
        jogo.plataforma = plataforma
        jogo.categoria = categoria
        jogo.descricao = descricao
        jogo.avaliacao = avaliacao
        jogo.preco = preco

        db.session.add(jogo)
        db.session.commit()

        return redirect('/jogoteca/recovery')


# route delete by id user
@blueprint_jogos.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    jogo = Jogo.query.get(id)

    if request.method == 'GET':
        return render_template('jogo_delete.html', jogo=jogo)

    if request.method == 'POST':
        db.session.delete(jogo)
        db.session.commit()
        return redirect('/jogoteca/recovery')

from flask import Flask, render_template, request, redirect, session, flash, url_for
from models import Jogo, Usuario
from dao import JogoDao
from flask_mysqldb import MySQL




app = Flask(__name__)
app.secret_key = 'alura'

app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "1234"
app.config['MYSQL_DB'] = "jogoteca"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)
jogo_dao = JogoDao(db)

usuario1 = Usuario('thiago448', 'thiago', 'thiago')
usuario2 = Usuario('alineaclina', 'Aline', 'gatita')
usuarios = {usuario1.id: usuario1,
            usuario2.id: usuario2}

@app.route('/')
def index():
    lista = jogo_dao.listar()
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo jogo') 


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima, titulo='Manager DevOps')


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)

    else:
        flash('Não logado, tente de novo!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado')
    return redirect(url_for('index'))


# MY CREATE


@app.route('/cadastre')
def cadastre():
    proxima = request.args.get('proxima')
    return render_template('cadastro.html', proxima=proxima)


@app.route('/efetuarcadastro', methods=['POST', ])
def efetuarcadastro():
    id = request.form['id']
    nome = request.form['cadastrouser']
    senha = request.form['cadastrosenha']
    usuarios = []
    user = Usuario(id, nome, senha)
    usuarios.append(user)
    return redirect(url_for('login'))


app.run(host='127.0.0.1', debug=True)

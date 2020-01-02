from flask import Flask, render_template, request, redirect, session, flash, url_for
app = Flask(__name__)
app.secret_key = 'eueumesmo'


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Super Mario', 'Acao', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'LutA', 'SNES')
lista = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

usuario1 = Usuario('thiago448','thiago','thiago')
usuario2 = Usuario('alineaclina','Aline', 'gatita')
usuarios= {usuario1.id:usuario1,
          usuario2.id: usuario2}


@app.route('/')
def index():
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
    lista.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima, titulo='Teckne')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)

    else :
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
    return render_template ('cadastro.html', proxima=proxima)
    
@app.route('/efetuarcadastro', methods=['POST',])
def efetuarcadastro():
    id = request.form['id']
    nome = request.form['cadastrosenha']
    senha = request.form['cadastrosenha']
    user = Usuario (id, nome, senha) 
    usuarios.append(user)
    return redirect (url_for('login'))



app.run(debug=True)


class Jogo:
    def __init__(self, nome, categoria, console, id=None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.console = console


class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

class Status:
    def __init__(self,qte, status, Jogo):
        self.qte= qte       
        self.status = status
        self.Jogo = Jogo
    

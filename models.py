
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
    def __init__(self, ClassStatus, status, NameStatus):
        self.ClassStatus = ClassStatus
        self.status = status
        self.NameStatus = NameStatus

    def Boards(self, id, titulo, nome, Boardstatus):
        self.id = id
        self.titulo = titulo
        self.nome = nome
        self.Boardstatus = Boardstatus

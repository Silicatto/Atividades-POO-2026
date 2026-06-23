from datetime import date 

class Presenca:
    def __init__(self, ID:int, data:date) -> None:
        self.ID = ID
        self.data = data

class pessoa:
    def __init__(self, CPF:str, nome:str) -> None:
        self.CPF = CPF
        self.nome = nome
        self.listaPresenca = []
    def addPresenca(self, ID:int, data:date) -> None:
        self.listaPresenca.append(Presenca(ID, data))

class docente(pessoa):
    def __init__(self, CPF:str, nome:str, salario:float) -> None:
        super().__init__(CPF, nome)
        self.salario = salario

class Atividade:
    def __init__(self, codigo:int, descricao:str, valor:float) -> None:
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor

class estudante(pessoa):
    def __init__(self, CPF:str, nome:str, RA:str) -> None:
        super().__init__(CPF, nome)
        self.RA = RA
        self.listaAtividade = []
    def addAtividade(self, atv:Atividade) -> None:
        self.listaAtividade.append(atv)
    

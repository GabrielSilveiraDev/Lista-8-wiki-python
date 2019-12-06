class Pessoa:

    def __init__(self, nome, idade, altura):

        self.nome = nome
        self.altura = altura
        self.idade = idade

    def setNome(self, nome):

        self.nome = nome

    def setIdade(self, idade):

        self.idade = idade

    def setAltura(self, altura):

        self.altura = altura

    def getNome(self):

        return self.nome

    def getIdade(self):

        return self.idade

    def getAltura(self):

        return self.altura
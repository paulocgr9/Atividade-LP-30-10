class Produto:
    def __init__(self, nome, marca, preço):
        self.nome = nome
        self.marca = marca
        self.preço = preço

    def obter_codigo_de_barras(self):
        pass

class Sabão(Produto):
    def __init__(self, nome, marca, preço):
        super().__init__(nome, marca, preço)

    def obter_codigo_de_barras(self):
        return "789" + "600370516" + self.marca.value

    def tomar_banho(self):
        print("Você tomou banho")

class Absorvente(Produto):
    def __init__(self, nome, marca, preco):
        super().__init__(nome, marca, preco)

    def obter_codigo_de_barras(self):
        return "789" + "023285809" + self.marca.value

    def menstruar(self):
        print("O absorvente segurou o seu sangue")

class EscovaDeDente(Produto):
    def __init__(self, nome, marca, preco):
        super().__init__(self, nome, marca, preco)
    
    def obter_codigo_de_barras(self):
        return "789" + "677564728" + self.marca.value

    def escovar_o_dente(self):
        print("Sua boca não é mais um bueiro")

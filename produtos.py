# A classe produto é geral. Como os códigos de barras dependem da categoria de produto,
# Ela não implementa a geração de código de barras, apenas mostra que existe

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
        # O código de barras depende da classe de produto e da marca dele
        return "789" + "600370516" + str(self.marca.value)

    def tomar_banho(self):
        # Cada tipo de produto tem funções específicas de coisas que só o produto faz
        print("Você tomou banho")

class Absorvente(Produto):
    def __init__(self, nome, marca, preco):
        super().__init__(nome, marca, preco)

    def obter_codigo_de_barras(self):
        return "789" + "023285809" + str(self.marca.value)

    def menstruar(self):
        print("O absorvente segurou o seu sangue")

class EscovaDeDente(Produto):
    def __init__(self, nome, marca, preco):
        super().__init__(self, nome, marca, preco)
    
    def obter_codigo_de_barras(self):
        return "789" + "677564728" + str(self.marca.value)

    def escovar_o_dente(self):
        print("Sua boca não é mais um bueiro")

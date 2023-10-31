class Produto:
    def __init__(self, nome, marca, preco):
        self.nome = nome
        self.marca = marca
        self.preco = preco

    def obter_codigo_de_barras(self):
        pass

class Sabao(Produto):
    def __init__(self, nome, marca, preco):
        super().__init__(nome, marca, preco)

    def obter_codigo_de_barras(self):
        return "789" + "600370516" + self.marca.value

class Absorivente(Produto):
    def __init__(self, nome, marca, preco):
        super().__init__(nome, marca, preco)

    def obter_codigo_de_barras(self):
        return "789" + "0232858" + self.marca.value

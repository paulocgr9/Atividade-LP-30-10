import excecoes as exc

class Inventario:
    def __init__(self, nome):
        self.nome = nome
        self.estoque = dict()

    def adicionar_produto(self, produto, quantidade):
        codigo_de_barras = produto.obter_codigo_de_barras()
        if codigo_de_barras not in self.estoque:
            self.estoque[codigo_de_barras] = quantidade
        else:
            self.estoque[codigo_de_barras] += quantidade

    def vender_produto(self, produto, quantidade):
        codigo_de_barras = produto.obter_codigo_de_barras()
        
        if codigo_de_barras not in self.estoque:
                raise exc.ProdutoNaoDisponivel
        
        elif self.estoque[codigo_de_barras] < quantidade:
                raise exc.QuantidadeNaoDisponivel
            
        else:
            self.estoque[codigo_de_barras] -= quantidade
            print(f"O {produto} foi vendido!")
        
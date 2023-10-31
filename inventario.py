import excecoes as exc

# Definida a classe inventário contendo um nome de inventário e seu conteúdo
class Inventario:
    def __init__(self, nome):
        self.nome = nome
        self.estoque = dict()

    # Método de adicionar produto ao inventário
    def adicionar_produto(self, produto, quantidade):
        codigo_de_barras = produto.obter_codigo_de_barras()
    
    # Caso o produto não exista, ele é criado e passa a ter a quantidade informada
        if codigo_de_barras not in self.estoque:
            self.estoque[codigo_de_barras] = quantidade
    # Caso o produto exista, soma-se a quantidade atual à quantidade passada
        else:
            self.estoque[codigo_de_barras] += quantidade
            print(f"Adicionado {quantidade} {produto.nome} no estoque.")

    # Método de vender produtos
    def vender_produto(self, produto, quantidade):
        codigo_de_barras = produto.obter_codigo_de_barras()
        
        # Tratamento de erro para caso o produto não esteja no inventário
        if codigo_de_barras not in self.estoque:
            raise exc.ProdutoNaoDisponivel(f"O produto {produto.nome} não existe no estoque")
        
        # Tratamento de erro para caso a quantidade em estoque seja insuficiente para a venda
        elif self.estoque[codigo_de_barras] < quantidade:
            raise exc.QuantidadeNaoDisponivel(f"Não existem {quantidade} {produto.nome} no estoque, apenas {self.estoque[codigo_de_barras]}")

        # Tratamento de erro caso a quantidade solicitada seja menor ou igual a 0
        elif quantidade <= 0:
            raise exc.QuantidadeInvalida(f"A quantidade informada não pode ser devolvida. A quantidade deve ser um número inteiro maior que 1.")

        # Remove a quantidade vendida do inventário e avisa que a venda foi bem sucedida
        else:
            self.estoque[codigo_de_barras] -= quantidade
            print(f"O {produto} foi vendido!")


    # Método para retornar/devolver produtos
    def retornar_produto(self, produto, quantidade):
        codigo_de_barras = produto.obter_codigo_de_barras()

    # Tratamento de erro para caso o produto não exista
        if codigo_de_barras not in self.estoque:
            raise exc.ProdutoNaoDisponivel(f"O produto {produto} não pode ser devolvido.")
        
    # Tratamento de erro para caso a quantidade a ser devolvida seja menor que zero
        elif quantidade <= 0:
            raise exc.QuantidadeInvalida(f"A quantidade informada não pode ser devolvida. A quantidade deve ser um número inteiro maior que 1.")
        
    # Aumenta a quantidade em estoque e informa que a devolução foi bem sucedida
        else:
            self.estoque[codigo_de_barras] += quantidade
            print(f"O produto {produto} foi retornado com sucesso.")

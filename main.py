import produtos
import enums
import inventario
import excecoes

# DRIVER CODE COM EXEMPLOS EXPLICADOS

# Cria um invetario. No caso, cada instancia de inventário
# Representa um inventário de um aloja diferente
inventario_lojas = inventario.Inventario("Lojas Guilherme")

# Cria um sabao cracrá. Cada instancia de um sabão representa um
# Sabão de uma marca diferente
sabao_craca = produtos.Sabão("Sabão Cracrá", enums.MarcasSabao.CRACRA, 9999)

# Adiciona no inventário da loja 5 sabãos cracrá
inventario_lojas.adicionar_produto(sabao_craca, 5)

# Vende 3 sabãos cracrá
inventario_lojas.vender_produto(sabao_craca, 3)

# Se alguem tentar comprar mais sabãos do que tem no estoque, explode
try:
    inventario_lojas.vender_produto(sabao_craca, 40)
except excecoes.QuantidadeNaoDisponivel as e:
    print(e)

absorvente_dracula = produtos.Absorvente("Absorvente Drácula", enums.MarcasAbsorvente.DRACULA, 88)

# Se o produto não tiver sido adicionado anteriormente o erro é diferente
try:
    inventario_lojas.vender_produto(absorvente_dracula, 1)
except excecoes.ProdutoNaoDisponivel as e:
    print(e)

# Devolver produto é semelhabnte ao adicionar produto porem só funciona se o produto existir no estoque
inventario_lojas.retornar_produto(sabao_craca, 20)

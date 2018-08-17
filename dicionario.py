estoque = {"Alface": [1000, 2.50],
           "Tomate": [456, 8.90],
           "Batata": [1673, 1.20],
           "Feijão": [2345, 6.75]}
vendas = [["Tomate", 5], ["Feijão", 10], ["Alface", 4]]
valor_total = 0
for venda in vendas:
    produto = venda [0]
    quantidade = venda[1]
    lista_produto = estoque[produto]
    valor = lista_produto[1]
    valor_total = valor_total + (quantidade * valor)
    estoque[produto][0] -= quantidade
print(valor_total)
for produto, lista_produto in estoque.items():
    print("Produto:", produto)
    print("Quantidade:", lista_produto[0])
    print("Valor:", lista_produto[1])
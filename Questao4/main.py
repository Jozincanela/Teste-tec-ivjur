import json
with open('dados_vendas.json') as arquivo:
    vendas = json.load(arquivo)
todas_vendas = {}
for venda in vendas:
    produto = venda['produto']
    quantidade = venda['quantidade']
    preco = venda['preco']
    total_venda = quantidade * preco
    todas_vendas[produto] = todas_vendas.get(produto, 0) + total_venda


produto_mais_vendido = max(todas_vendas, key=todas_vendas.get)
total_vendas_do_mais_vendido = todas_vendas[produto_mais_vendido]


print("Total de vendas por produto:")
for produto, total_vendas in todas_vendas.items():
    print(f"{produto}: R${total_vendas:.2f}")

print(f"\nProduto mais vendido: {produto_mais_vendido}")
print(f"Total de vendas do produto mais vendido: R${total_vendas_do_mais_vendido:.2f}")

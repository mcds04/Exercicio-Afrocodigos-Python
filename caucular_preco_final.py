# Calcular o preço final após um desconto:

def calcular_preco_com_desconto(preco, desconto):
    return preco - (preco * desconto / 100)

preco = 100
desconto = 20
print(calcular_preco_com_desconto(preco, desconto))

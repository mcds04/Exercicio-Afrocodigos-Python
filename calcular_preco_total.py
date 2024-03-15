def calcular_preco_total():
    total = 0
    while True:
        preco = input("Insira o preço da fruta ou 'sair' para terminar: ")
        if preco.lower() == 'sair':
            break
        try:
            total += float(preco)
        except ValueError:
            print("Por favor, insira um número.")
    print("Preço total: ", total)

calcular_preco_total()

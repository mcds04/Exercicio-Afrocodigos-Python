# Remover duplicatas de uma lista:

def remover_duplicatas(lista):
    return list(set(lista))

lista = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print(remover_duplicatas(lista))

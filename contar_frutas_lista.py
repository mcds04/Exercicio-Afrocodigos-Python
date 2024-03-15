# Contar quantas vezes cada fruta aparece em uma lista:

def contar_frutas(lista):
    contagem = {fruta: lista.count(fruta) for fruta in lista}
    return contagem

frutas = ['maçã', 'banana', 'uva', 'abacaxi', 'maçã', 'uva']
print(contar_frutas(frutas))

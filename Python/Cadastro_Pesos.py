# Programa que lê o nome e o peso de varias pessoas,
# guardando tudo em uma lista.
# No final mostra:
# - Quantas pessoas foram cadastradas
# - Uma listagem com as pessoas mais pesadas
# - Uma listagem com as pessoas mais leves#
def linha():
    print("=" * 12)


lista = [[], [], []]
pessoas = 0
while True:
    nome = str(input("Digite o nome"))
    lista[2].append(nome)
    pessoas = pessoas + 1
    peso = float(input("Digite o peso"))
    if peso <= 70:
        lista[0].append(peso)
    else:
        lista[1].append(peso)
    opcao = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if opcao == "N":
        break
linha()
print("Você cadastrou um total de: {} pessoas".format(pessoas))
linha()
print("O peso mais leve é: {}".format(min(lista[0]), lista[2]))
linha()
print("O peso mais pesado é: {}".format(max(lista[1])))

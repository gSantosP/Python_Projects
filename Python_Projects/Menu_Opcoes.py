# Programa que lê 2 valores, faz algumas tarefas
# e mostra um menu com opções na tela.
# [1] Soma, [2] Multiplicação, [3] Maior numero,
# [4] Trocar numeros e [5] Sair do programa.
from time import sleep


def linha():
    print("=" * 12)
linha()
print("Menu de opções")
linha()
n1 = int(input("Digite o primeiro numero"))
n2 = int(input("Digite o segundo numero"))
opção = 0
while True:
    print("")
    print("Escolha uma opção")
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos numeros")
    print("[5] Sair")
    linha()
    opcao = int(input("Digite sua opção"))
    if opcao == 1:
        linha()
        print("A soma dos numeros {} e {}, é: {}".format(n1, n2, n1 + n2))
    elif opcao == 2:
        print("=" * 12)
        print("A multiplicação dos numeros {} e {}, é: {}".format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            linha()
            print("O numero {} é maior que o numero {}".format(n1, n2))
        elif n2 < n1:
            maior = n2
            linha()
            print("O numero {} é maior que o numero {}".format(n2, n1))
        elif n1 == n2:
            print("Os numeros: {} e {} são iguais!".format(n1, n2))
    elif opcao == 4:
            print("=" * 12)
            n1 = int(input("Digite o primeiro numero"))
            n2 = int(input("Digite o segundo numero"))
    elif opcao == 5:
        print("Saindo...")
        sleep(1)
        break

    else:
        linha()
        print("Opção invalida, digite novamente 1 a 5")
        sleep(2)
print("Fim do programa")
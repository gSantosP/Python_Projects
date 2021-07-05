# Programa que simula o funcionamento de um caixa eletronico.
# O programa vai informar quantas cedulas de cada valor serão entregues
# O caixa possui cedulas de:
# R$50, R$20, R$10, R$1
def linha():
    print("=" * 20)

linha()
print("BEM VINDO AO CAIXA ELETRONICO")
linha()
valor = int(input("Digite o valor a ser sacado:"))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total = total - ced
        totalced = totalced + 1
    else:
        if totalced > 0:
            print("Você receberá {} cedulas de {}".format(totalced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total ==0:
            break
print("Volte sempre!")
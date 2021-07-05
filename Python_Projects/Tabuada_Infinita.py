# Programa que calcula a tabuada de qualquer número solicitado
# pelo usuário até o 10. Se o valor digitado for 0, o programa
# termina.#
from time import sleep
# Função para esperar, no caso 1 segundo
def linha():
    print("=" * 21)
# Função definida para criar linhas entre o programa

while True:
    n = int(input("Quer ver a tabuada de qual numero?"))
    linha()
    if n == 0:
        print("Saindo...")
        sleep(1)
        break
    for c in range(0, 10):
        print("{} X {} = {}".format(n, c, n*c))
    linha()
# Loop para executar a tabuada até o 10


# Programa que cria palpites da mega sena.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 numeros entre 1 e 60 para cada jogo.
from random import randint
from time import sleep
print("=-" * 15)
print("GERADOR DE JOGOS MEGA SENA")
print("=-" * 15)
n = int(input("Você quer gerar quantos jogos?"))
for i in range(n):
    jogos = [randint(0, 60), randint(0, 60), randint(0, 60),
             randint(0, 60), randint(0, 60), randint(0, 60)]
    jogos.sort()
    print("Jogo {}: {}".format(i + 1, jogos))
    sleep(1)
print("=-" * 15)
print("BOA SORTE")
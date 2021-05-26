# Programa que mostra os 10 primeiros termos de uma P.A. e
# pergunta para o usuario se ele quer mostrar
# mais alguns termos. o programa encerra quando disser que
# quer mostrar 0 termos
# correção#
print("=" * 10)
print("Gerador de P.A.")
print("=" * 10)
primeiro = int(input("Digite o primeiro termo"))
razao = int(input("Digite a razao"))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
         print("{}".format(termo), end=" ->")
         termo = termo + razao
         cont = cont + 1
    print("Pausa")
    mais = int(input("Quantos termos voce quer mostrar a mais? \n(0 para sair)"))
print("=" * 10)
print("Progressão finalizada com {} termos".format(total))
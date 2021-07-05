"""
Programa para calcular média final. 
Ele recebe 4 notas, depois divide por 4 e por fim,
faz uma verificação se a nota é maior ou menor que 6
Escrito por Gabriel Santos Pereira
"""


print ("Olá este é um programa para calcular média final!")
aluno = str(input("Digite o nome do aluno:"))

#Loop para verificar se o numero inserido é de 0 a 10
while True: 
    try:
        nota1 = int(input("Digite a nota numero 1:"))
        if not 0 <= nota1 <= 10:
            raise ValueError("Numero invalido, por favor digite um numero de 0 a 10")
        break
    except ValueError as error:
        print(error)

while True:
    try:
        nota2 = int(input("Digite a nota numero 2:"))
        if not 0 <= nota2 <= 10:
            raise ValueError("Numero invalido, por favor digite um numero de 0 a 10")
        break
    except ValueError as error:
        print(error)
        
while True:
    try:
        nota3 = int(input("Digite a nota numero 3:"))
        if not 0 <= nota3 <= 10:
            raise ValueError("Numero invalido, por favor digite um numero de 0 a 10")
        break
    except ValueError as error:
        print(error)
        
while True:
    try:
        nota4 = int(input("Digite a nota numero 4:"))
        if not 0 <= nota4 <= 10:
            raise ValueError("Numero invalido, por favor digite um numero de 0 a 10")
        break
    except ValueError as error:
        print(error)



media = int(nota1+nota2+nota3+nota4)/4



if media >= 6:
   print("Felizmente, o aluno " + aluno + " foi aprovado!")
   print("Média final:")
   print (media)

if media <= 6:
   print("Infelizmente, o aluno " + aluno + " foi reprovado.")
   print("Média final:")
   print (media)








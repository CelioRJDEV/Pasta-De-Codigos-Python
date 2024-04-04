#Programa, ao iniciar gera um valor aleatorio de 1 a 10 e permite que o usuario chute o numero ate que o valor aleatorio gerado seja chutado corretamente.

import random

valor_aleatorio = random.randint(1,10)
acertou = False

while acertou == False:
    chute = int(input("Chute um valor: "))
    if chute > valor_aleatorio:
        print("chute foi maior que o valor gerado")
    elif chute < valor_aleatorio:
        print("chute foi menor que o valor gerado")    
    elif chute == valor_aleatorio:
        acertou == True
        print("voce acertou! ")

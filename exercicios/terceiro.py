"""
1) Faça um algoritmo que imprima os números no intervalo entre 1 e 100:
for i in range(2,100,1):
    print(i)
"""

"""
2) Evolua o algoritmo no qual imprimimos os números num intervalo pré-definido para um algoritmo que pergunte ao usuário qual o intervalo que o mesmo deseja que seja impresso:

inicio=int(input("Insira o inicio do intervalo: "))
fim=int(input("Insira o fim do intervalo: "))
for i in range(inicio+1,fim,1):
    print(i)
"""

"""
3) Faça um algoritmo que imprima os números no intervalo entre 1 e 10 em ordem inversa:

for i in range(9,1,-1):
    print(i)
"""

"""
4) Faça um algoritmo que imprima os números pares entre 0 e 100:

for i in range(100):
    if(i%2==0):
        print(i)
"""

"""
5) Faça um algoritmo que some a quantidade de números pares encontrados no intervalo entre 0 e 100:

soma=0
for i in range(100):
    if(i%2==0):
        soma=soma+i
print("A soma é:",soma)
"""

"""
6) Faça um algoritmo que imprima os números primos entre 0 e 100:

for i in range(100):
    aux=i
    cont=0
    for j in range(1,aux+1,1):
        if(aux%j==0):
            cont+=1
    if(cont==2):
        print(i)
"""

"""
7) Faça um algoritmo que calcule os número primos num intervalo pré-determinado pelo usuário:

inicio=int(input("Insira o inicio do intervalo: "))
fim=int(input("Insira o fim do intervalo: "))
for i in range(inicio+1,fim,1):
    aux=i
    cont=0
    for j in range(1,aux+1,1):
        if(aux%j==0):
            cont+=1
    if(cont==2):
        print(i)
"""

"""
8) Faça um algoritmo que imprima os valores no intervalo definido pelo usuário e permita que o mesmo possa definir 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela:

inicio=int(input("Insira o inicio do intervalo: "))
fim=int(input("Insira o fim do intervalo: "))
num1=int(input("Insira o primeiro número a ser ignorado: "))
num2=int(input("Insira o segundo número a ser ignorado: "))
num3=int(input("Insira o terceiro número a ser ignorado: "))
for i in range(inicio+1,fim,1):
    if(i==num1 or i==num2 or i==num3):
        continue
    print(i)
"""

"""
9) Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra. Caso a letra seja o "q" finalize a aplicação. 
Do contrário, imprima novamente a mesma frase até que o caractere "q" seja enviado:


print("estou em looping")
var=input()
while(var!="q"):
    print("estou em looping")
    var = input()
"""

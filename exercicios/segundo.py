"""
1) Faça um algoritmo que leia um número e mostre se o mesmo é positivo, negativo ou zero.
num=int(input("Insira um número: "))
if(num>0):
    print("O número inserido é positivo.")
elif(num<0):
    print("O número inserido é negativo.")
elif(num==0):
    print("O número inserido é zero.")
"""

#-----#

"""
2) Faça um algoritmo que leia um número e mostre se o mesmo é par ou ímpar.
num=int(input("Insira um número: "))
if(num%2==0):
    print("O número inserido é par.")
else:
    print("O número inserido é impar.")
"""

#-----#

"""
3) Faça um algoritmo que leia dois números e imprima o maior.
num1=float(input("Insira o primeiro número: "))
num2=float(input("Insira o segundo número: "))
if(num1>num2):
    print("O primeiro número inserido é maior.")
else:
    print("O segundo número inserido é maior.")
"""

#-----#

"""
4) Faça um algoritmo que peça a idade de uma pessoa e imprima na tela se a mesma já é maior de idade ou então, se a mesma é de menor.
idade=int(input("Insira sua idade: "))
if(idade>18):
    print("Você é de maior.")
else:
    print("Você não é de maior.")
"""

#-----#

"""
5) Faça um algoritmo que peça a idade do usuário e a idade da sua mãe. Em seguida, imprima na tela com quantos anos sua mãe o teve.
idade=int(input("Insira sua idade: "))
idade_mae=int(input("Insira a idade da sua mãe: "))
print("Sua mae o teve com",idade_mae-idade,"anos")
"""

#-----#

#6) Faça um algoritmo que imprima 50 vezes o caractere "-" na tela (sem a utilização de laços de repetição).
#print("--------------------------------------------------")

"""
#7) Faça um algoritmo que peça um número ao usuário e verifique se o mesmo é par ou então ímpar.
num=int(input("Insira um número: "))
if(num%2==0):
    print("O número inserido é par.")
else:
    print("O número inserido é impar.")
"""

#-----#

"""
8) Faça um algoritmo que peça dois números. Primeiro, imprima o maior e, em seguida, o menor.
num1=float(input("Insira o primeiro número: "))
num2=float(input("Insira o segundo número: "))
if(num1>num2):
    print("O número",num1," é o maior.")
    print()
    print("O número", num2, " é o menor.")
else:
    print("O número",num2," é o maior.")
    print()
    print("O número", num1, " é o menor.")
"""

#-----#


"""
9) Faça um algoritmo que verifica se um determinado valor é um número inteiro.
num1=float(input("Insira um número: "))
if(num1//1==num1):
    print("O número é inteiro")
else:
    print("O número não é inteiro")
    
"""

#-----#

"""
10) Faça um algoritmo que verifica se um determinado valor é uma String.
valor=input("Insira um valor: ")
if(type(valor) is str):
    print("O valor é uma string.")
else:
    print("O valor não é uma string.")
"""

#-----#

"""
11) Faça um algoritmo que verifica se um determinado valor é do tipo decimal.
valor=float(input("Insira um valor: "))
if(valor//1!=valor):
    print("O número é decimal")
else:
    print("O número não é decimal")
"""

#-----#

"""
12) Faça um algoritmo que peça um valor numérico.
Em seguida, verifique se o número é inteiro ou decimal.
valor=float(input("Insira um valor: "))
if(valor//1==valor):
    print("O número é inteiro")
else:
    print("O número é decimal")
"""

#-----#

"""
13) Faça um algoritmo que leia três números e imprima na tela o maior deles.

num1=float(input("Insira o primeiro número: "))
num2=float(input("Insira o segundo número: "))
num3=float(input("Insira o terceiro número: "))
if(num1>num2 and num1>num3):
    print("O número",num1,"é o maior")
elif(num2>num1 and num2>num3):
    print("O número", num2, "é o maior")
elif(num3>num1 and num3>num2):
    print("O número", num3, "é o maior")
"""

#-----#

"""
14) Faça um algoritmo que leia três números e imprima-os em ordem crescente.

num1=float(input("Insira o primeiro número: "))
num2=float(input("Insira o segundo número: "))
num3=float(input("Insira o terceiro número: "))
if(num1>num2):
    if(num2>num3):
        print(num3,"<",num2,"<",num1)
    else:
        if (num3 < num1):
            print(num2, "<", num3, "<", num1)
        else:
            print(num2, "<", num1, "<", num3)
elif(num2>num1):
    if(num1>num3):
        print(num3,"<",num1,"<",num2)
    else:
        if (num3 < num2):
            print(num1, "<", num3, "<", num2)
        else:
            print(num1, "<", num2, "<", num3)
elif(num3>num1):
    if(num1>num2):
        print(num2,"<",num1,"<",num3)
    else:
        if (num2 < num3):
            print(num1, "<", num2, "<", num3)
        else:
            print(num1, "<", num3, "<", num2)
"""

#-----#


"""
15) Faça um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não.

carac=str(input("Insira um caractere: "))
if(carac=="a" or carac=="e" or carac=="i"):
    print("O caractere é uma vogal.")
elif(carac=="o" or carac=="u" or carac=="A"):
    print("O caractere é uma vogal.")
elif(carac=="E" or carac=="I" or carac=="O"):
    print("O caractere é uma vogal.")
elif(carac=="U"):
    print("O caractere é uma vogal.")
else:
    print("O caractere não é uma vogal.")
"""

#-----#


"""
16) Os endereços IP versão 4 são divididos em cinco classes: A, B, C, D e E. Os endereços no intervalo de 0 à 127 são classe A, de 128 a 191 são classe B, de 192 a 223 são classe C, de 224 à 239 são classe D e a partir de 240 são classe E. 
    Faça um algoritmo que leia o primeiro octeto, no formato decimal de um endereço IP, e informe a sua classe.

ip=float(input("Insira o primeiro octeto do endereço de ip: "))
if(0<=ip and ip<=127):
    print("O ip é da classe A.")
if(128<=ip and ip<=191):
    print("O ip é da classe B.")
if(192<=ip and ip<=223):
    print("O ip é da classe C.")
if(224<=ip and ip<=239):
    print("O ip é da classe D.")
if(ip>=240):
    print("O ip é da classe E.")
"""

#-----#


"""
17) Faça um algoritmo que receba um número inteiro, que represente um determinado mês do ano, e mostre o nome do mês correspondente. Por exemplo, se for informado o número 2, o algoritmo deverá exibir: fevereiro. 
    O algoritmo também deve validar se a entrada está correta.

num=int(input("Insira um número: "))
if(num==1):
    print("Janeiro é o mês correspondente.")
if(num==2):
    print("Fevereiro é o mês correspondente.")
if(num==3):
    print("Março é o mês correspondente.")
if(num==4):
    print("Abril é o mês correspondente.")
if(num==5):
    print("Maio é o mês correspondente.")
if(num==6):
    print("Junho é o mês correspondente.")
if(num==7):
    print("Julho é o mês correspondente.")
if(num==8):
    print("Agosto é o mês correspondente.")
if(num==9):
    print("Setembro é o mês correspondente.")
if(num==10):
    print("Outubro é o mês correspondente.")
if(num==11):
    print("Novembro é o mês correspondente.")
if(num==12):
    print("Dezembro é o mês correspondente.")
if(num<=0 or num>=13):
    print("Número inválido.")
"""

#-----#

"""
18) Faça um algoritmo que valide uma data. A mesma deve ser formada por dia, mês e ano. Por exemplo, se o usuário digitar a data 10/8 a mesma será inválida. Porém, caso a data seja 01/10/2018, a mesma deve ser considerada válida.
dia=int(input("Insira o dia: "))
mes=int(input("Insira o mês: "))
ano=int(input("Insira o ano: "))
if(ano%4==0):
    if(mes==2):
        if(dia>=1 and dia<=29):
            print("A data é válida")
        else:
            print("A data é inválida")
else:
    if(mes==1 or mes==3 or mes==5):
        if(dia>=1 and dia<=31):
            print("A data é válida")
        else:
            print("A data é inválida")
    elif(mes==7 or mes==8 or mes==10):
        if (dia >= 1 and dia <= 31):
            print("A data é válida")
        else:
            print("A data é inválida")
    elif(mes==12):
        if (dia >= 1 and dia <= 31):
            print("A data é válida")
        else:
            print("A data é inválida")
    elif(mes==2):
        if (dia >= 1 and dia <= 28):
            print("A data é válida")
        else:
            print("A data é inválida")
    else:
        if(dia >= 1 and dia <= 30):
            print("A data é válida")
        else:
            print("A data é inválida")
"""

#1) Faça um algoritmo que apenas imprima o seu nome na tela e em seguida finalize a aplicação.
#print("Eduardo Correia dos Santos Junior")
#-----#

"""
2) Faça um algoritmo que solicite ao usuário digitar o seu nome e em seguida envie a seguinte frase para a saída padrão:
"O seu nome é: [nome do usuário]".

nome=input("Inisira seu nome: ")
print("O seu nome é %s"%nome)
"""

#-----#

"""
3) Faça um algoritmo que solicite o nome e a idade do usuário e então, envie a seguinte frase para o Console: 
"O seu nome é <nome> e a sua idade é <idade>".

nome=input("Inisira seu nome: ")
idade=input("Insira sua idade: ")
print("O seu nome é",nome,"e a sua idade é",idade)
"""

#-----#

"""
4) Faça um algoritmo que solicite ao usuário informar um número. Em seguida, armazene este número numa variável. 
Por fim, envie esse número para a saída padrão.

num=input("Insira um número: ")
print(num)
"""

#-----#

"""
5) Faça um algoritmo que solicite ao usuário informar um número. Em seguida, escreva a seguinte mensagem: "O número digitado foi: ".

num=int(input("Insira um número: "))
print("O numero digitado foi: %i" %num)
"""

#-----#

"""
6) Faça um algoritmo que solicite ao usuário informar 3 números. 
Em seguida, some-os e envie para a saída padrão a seguinte frase: "A soma total é: "

num=int(input("Insira um número: "))
num2=int(input("Insira um outro número: "))
num3=int(input("Insira mais um número: "))
soma=num+num2+num3
print("A soma total é: %i"%soma)
"""

#-----#

"""
7) Faça um algoritmo que solicite ao usuário informar 2 números. 
Em seguida, some os valores e envie para a saída padrão a seguinte frase: 
"A soma entre <X> e <Y> é igual <total>".

num=int(input("Insira um número: "))
num2=int(input("Insira um outro número: "))
soma=num+num2
print("A soma entre",num,"e",num2,"é: %i"%soma)
"""

#-----#

"""
8) Faça um algoritmo que solicite a nota das 4 provas semestrais do usuário. 
Em seguida, calcule e envie para a saída padrão a média:

nota1=float(input("Insira a primeira nota: "))
nota2=float(input("Insira a segunda nota: "))
nota3=float(input("Insira a terceira nota: "))
nota4=float(input("Insira a quarta nota: "))
media=(nota1+nota2+nota3+nota4)/4
print("A média é: %.2f"%media)
"""

#-----#

"""
9) Faça um algoritmo em que o usuário informe uma medida em metros. 
Em seguida, converta essa medida para centímetros e envie para a saída padrão:

med=float(input("Insira uma medida: "))
med=med*100
print("A medida em centimetros é: %.2f"%med)
"""

#-----#

"""
10) Faça um algoritmo que calcule o cubo e o quadrado de um determinado número:

num=int(input("Insira um número: "))
quad=num*num
cubo=num**3
print("O quadrado de",num,"é",quad,"enquanto seu cubo é",cubo)
"""

#-----#

"""
11) Faça um algoritmo que solicite ao usuário digitar 2 números. 
Em seguida, imprima o total decimal da divisão e o total inteiro (sem casas decimais):

num=float(input("Insira um número: "))
num2=float(input("Insira um outro número: "))
dec=num/num2
div_inteiro=num//num2
print("A divisao decimal entre esses numero é",dec,"e a divisão inteira é %i"%div_inteiro)
"""

#-----#

"""
12) Faça um algoritmo que solicite a largura e a altura de um retângulo. 
Em seguida, imprima para o usuário quantos metros quadrados possui a área total.

wid=float(input("Insira a largura do retângulo: "))
hei=float(input("Insira a altura do retângulo: "))
area=wid*hei
print("A area total desse retângulo é %im²"%area)
"""

#-----#

"""
13) Faça um algoritmo que solicite ao usuário informar uma quantidade de dias, horas, minutos
e segundos. Em seguida, converta tudo para segundos:

dias=int(input("Insira um número de dias: "))
horas=int(input("Insira um número de horas: "))
minutos=int(input("Insira um número de minutos: "))
segundos=int(input("Insira um número de segundos: "))
total=segundos+(minutos*60)+(horas*3600)+(dias*86400)
print("O total em segundos é %i"%total)
"""

#-----#

"""
14) Faça um algoritmo que solicite ao usuário informar o valor de uma compra. 
Em seguida, aplique 10% de desconto e imprima na tela tanto o valor total e também o valor 
com o desconto aplicado.

valor_compra=float(input("Insira o valor de uma compra: "))
valor_desc=valor_compra-(valor_compra*0.1)
print("O valor com 10%% de desconto aplicado é R$%.2f"%valor_desc)
"""

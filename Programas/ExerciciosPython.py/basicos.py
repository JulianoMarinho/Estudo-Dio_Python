# Faça um programa que informe a versão do Python que você está utilizando (OK)
#import sys

#print("Versão do Python")
#print(sys.version)

#print("Informação da Versão instalada")
#print(sys.version_info)

#Faça um programa em linguagem Python que converta metros para centímetros. (OK)

#entrada = float(input("Digite o tamanho da corda: "))

#print(f"Sua corda possui {entrada * 100} centímetros")

#  Faça um programa em Python 
# que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido. (OK)

#inteiro = int(input("Digite um número inteiro: "))
#for n in range(1,11):
#    print(f"{inteiro} * {n} = {inteiro * n}")

#Faça um algoritmo em linguagem Python que receba (OK)
#duas notas e calcule a média aritmética e mostre o resultado.

#nota1 = float(input("Digite a primeira nota: "))
#nota2 = float(input("Digite a segunda nota: "))
#print(f'A média das notas é: {(nota1 + nota2) /2}')

#Escreva um programa que mostre todos os números entre 5 e 100 que (OK)
#são divisíveis por 7, mas não são múltiplos de 5. 
#Os números obtidos devem ser impressos em sequência.

#for n in range(1,101):
#    if(n%7 == 0 and n%5 != 0):
#        print(n, end = ' ')


#Faça um programa que receba um número digitado pelo usuário e calcule a soma de todos os números de 1 até ao 
#número digitado. Por exemplo, se o usuário digitou o número 4, a saída deve ser 10

#numero = int(input("Digite um número inteiro: "))
#soma = 0
#for n in range(1, numero + 1):
#    soma += n
#print(soma)

#Crie um algoritmo que receba um número, conte o número total de dígitos 
#e mostre o resultado.
#Por exemplo, se o número é 2021 , então a saída deve ser 4

#numero = int(input("Digite um número: "))
#cont = 0
#while numero != 0:
#    numero = numero //10
#    cont+=1

#print(cont)


# Faça um programa em linguagem Python, que lê um número n e 
#imprime os n primeiros números da sequência de Fibonacci.
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

n = int(input("Digite o n: "))
primeiroN = 0
segundoN = 1
terceiroN = 0
cont = 0

while cont < n:
    terceiroN = primeiroN + segundoN
    primeiroN = segundoN
    segundoN = terceiroN
    cont+=1
    print(primeiroN, end=' ')





#1 - Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue 
#pedindo até que o usuário informe um valor válido

#nota = int(input("Digite uma nota de 0 a 10: "))

#while (not(0 <= nota <= 10)):
    #nota = int(input("Digite uma nota de 0 a 10: "))

#===============================================================
#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha 
#igual ao nome do usuário, mostrando uma mensagem de erro e voltando a 
#pedir as informações.

#login = input("Digite o seu login: ")
#senha = input("Digite uma senha: ")

#while (senha == login):
    #print("Erro, login e senha iguais!")
    #login = input("Digite o seu login: ")
    #senha = input("Digite uma senha: ")

#================================================================
#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
#T = input()
#nome = input("Digite um nome: ")
#idade = int(input("Digite uma idade: "))
#salario = float(input("Digite seu salário: "))
#sexo = input("Qual seu sexo? (digite m ou f):")
#estado_civil = input("Digite seu estado civil: (s,c,v ou d): ")

#if(len(nome) > 3):
#    print(f'O nome: {nome}, possui {len(nome)} caracteres. (OK)')
#else:
#    print("O nome não possui 3 caracteres!")


#================================================

#T = "RT @TheEllenShow: If only Bradley's arm was longer. Best photo ever. #oscars pic.twitter.com/C9U5NOtGap"

#if(1<= len(T) <= 140):
#  print("TWEET")
#else:
#  print("MUTE")


'''month = int(input())

months_dict = {
  1:'January',
  2:'February',
  3:'March',
  4:'April',
  5:'May',
  6:'June',
  7:'July',
  8:'August',
  9:'September',
  10:'October',
  11:'November',
  12:'December'
}

print(months_dict[month])
'''
cont = 0
quat = int(input('Insira quantas vezes quer repetir: '))

while(cont < quat ):
    a = input('Insira o valor de a: ')
    b = input('Insira o valor de b: ')
  
    if b in a:
        print('encaixa')
   
    
    else:
        print('nao')
    
    cont = cont + 1












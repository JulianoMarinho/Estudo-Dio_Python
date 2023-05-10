curso = " Python "

print (curso.strip()) #remove todos os espaços

print (curso.lstrip()) #remove o espaço da esquerda

print (curso.rstrip()) #remove o espaço da direita

print (curso.center(10, "#")) #Adiciona 10 caracteres, considerando a string passada e completando com # para somar 10 caracteres

print (".".join(curso)) #coloca ponto entre as junções -> P.y.t.h.o.n

#imprimindo variaveis dentro de uma string - Interpolação

nome = "Fulano"
idade = 30
profissao = "Programador" 
linguagem = "Python"

print(f"Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}")

PI = 3.14159

print (f" Valor de PI: {PI: .2f}") #formata as casas decimais

print (f"Valor de PI: {PI:10.2f}") #coloca 10 espaços antes da string

#Fatiamento de Strings

nome2 = "José Augusto das Candinhas"

print(nome2[0]) #imprime o primeiro caracter.

print(nome[0:4]) #imprime o José, pegando o inicio e o fim

print(nome[0:4:2]) #imprime o primeiro nome pulando de 2 em 2

print(nome[:]) #Retorna a string inteira

print(nome[::-1]) #inverte a String

#criando um menu joinha


print(
    '''
    =======================Teste========================

    1 - Depositar
    2 - Sacar
    0 - Sair

    ====================================================
        Obrigado por usar nosso sistema!

    '''


)



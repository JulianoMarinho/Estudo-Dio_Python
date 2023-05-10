cont = 0
quat = int(input('Insira quantas vezes quer repetir: '))


while(cont < quat ):

    numeros = input('Insira o valor de a: ')
    entrada  = input('Insira o valor de b: ')
  
    ultimo_valor = numeros[-len(entrada)::]
    if entrada in ultimo_valor:
        print('encaixa')
    else:
        print('nao encaixa')

    cont = cont + 1
'''
print(numeros.index(entrada))

print(numeros[numeros.index(entrada)])

print(len(numeros))
print(len(entrada))
'''

#print(numeros[-len(entrada)::])

'''

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 3

print(list_numbers.index(element))



if entrada in numeros:
    print(f"Possui a entrada {entrada}")
else:
    print(f'Nao possui')


'''




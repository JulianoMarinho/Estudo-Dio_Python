numeros = [1,30,21,2,9,65,34]
pares = []
pares2 = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

#isso pode ser feito de uma segunda maneira:

pares2 = [numero for numero in numeros if numero % 2 == 0]
#o primeiro item é um retorno, o segundo já é o for anterior com a condição

#elevando os numeros ao quadrado usando a segunda forma

quadrado = [numero ** 2 for numero in numeros]


def sum_list(l):
    sum = 0
    for x in l:
        sum += x
    return sum

#l = [1, 2, 3, 4, 5]
#sum_list(l)

l = list(map(int, input("Enter numbers separated by spaces: ").split()))

#print(sum_list(l))

numeros = []

numeros.append(l)
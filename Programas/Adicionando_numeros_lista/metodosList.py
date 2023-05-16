lista = []
#metodo append - adiciona
lista.append(1)

#metodo clear - limpa a lista

lista.clear()

#metodo copy

lista = [1,"Python",56]

l2 = lista.copy()

print(lista)
print(l2)
print(id(l2), id(lista))

#usando o copy da pra copiar o conteudo 
#de uma lista em outra...

#count, conta quantas vezes um elemento aparece
#dentro de uma lista

lista.count(1)

#extend, da pra juntar 2 listas, passando a outra lista
#ele n elimina os valores duplicados.

listagens = ["python", "js", "c","c"]

print(listagens) 

listagens.extend(["java", "c#"])

print(listagens)

#index, retorna a primeira ocorrencia de determinado item

print(listagens.index("java"))

print(listagens.pop()) #retira o ultimo elemento da lista

#se passar o indice, ele tira o elemento requisitado.
print(listagens.pop(0))

#remove o primeiro elemento correspondente

print(listagens.remove("c"))
print(listagens)

#reverse, coloca a lista ao contrário
listagens.reverse()
print(listagens)

#sort, ordena uma lista

alfabeto = ["a","b","c","e","d","ijk","lm"]

alfabeto.sort()
print(alfabeto)

#da pra definir o método de ordenação também
alfabeto.sort(key=lambda x: len(x))
#da pra passar mais itens para a ordenação, por
#exemplo, ordenando pela qnditade de palavras e 
#revertendo a lista
alfabeto.sort(key=lambda x: len(x), reverse=True)





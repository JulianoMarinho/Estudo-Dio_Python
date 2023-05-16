#conjunto é uma coleção de objetos que possuem elementos únicos
#usa-se o construtor do set

print(set([1,2,3,1,4,3])) #{1,2,3,4}

teste = {1,2,3,4,5,1,2,7}

#da pra usar chaves tbm sem precisar do construtor de set, mas isso na
#declaração dos itens
print(teste)

#se for preciso consumir os valores do set, é necessário transformá-lo 
#em uma lista

numeros = {1,2,3,4}

numeros = list(numeros)

print(numeros[0])

#da pra ler um set usando o for normalmente

itens = {1,2,3,4}

for item in itens:
    print(item)

#mostrando o indice

carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#metodos da classe set

conjunto_a = {1,2}
conjunto_b = {3,4}

#uniao
conjunto_a.union(conjunto_b) #{1,2,3,4}

#intersecao
conjunto_a.intersection(conjunto_b) #{2,3}


#diferenca

conjunto_a.difference(conjunto_b) #{1}

#diferenca simetrica : todos os elementos que nao estao na intersecao

conjunto_a.symmetric_difference(conjunto_b) #{1,4}

#issubset: se um conjunto é subconjunto de outro, entao todos os elementos 
# de a pertencem a b

conjunto_c = {1,2,3}
conjunto_d = {4,1,2,5,6,3}
conjunto_e = {0}
conjunto_c.issubset(conjunto_d) #false
conjunto_d.issubset(conjunto_c) #true

#isdisjoit nao possui intersecao

conjunto_c.isdisjoint(conjunto_d) #false
conjunto_c.isdisjoint(conjunto_e) #true

#metodo add

sorteio = {1,23}

sorteio.add(25) #{1,23,25}

#obs: se passarmos um elemento que já existia, ele vai ser ignorado

#metodo clear lima o set
#copy, gera uma copia do set
#discart, descarta um valor

#pop, retira o primeiro valor.

#remove: tira um valor especifico
#o remove da erro se o elemento n existir, o discart nao da erro

#temos o len, serve para tirar o tamanho do elemento

#da pra usar o operador in para verificar se um numero esta dentro do set

1 in sorteio #true
10 in sorteio #false


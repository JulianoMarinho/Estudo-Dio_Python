#tupla é mais restrita, ela é imutável e a lista mutável

frutas = ("laranja", "pera", "uva",) #boa pratica por uma virgula no final para tuplas

letras = tuple("python") #utilizando o construtor tuple e passando python

numeros = tuple([1,2,3,4])

pais = ("Brasil",)

#acessando elementos da tupla:

frutas[0]

matriz = (
    (1,"a", 2),
    ("b",3, 4),
    (6,5, "c"),
)

matriz[0] #(1,"a",2)
matriz[0][0] #1

#fatiamento start, stop e step

tupla = ("p","y","t","h","o","n",)
tupla[2:]
tupla[:2]
tupla[1:3]
tupla[0:3:2]
tupla[::]
tupla[::-1]

#metodos
#count
#index
#len
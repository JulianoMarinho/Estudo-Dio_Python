a = [1,2,3,4,5,6,7]

#primeiro elemento 
print(f'Primeiro Elemento: {a[0]}')
#ultimo elemento
print(f'Primeiro Elemento: {a[-1]}')
#range na lista [0 até 4] => [0:4] obs.: isso não vai incluir o elemento de
#indice 4, pois começamos do 0
print(f'Range até o 4o elemento: {a[0:4]}')

#mas e se quisermos pegar do 1o até o utimo, podemos fazer assim:
print(f'Range do 1o até o utimo: {a[0:-1]}')

#ué mas o ultimo n era o 6? -Neste caso, se omitirmos o numero apos o : 
#ele vai entender que queremos até o utimo.
print(f'Range do 1o até o utimo: {a[0:]}')

#estranho...

#da pra usarmos dessa forma tbm:
print(f'Range do 1o até o utimo: {a[:]}') #essa é uma forma de copiar listas em python tbm

#da pra estipular uma condição de avanço também, assim:

print(f'Range com avanço: {a[::2]}') #veja que ele vai pulando de 2 em 2 na nossa lista

#este avanço, também funciona ao contrário, essa é uma forma fácil de invertermos uma lista ex.:
print(f'Range com avanço: {a[::-1]}') #isso também funciona com strings



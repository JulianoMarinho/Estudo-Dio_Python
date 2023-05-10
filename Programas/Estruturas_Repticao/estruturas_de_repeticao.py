texto = "Informe um texto"
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

#for else

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ") 
else: 
    print("\ncontinua aqui...") 


#for usando range

for numero in range(0,11):
    print(numero, end=" ")


#exibindo a tabuada do 5

for numero in range(0,51,5):
    print(numero, end=" ")

#while

opcao = -1

while opcao !=0:
    opcao = int(input("[1] Scar \n [2] Extrato \n [0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

#Assim como no for, o else tbm pode ser usado no final do while
MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

if idade>= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")

else:
    print("Menor de idade")


#if aninhado, if dentro de if

#no python o operador ternário é um pouco diferente
#considerando o exemplo (x % 2 == 0) ? "par" : "impar"

x = 10
print ("par" if x % 2 == 0 else "impar")

#ou

saldo = 1000
saque = 50

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
 
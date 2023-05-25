#desafio 1:

numeros = []
C = int(input()) 
for i in range (C):
    print("Mais de 8000!" if int(input()) > 8000 else "Inseto!")

#desafio 2
T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    numero_garrafas = N % K + N / K
    print(int(numero_garrafas))

#desafio 3

a = input() 
b = input() 
c = input() 


animals = {
    "vertebrado" : {
      "ave":{
        "carnivoro": "aguia",
        "onivoro": "pomba"
      },
      "mamifero":{
        "onivoro": "homem",
        "herbivoro": "vaca"
      }
    },
    "invertebrado": {
      "inseto": {
        "hematofago": "pulga",
        "herbivoro": "lagarta"
      },
      "anelideo": {
        "hematofago": "sanguessuga",
        "onivoro": "minhoca"
      }
    }
}
  
print(animals[a][b][c])




  

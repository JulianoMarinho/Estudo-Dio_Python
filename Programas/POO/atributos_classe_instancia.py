class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*obj):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Fulano",1)
aluno_2 = Estudante("Ciclano", 2)

mostrar_valores(aluno_1,aluno_2)

#self define variaveis de instancia; a escola, neste caso, é variavel de classe
Estudante.escola = "Python"
aluno_1.matricula = 3
mostrar_valores(aluno_1, aluno_2)
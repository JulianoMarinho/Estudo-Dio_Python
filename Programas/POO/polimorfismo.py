class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        return super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz nao pode voar")

# FIXME: exemplo ruim do uso de herança para "ganhar" o metodo voar
class Aviao(Passaro):
    def voar(self):
        print("O avião está decolando...")

def plano_voo(obj):
    obj.voar()

#o objeto se comporta de formas diferentes chamando o metodo

p1 = Pardal()
p2 = Avestruz()
p3 = Aviao()

plano_voo(p1)
plano_voo(p2)
plano_voo(p3)
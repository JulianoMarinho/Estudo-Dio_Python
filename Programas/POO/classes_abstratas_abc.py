from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligado!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "LG"

controle = ControleTv()

controle.ligar()
controle.desligar()

controleAc = ControleArCondicionado()
controleAc.ligar()
controleAc.desligar()

print(controleAc.marca)
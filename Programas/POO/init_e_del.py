class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a Classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Removendo a instância da classe...")

    def falar(self):
        print("auau")

def criar_cachorro():
    c = cachorro("zeus", "Branco e preto", false)
    print(c.nome)

criar_cachorro()    
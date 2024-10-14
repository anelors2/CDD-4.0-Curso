class Pessoa:
    def __init__(self,nome:str,peso:float,idade:int):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.falando = False
        self.comendo = False
        self.dormindo = False

    def falar(self):
        self.comendo = False
        self.dormindo = False
        if self.dormindo == False:
            if self.falando == False:
                if self.comendo == False:
                    print(f"{self.nome} foi falar")
                    self.falando = True
                else:
                    print(f"{self.nome} não pode falar pois está comendo.")
            else:
                print(f"{self.nome} não pode falar pois está falando.")
        else:
            print(f"{self.nome} não pode falar pois está dormindo.")
    def dormir(self):
        self.falando = False
        self.comendo = False
        if self.dormindo == False:
            if self.falando == False:
                if self.comendo == False:
                    print(f"{self.nome} foi dormir")
                    self.dormindo = True
                else:
                    print(f"{self.nome} não pode dormir pois está comendo.")
            else:
                print(f"{self.nome} não pode dormir pois está falando.")
        else:
            print(f"{self.nome} não pode dormir pois já está dormindo.")
    def comer(self):
        self.falando=False
        self.dormindo=False
        if self.dormindo == False:
            if self.falando == False:
                if self.comendo == False:
                    print(f"{self.nome} foi comer")
                    self.comendo = True
                else:
                    print(f"{self.nome} não pode comer pois já está comendo.")
            else:
                print(f"{self.nome} não pode comer pois está falando.")
        else:
            print(f"{self.nome} não pode comer pois está dormindo.")

class Animal:
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} foi comer.")

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"O {self.nome} faz MIAAAAAAAUUUUUUUUUUUUU")

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def pular(self):
        print(f"O coelho {self.nome} pula...")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def mugir(self):
        print(f"A vaquinha {self.nome} começou a mugir, MUUUUUUUUUUUUUUUUUU.")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def latir(self):
        print(f"O dog {self.nome} está latindo, Au Au.")

class Atleta:
    def __init__(self,nome,peso,idade):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.aquecimento=False

    def aposentar(self):
        if self.idade >= 60:
            print(f"O atleta {self.nome} está aposentado e não poderá competir.")
        else:
            print(f"O atleta {self.nome} está apto para competir.")

    def aquecer(self):
        print(f"O atleta {self.nome} está aquecido")
        self.aquecimento=True

class Corredor(Atleta):
    def __init__(self,nome,peso,idade):
        super().__init__(nome,peso,idade)
    def correr(self):
        if self.aquecimento==True:
            if self.idade >= 60:
                print(f"O atleta {self.nome} está aposentado e não poderá competir.")
            else:
                print(f"{self.nome} foi correr.")
        else:
            print(f"O atleta {self.nome} precisa aquecer.")

class Nadador(Atleta):
    def __init__(self,nome,peso,idade):
        super().__init__(nome,peso,idade)
    def nadar(self):
        if self.aquecimento == True:
            if self.idade >= 60:
                print(f"O atleta {self.nome} está aposentado e não poderá competir.")
            else:
                print(f"{self.nome} foi nadar.")
        else:
            print(f"O atleta {self.nome} precisa aquecer.")

class Ciclista(Atleta):
    def __init__(self,nome,peso,idade):
        super().__init__(nome,peso,idade)
    def pedalar(self):
        if self.aquecimento == True:
            if self.idade >= 60:
                print(f"O atleta {self.nome} está aposentado e não poderá competir.")
            else:
                print(f"{self.nome} foi pedalar.")
        else:
            print(f"O atleta {self.nome} precisa aquecer.")
class TriAtleta(Corredor ,Nadador ,Ciclista):
    def __init__(self,nome,peso,idade):
        super().__init__(nome,peso,idade)

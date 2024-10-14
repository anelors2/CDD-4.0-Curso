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

from reserva import Reserva

class Restaurante:
    def __init__(self, nome, mesas:int):
        self.nome = nome
        self.mesas_disponiveis = mesas
        self.aberto = False
        self.reservas = []

    def abrir_restaurante(self):    
        self.aberto = True  
        print(f"Bem vindo ao restaurante {self.nome}, no momento estamos aberto.")

    def fechar_restaurante(self):
        self.aberto = False
        print(f"O restaurante {self.nome} se encontra fechado.")

    def contador_de_mesas(self):
        if self.mesas_disponiveis > 0:  
            self.reservas.append(Reserva)
            self.mesas_disponiveis -= 1  
            print(f"Reserva {Reserva.Numero} adicionada com sucesso. Mesas disponíveis: {self.mesas_disponiveis}.")
        else:
            print("Desculpe, não há mesas disponíveis.")  
    

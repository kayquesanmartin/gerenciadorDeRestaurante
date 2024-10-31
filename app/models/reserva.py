from cliente import Cliente

class Reserva(Cliente):
    def __init__(self,Numero,Quantidade_Cadeira,Disponivel=True):
        super().__init__(self.nome,self.idade,self.cpf)
        self.Numero = Numero
        self.Quantidade_Cadeira = Quantidade_Cadeira
        self.Disponivel = Disponivel
        pass

        

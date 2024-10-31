class Menu:
    def __init__(self,preco,descricao):
        self.Lista_Prato = []
        self.preco = preco  
        self.descricao = descricao
        pass
    
    def adicionar_prato(self,prato):
        self.Lista_Prato.append(prato)
        pass

    def remover_prato(self,prato):
        self.Lista_Prato.remove(prato)
        pass            

    def atualizar_prato(self,prato):
        #dps que criar class prato, terminar essa
        pass    
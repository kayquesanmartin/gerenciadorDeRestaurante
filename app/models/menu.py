from prato import Prato
from erros import *

class Menu:
    def __init__(self):
        self.Lista_Prato = []
    
    def adicionar_prato(self,prato):  
        try:
            if not isinstance(prato, Prato):
                raise TypeError("O objeto deve ser uma instância de Prato.")
            if prato in self.Lista_Prato:
                raise PratoJaAdicionadoError("O prato já foi adicionado ao menu.")
            self.Lista_Prato.append(prato)
            print("Prato adicionado com sucesso!")
        except (TypeError, PratoJaAdicionadoError) as e:
            print(f"Erro ao adicionar o prato: {e}")

    def remover_prato(self,prato):
        try:
            if prato in self.Lista_Prato:
                raise PratoNaoEncontradoError("Erro: prato não encontrado na lista.")
            self.Lista_Prato.remove(prato)
            print("Prato removido com sucesso!")
        except PratoNaoEncontradoError as e:
            print(f"Erro ao remover o prato: {e}")           
    
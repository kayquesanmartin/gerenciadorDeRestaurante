class Prato:
    def __init__(self, nome,descricao, preco:float):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def editar_prato(self, novo_nome, nova_descricao, novo_preco:float):
        try:
            if not novo_nome:
                raise ValueError("O nome não pode ser vazio.")
            if not nova_descricao:
                raise ValueError("A descrição não pode ser vazia.")
            if novo_preco == None or novo_preco <= 0:
                raise ValueError("O preço deve ser maior que 0.")
            self.nome = novo_nome
            self.descricao = nova_descricao
            self.preco = novo_preco
            print("Prato atualizado com sucesso!")

        except ValueError as e:
            print(f"Erro ao atualizar o prato: {e}")
  

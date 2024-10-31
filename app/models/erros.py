
#erros do menu tropa
class PratoJaAdicionadoError(Exception):
    """Exceção para indicar que o prato já foi adicionado ao menu."""
    pass

class PratoNaoEncontradoError(Exception):
    """Exceção para indicar que o prato não foi encontrado no menu."""
    pass

class NomeVazioError(Exception):
    """Exceção para indicar que o nome não pode ser vazio."""
    pass

class DescricaoVaziaError(Exception):
    """Exceção para indicar que a descrição não pode ser vazia."""
    pass

class PrecoInvalidoError(Exception):
    """Exceção para indicar que o preço deve ser maior que zero."""
    pass

class TipoInvalidoError(Exception):
    """Exceção para indicar que o objeto não é do tipo esperado."""
    pass


#--------------------------------------------------------------------------

#tem mt erro que nao fiz ainda, fiquei com sono fui mimir amigos
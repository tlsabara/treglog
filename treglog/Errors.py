class TregFileErrors:
    """
    Uma classe destinada para os erros relacionados a arquivos
    """
    class TlogErrorWriteFile(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'Erro na gravação do arquivo: {self.value}.'

    class TlogErrorWriteFileOrForce(Exception):
        # todo Pra que essa classe?
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'Erro na gravação do arquivo: {self.value}. Utilize "force_mode=True" na instancia do objeto'

    class TlogErrorPathNotExistsOrInacessible(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'O caminho de pasta passado esta inacessível ou não existe.\n {self.value}'


class TregDBErrors:
    ...


class TregGeneralErrors:
    """
    Para erros relacionados a utilização do módulo.
    """
    class TlogErrorParameterValue(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'O valor do parâmetro {self.value} esta incorreto.\n  Verifique a documentação em: https://github.com/tlsabara/tlog'

    class TlogErrorInvalidTypeBool(Exception):
        def __init__(self, value, name):
            self.value = value
            self.tipo = name

        def __str__(self):
            return f'O valor do parametro esta incorreto: "{self.value}":: (variavel:{self.tipo}) , não é do tipo "bool".\nVerifique a documentação em -> https://github.com/tlsabara/tlog'

    class TlogErrorIncorrectUtilization(Exception):
        def __init__(self, value, name):
            self.value = value
            self.tipo = name

        def __str__(self):
            return 'O log foi instanciado com o parameto "fullMestype = True", mas não foi informado o parametro "call" na chamada.\nEdite a função ou modifique o parametro na instancia'

    class TlogErrorIncorrectTypeLog(Exception):
        def __init__(self, value):
            self.value

        def __str__(self):
            return f'O tipo do log informado ({self.value}) é incoreto.\nVerifique a documentação em -> https://github.com/tlsabara/tlog'
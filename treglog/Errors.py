from re import S


class TregFileErrors:
    """
    Uma classe destinada para os erros relacionados a arquivos
    """
    class TlogErrorWriteFile(Exception):
        """
        Exceções para casos onde o arquivo não pode ser gravado.
        """
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'Erro na gravação do arquivo: {self.value}.'

    class TlogErrorPathNotExistsOrInacessible(Exception):
        """
        Exceções para casos onde o caminho do arquivo não existe.
        """
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'O caminho de pasta passado esta inacessível ou não existe.\n {self.value}'


class TregDBErrors:
    """
    Classe para erros relacionados a utilização do banco de dados.
    """
    class TlogErrorServerUnrearcheble(Exception):
        """
        Erro para casos onde o servidor não foi encontrado(DNS).
        """
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'{self.value}'

    class TlogErrorInvalidResponse(Exception):
        """
        Erro para casos onde o servidor responde de forma incorreta
        """
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'{self.value}'

    class TlogErrorNoPermited(Exception):
        """
        Erros relacionados a permissão no banco de dados
        """
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'{self.value}'

    class TlogErrorDatabaseNotFound(Exception):
        """
        Erro para casos onde o database não é localizado.
        """
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'{self.value}'

    class TlogErrorTableNotFound(Exception):
        """
        Erro para os casos onde a tabela não foi encontrado no banco de dados acessado.
        """
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'{self.value}'

    class TlogErrorSQLDataTypeWrong(Exception):
        """
        Erros onde o tipo de dado a ser inserido não é permitido pela coluna no banco de dados.
        """
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'{self.value}'

    class TlogErrorServerTimeout(Exception):
        """
        Erros onde o servidor exede o timeout configurado.
        """
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'{self.value}'

class TregGeneralErrors:
    """
    Para erros relacionados a utilização da Lib.
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
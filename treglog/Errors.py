from re import S


class TregException(Exception):
    def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'{self.value}'


class TregFileErrors:
    """
    Uma classe destinada para os erros relacionados a arquivos
    """
    class TlogErrorWriteFile(TregException):
        """
        Exceções para casos onde o arquivo não pode ser gravado.
        """
        pass

    class TlogErrorPathNotExistsOrInacessible(TregException):
        """
        Exceções para casos onde o caminho do arquivo não existe.
        """
        pass


class TregDBErrors:
    """
    Classe para erros relacionados a utilização do banco de dados.
    """
    class TlogErrorServerUnrearcheble(TregException):
        """
        Erro para casos onde o servidor não foi encontrado(DNS).
        """
        pass

    class TlogErrorInvalidResponse(TregException):
        """
        Erro para casos onde o servidor responde de forma incorreta
        """
        pass

    class TlogErrorNoPermited(TregException):
        """
        Erros relacionados a permissão no banco de dados
        """
        pass

    class TlogErrorDatabaseNotFound(TregException):
        """
        Erro para casos onde o database não é localizado.
        """
        pass

    class TlogErrorTableNotFound(TregException):
        """
        Erro para os casos onde a tabela não foi encontrado no banco de dados acessado.
        """
        pass

    class TlogErrorSQLDataTypeWrong(TregException):
        """
        Erros onde o tipo de dado a ser inserido não é permitido pela coluna no banco de dados.
        """
        pass

    class TlogErrorServerTimeout(TregException):
        """
        Erros onde o servidor exede o timeout configurado.
        """
        pass

class TregGeneralErrors:
    """
    Para erros relacionados a utilização da Lib.
    """
    class TlogErrorParameterValue(TregException):
        pass


    class TlogErrorInvalidTypeBool(TregException):
        pass


    class TlogErrorIncorrectUtilization(TregException):
        pass


    class TlogErrorIncorrectTypeLog(TregException):
        pass
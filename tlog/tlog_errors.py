class TlogErrorWriteFile(Exception):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return f'Erro na gravação do arquivo: {self.value}.'
    
class TlogErrorParameterValue(Exception):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return f'O valor do parametro typeLog esta incorreto.\n  Verifique a documentação em: https://github.com/tlsabara/tlog'
    
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
        return f'O log foi instanciado com o parameto "fullMestype = True", mas não foi informado o parametro "call" na chamada.\nEdite a função ou modifique o parametro na instancia'
from .Interfaces import InterfaceTlog, InterfaceTlogCommander
from ..Errors import TregGeneralErrors
from types import FunctionType

def __checker(func: FunctionType) -> None:
    """
    Apenas valida se o parâmetro recebido é do tipo "function"
    """
    if not isinstance(func, function):
        raise TregGeneralErrors.TlogErrorIncorrectUtilization(
            'Este decorador é aplicável apenas em funções.'
        )


def tdebug_decorator(func_to_decorate: FunctionType, tlog_controller: InterfaceTlogCommander, message, call_message:str = '') -> any:
    """
    Destinada a ser usada como um decorador para funções, utilizando apenas os parametros para debug.
    Sofre influencia do metodo de log verbose
    """
    __checker(func_to_decorate)    
    def func_decorated(*args, **kwargs):
        tlog_controller.m_debug(message, call_message)
        return func_to_decorate(*args, **kwargs)

    return func_decorated


def tlog_decorator(func_to_decorate: FunctionType, tlog_controller: InterfaceTlogCommander, message, call_message:str = '') -> any:
    """
    Destinada a ser usada como um decorador para funções, utilizando apenas os parametros para defaut log.
    Sofre influencia do metodo de log verbose.
    """
    __checker(func_to_decorate)
    def func_decorated(*args, **kwargs):
        tlog_controller.m_log(message, call_message)
        return func_to_decorate(*args, **kwargs)

    return func_decorated
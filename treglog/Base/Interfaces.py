from abc import ABC, abstractmethod
from datetime import datetime
from uuid import uuid4, uuid5
from ..Errors import TregGeneralErrors


class InterfaceTlogCommander(ABC):
    """
    Interface para o commander do tLog
    """
    ...

class InterfaceTlog(ABC):
    """
    Interface para os modos de Tlog
    """
    default_msg_full = 'Time: {} - Message: [call: {}] - {}'
    default_msg_simple = 'Time: {} - Message: {}'
    ACCEPTED_MODES = ('d', 's', 'v')  # d=debug/s=simple/v=verbose
    ACCEPTED_KEYWORDS = [
        'mode_log',
        'forced_replace',
        'log_name'
    ]

    def __init__(self, **kwargs) -> None:
        mode_log = kwargs.get('mode_log')
        if not mode_log in self.ACCEPTED_MODES:
            raise TregGeneralErrors.TlogErrorParameterValue(
                f'Parâmetro "mode_log" incorreto.\nSão aceitos apenas os valores: {self.ACCEPTED_MODES}.'
            )
        log_name = kwargs.get('log_name')
        self._id_exec = uuid4()
        self.log_name = 'Tlog' if log_name is None else log_name

    def __str__(self) -> str:
        return f'{self.__class__.__name__} (name = {self.log_name}, id={self._id_exec})'

    def show_log(self, full: bool=False) -> None:
        if self.conf in [0,1,2]:
            if full == True:
                dst_log = self.full_log
            else:
                dst_log = self.buffer_log
            try:
                print(f'|----------------------|')
                for line in dst_log:
                    print(line)
                print('-----| FIM DE LOG |-----')
                print('|----------------------|')
                self.buffer_log.append(self.default_msg_simple.format(datetime.now(), "Executado um print do log"))
                self.save_log()
            except:
                pass  #wtf????????
        else:
            pass  #wtf????????
    
    @property
    @abstractmethod
    def full_log(self) -> [list, dict]:
        pass

    @property
    @abstractmethod
    def buffer_log(self) -> [list, dict]:
        pass

    @abstractmethod
    def m_log(self, mess: str, call: str=''):
        pass

    @abstractmethod
    def m_debug(self, mess: str, call: str = '') -> None:
        pass

    def _treatment_message(self, mess, call):
        if call == '':
            mess = self.default_msg_simple.format(datetime.now(), str(mess))
        else:
            mess = self.default_msg_full.format(datetime.now(), str(call), str(mess))
        return mess

    @abstractmethod
    def save_log(self) -> None:
        pass

from abc import ABC, abstractmethod
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
    defautl_msg_full = 'Time: {} - Message: [call: {}] - {}' 
    default_msg_simple = 'Time: {} - Message: {}'
    ACCEPTED_MODES = ('d', 's', 'v')


    def __init__(self, mode_log='s', forced_replace=False, **kwargs) -> None:
        if not mode_log in self.ACCEPTED_MODES:
            raise TregGeneralErrors.TlogErrorParameterValue(
                f'Parâmetro "mdoe_log" incorreto.\nSão aceitos apenas os valores: {self.ACCEPTED_MODES}.'
            )


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


    @full_log.setter
    def full_log(self, value: any) -> None:
        raise TregGeneralErrors.TlogErrorIncorrectUtilization(
            'O atributo "full_log" não pode receber nenhum valor.'
        )

    @property
    @abstractmethod
    def buffer_log(self) -> [list, dict]:
        pass


    @buffer_log.setter
    def buffer_log(self, value: any) -> None:
        raise TregGeneralErrors.TlogErrorIncorrectUtilization(
            'O atributo "buffer_log" não pode receber nenhum valor.'
        )

    @abstractmethod
    def m_log(self, mess: str, call: str=''):
        pass

    @abstractmethod
    def m_debug(self, mess: str, call: str = '') -> None:
        pass
        
    @abstractmethod
    def _treatmentMess(self, mess, call):
        pass

    @abstractmethod
    def save_log(self) -> None:
        pass

# General Imports
from abc import ABC, abstractmethod
from datetime import datetime
import os
import sqlite3

# Local Imports
from Errors import TregFileErrors, TregGeneralErrors, TregDBErrors


class AbsWorker(ABC):
    def __init__(self, **kwargs):
        filename = kwargs.get('filename')
        path = kwargs.get('path')

        if not path:
            path = ''
        if not filename:
            raise TregGeneralErrors.TlogErrorParameterValue('filename as NoneType')

        self.__path = path
        self.__filename = filename

    @property
    def full_path(self):
        return self.__path + self.__filename

    @abstractmethod
    def input_log(self, message, type_message=0, parent=None):
        # Tipo de mensagem (0 - Info, 1 - Atenção, 2 - Crítico, -1 - Debug)
        ...

    @abstractmethod
    def create_file(self):
        # Criação do arquivo do log, seja .bd ou .txt
        ...

    @abstractmethod
    def read_log(self, **kargs):
        # leitura do arquivo de log. Diferença se é um arquivo txt ou se é um arquivo .bd
        ...

    @staticmethod
    def translate_level(level):
        # Tipo de mensagem (0 - Info, 1 - Atenção, 2 - Crítico, -1 - Debug)
        if level == 0:
            return 'info'
        elif level == 1:
            return 'warning'
        elif level == 2:
            return 'critical'
        elif level == -1:
            return 'debug'
        else:
            raise TregGeneralErrors.TlogErrorIncorrectTypeLog(level)


class TextWorker(AbsWorker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        full_path = str(self.__path) + str(self.__filename)
        self.str_message_simple = 'Time:{} | Message{} | Type:{}\n'
        self.str_message_full = 'Time:{} | Message{} | Type:{} | Call: {}\n'
        self.__first_write = True
        self.__full_message = kwargs.get('full_message')
        if not os.access(full_path, os.W_OK):
            raise TregFileErrors.TlogErrorWriteFile(full_path)

    def input_log(self, message, type_message=0, parent=None):
        if self.__first_write:
            with open(self.full_path, 'w') as log_file:
                log_file.write(f'{"| Log File, by Treglog |":-^50}')
                log_file.write(self.str_message_simple.format(
                    datetime.now(),
                    message,
                    self.translate_level(type_message)))
                log_file.write(f'{"| Final do Log |":-^50}\n')
                log_file.close()
        else:
            with open(self.full_path, 'a+') as log_file:
                log_file.seek(0, os.SEEK_END)
                pos = log_file.tell() - 1
                while pos > 0 and log_file.read(1) != "\n":
                    pos -= 1
                    log_file.seek(pos, os.SEEK_SET)
                if pos > 0:
                    log_file.seek(pos, os.SEEK_SET)
                    log_file.truncate()
                if self.__full_message:
                    log_file.write(
                        self.str_message_simple.format(
                            datetime.now(),
                            message,
                            self.translate_level(type_message)
                        )
                    )
                else:
                    log_file.write(
                        self.str_message_full.format(
                            datetime.now(),
                            message,
                            self.translate_level(type_message),
                            parent
                        )
                    )
                log_file.write(f'{"| Final do Log |":-^50}\n')
                log_file.close()

    def create_file(self):
        try:
            with open(self.full_path, 'w') as file:
                file.close()
        except Exception as e:
            print('Erro Na croicação do arquivo.', e)

    def read_log(self, **kargs):
        try:
            with open(self.full_path, 'r') as file:
                lines = file.readlines()
                file.close()
                return  lines
        except Exception as e:
            print('Erro Na croicação do arquivo.', e)

    class DBWorker(AbsWorker):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.conn = sqlite3.connect(self.full_path)
            self.cursor = self.conn.cursor()

            if kwargs.get('')


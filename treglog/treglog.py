from pathlib import Path
from datetime import datetime
import os
from .Errors import TregFileErrors, TregGeneralErrors, TregDBErrors
from .Base.Interfaces import InterfaceTlog

TLOG_VERSION = '3.0.0'


class TlogFile(InterfaceTlog):
    ACCEPTED_KEYWORDS_TLOG = [
        'path_export',
        'prefix',
        'file_limit_lines'
    ]

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if not k in self.ACCEPTED_KEYWORDS and not k in self.ACCEPTED_KEYWORDS_TLOG:
                raise TregGeneralErrors.TlogErrorParameterValue(
                    f'O parâmetro {k}(valor: {v}) não é aceito'
                )
        super().__init__(**kwargs)

        path_export = kwargs.get('path_export')
        prefix = 'no_prefix'
        limit_lines = 1000
        force_mode = False

        if not path_export:
            Path(str(Path.cwd()), 'log', prefix).mkdir(parents=True, exist_ok=True)
            path_export_file_full = Path(str(Path.cwd()), 'log', prefix)

        elif isinstance(path_export, str):
            Path(str(path_export), 'log', prefix).mkdir(parents=True, exist_ok=True)
            path_export_file_full = Path(str(Path.cwd()), 'log', prefix)
        else:
            raise TregFileErrors.TlogErrorPathNotExistsOrInacessible(
                'Erro na criação do arquivo.'
            )

        id_exec = self.__check_folder(path_export_file_full, prefix)
        start_time = f'id:{id_exec} Start time: {str(datetime.now())}'
        log_time = str(datetime.now())
        prefix_file = prefix + '@' + str(id_exec)
        file_try = prefix + '@' + str(id_exec) + '__' + log_time[:10] + '_' + log_time[11:19].replace(
            ':', '_') + '.txt'

        with open(Path(path_export_file_full, file_try), 'w') as arquivo:
            arquivo.write('---| teste log |---\n')
            arquivo.write('generated with TLOG by sbk v{}\n'.format(TLOG_VERSION))
            arquivo.close()

        self.limit_lines = limit_lines
        self.time = log_time
        self.start_time = start_time
        self.__buffer_log = [self.start_time]
        self.__full_log = list()
        self.prefix = str(prefix_file)
        self.export_file = Path(path_export_file_full, file_try)
        self.conf = kwargs.get('mode_log')
        self.path_export_file_full = path_export_file_full
        self.hist_filelog = []
        self.hist_filelog_size = 0
        self.force_mode = force_mode

    def __check_folder(self, path, prefix):
        alt_list = list()
        for path_in in Path(path).iterdir():
            if path_in.is_file():
                if str(path_in.name)[:len(prefix) + 1] == str(prefix + '@'):
                    alt_list.append(path_in)
        return len(alt_list) + 1

    def _verify_len_log(self):
        if len(self.buffer_log) >= self.limit_lines:
            cl = 0
            for l in self.buffer_log:
                self.__full_log.append(l)
                cl += 1
            self.hist_filelog_size += cl
            self.export_file = self.path_export_file_full + \
                               self.prefix + '__' + \
                               self.time[:10] + '_' + \
                               self.time[11:19].replace(':', '_') + f'_l_{self.hist_filelog_size}.txt'
        else:
            pass

    def _write_file(self):
        with open(str(self.export_file), 'w') as lfile:
            lfile.write('---| ARQUIVO DE LOG |---\n')
            for line in self.buffer_log:
                lfile.write(line)
                lfile.write('\n')
            lfile.write('Ultima execução: {}\n'.format(str(datetime.now())))
            lfile.write('-----| FIM DE LOG |-----\n')
            lfile.close()

    def save_log(self):
        try:
            self._write_file()
            self._verify_len_log()
            return True
        except Exception as e:
            raise e

    @property
    def buffer_log(self):
        return self.__buffer_log

    @property
    def full_log(self):
        return self.__full_log

    def m_debug(self, mess: str, call: str = '') -> None:
        return super().m_debug(mess, call)

    def m_log(self, mess: str, call: str = ''):
        mess = self._treatment_message(mess, call)
        if self.conf == 'd' or self.conf == 's':
            self.__buffer_log.append(mess)
            self.save_log()
        if self.conf == 'v':
            print(mess)
            self.__buffer_log.append(mess)
            self.save_log()

class TlogDB(InterfaceTlog):
    """
    Classe para utilziar o treglog com banco de dados.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def m_debug(self, mess: str, call: str = '') -> None:
        return super().m_debug(mess, call)

    def m_log(self, mess: str, call: str = ''):
        return super().m_log(mess, call)

    @property
    def buffer_log(self):
        return super().buffer_log

    @property
    def full_log(self):
        return super().full_log

    def save_log(self) -> None:
        return super().save_log()

    def _treatment_message(self, mess, call):
        return super()._treatment_message(mess, call)

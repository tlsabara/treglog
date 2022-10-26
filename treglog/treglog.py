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
                print(k)
                raise TregGeneralErrors.TlogErrorParameterValue(
                    f'O parâmetro {k}(valor: {v}) não é aceito'
                )
        super().__init__(**kwargs)
        # rever assinatura
        # path_export_file='', typeLog=0, prefix = 'no_prefix', limit_lines = 1000, force_mode=False
        #rever muito
        #rever muito
        #rever muito
        #rever muito


        path_export = kwargs.get('path_export')
        typeLog=0
        prefix = 'no_prefix'
        limit_lines = 1000
        force_mode=False
        
        id_exec = 1
        
        if not path_export:
            try:
                Path(str(Path.cwd()), 'log', prefix).mkdir(parents=True, exist_ok=True)
                path_export_file_full = Path(str(Path.cwd()), 'log', prefix)
            except Exception as e:
                raise  TregFileErrors.TlogErrorPathNotExistsOrInacessible(
                    'Erro na criação do arquivo.'
                )
        else:
            try:
                Path(str(path_export), 'log', prefix).mkdir(parents=True, exist_ok=True)
            except Exception as e:
                raise  TregFileErrors.TlogErrorPathNotExistsOrInacessible(
                    'Erro na criação do arquivo.'
                )

        alt_list = list()
        for path in os.listdir(path_export_file_full):
                if os.path.isfile(os.path.join(path_export_file_full, path)):
                    if path[:len(prefix)+1] == str(prefix+'@'):
                        p = path[:path.find('__')]
                        if p not in alt_list:
                            alt_list.append(p)

        id_exec += len(alt_list)
        
        while prefix +'@'+ str(id_exec) in alt_list:
            id_exec += 1
        
        if typeLog not in [0,1,2,3]:
            raise TregGeneralErrors.TlogErrorParameterValue(typeLog)
        else:
            start_time = f'id:{id_exec} Start time: {str(datetime.now())}'
            log_time = str(datetime.now())
            prefix_file = prefix +'@'+ str(id_exec)
            path_try = str(path_export_file_full) + prefix_file + '__' + log_time[:10] +'_' + log_time[11:19].replace(':','_') + '.txt'
            try:
                if typeLog == 1 or typeLog == 0:
                    arquivo = open(str(path_try),'w')
                    arquivo.write('---| teste log |---\n')
                    arquivo.write('generated with TLOG by sbk v{}\n'.format(TLOG_VERSION))
                    arquivo.close()
            except FileNotFoundError:
                raise TregFileErrors.TlogErrorWriteFile(path_try)
            else:
                self.limit_lines = limit_lines
                self.time = log_time
                self.Startime = start_time
                self.filelog = [self.Startime]
                self.prefix = str(prefix_file)
                self.exportFile = path_try
                self.conf = typeLog
                self.defMsg_full = 'Hora: {} - Mensagem: [call: {}] - {}' 
                self.defMsg_simple = 'Hora: {} - Mensagem: {}'
                self.nosrc = False
                self.path_export_file_full = path_export_file_full
                self.hist_filelog = []
                self.hist_filelog_size = 0
                self.force_mode = force_mode
                
    def _verify_len_log(self):
        if len(self.filelog) >= self.limit_lines:
            cl = 0 
            for l in self.filelog:
                self.hist_filelog.append(l)
                cl +=1
            self.hist_filelog_size += cl
            self.filelog = [self.Startime]
            self.exportFile = self.path_export_file_full + self.prefix + '__' + self.time[:10] +'_' + self.time[11:19].replace(':','_') + f'_l_{self.hist_filelog_size}.txt'
        else:
            pass
        

    def save_log(self):
        try:
            if self.conf == 1 or self.conf == 0:
                lfile = open(str(self.exportFile),'w')
                lfile.write('---| ARQUIVO DE LOG |---\n')
                for line in self.filelog:
                    lfile.write(line)
                    lfile.write('\n')
                lfile.write('Ultima execução: {}'.format(str(datetime.now())))
                lfile.write('\n')
                lfile.write('-----| FIM DE LOG |-----\n')
                if self.nosrc == True: lfile.write('generated with TLOG by sbk v{}\n'.format(TLOG_VERSION))
                lfile.close()
                self._verify_len_log()
            return True
        except FileNotFoundError:
            if self.force_mode:
                os.makedirs(self.path_export_file_full)
                if self.conf == 1 or self.conf == 0:
                    lfile = open(str(self.exportFile),'w')
                    lfile.write('---| ARQUIVO DE LOG |---\n')
                    for line in self.filelog:
                        lfile.write(line)
                        lfile.write('\n')
                    lfile.write('Ultima execução: {}'.format(str(datetime.now())))
                    lfile.write('\n')               
                    lfile.write('-----| FIM DE LOG |-----\n')
                    if self.nosrc == True: lfile.write('generated with TLOG by sbk v{}\n'.format(TLOG_VERSION))
                    lfile.close()
                    self._verify_len_log()
                return True
            raise TregFileErrors.TlogErrorWriteFileOrForce(self.exportFile)
        except FileExistsError:
            # estranho
            if self.conf == 1 or self.conf == 0:
                lfile = open(str(self.exportFile),'w')
                lfile.write('---| ARQUIVO DE LOG |---\n')
                for line in self.filelog:
                    lfile.write(line)
                    lfile.write('\n')
                lfile.write('Ultima execução: {}'.format(str(datetime.now())))
                lfile.write('\n')
                lfile.write('-----| FIM DE LOG |-----\n')
                if self.nosrc == True: lfile.write('generated with TLOG by sbk v{}\n'.format(TLOG_VERSION))
                lfile.close()
                self._verify_len_log()

    def _treatment_message(self, mess, call):
        return super()._treatment_message(mess, call)

    @property
    def buffer_log(self):
        return super().buffer_log

    @property
    def full_log(self):
        return super().full_log
    
    def m_debug(self, mess: str, call: str = '') -> None:
        return super().m_debug(mess, call)

    def m_log(self, mess: str, call: str = ''):
        return super().m_log(mess, call)


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
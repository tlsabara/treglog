from datetime import datetime
import os

tlog_version = '2.1.0'


class TlogErrorWriteFile(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Erro na gravação do arquivo: {self.value}.'


class TlogErrorWriteFileOrForce(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Erro na gravação do arquivo: {self.value}. Utilize "force_mode=True" na instancia do objeto'


class TlogErrorParameterValue(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'O valor do parametro typeLog esta incorreto.\n  Verifique a documentação em: https://github.com/tlsabara/tlog'


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


class TlogErrorPathNotExistsOrInacessible(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'O caminho de pasta passado esta inacessível ou não existe.\n {self.value}'


class Tlog:
    def __init__(self, path_exportFile='', typeLog=0, prefix='no_prefix', limit_lines=1000, force_mode=False):
        id_exec = 1

        if path_exportFile == '':
            if os.name == 'nt':
                path_exportFile = f'C:\\Users\\{os.getlogin()}\\Documents\logs'
            if os.name == 'posix':
                path_exportFile = f'/home/{os.getlogin()}/Documents/logs'

        if os.name == 'nt':
            try:
                os.makedirs(f'{path_exportFile}\\{prefix}')
            except FileExistsError:
                pass
            except OSError:
                raise TlogErrorPathNotExistsOrInacessible(path_exportFile)
            finally:
                path_exportFile_full = f'{path_exportFile}\\{prefix}\\'
        else:
            try:
                os.makedirs(f'{path_exportFile}/{prefix}')
            except FileExistsError:
                pass
            except OSError:
                raise TlogErrorPathNotExistsOrInacessible(path_exportFile)
            finally:
                path_exportFile_full = f'{path_exportFile}/{prefix}/'

        alt_list = list()
        for path in os.listdir(path_exportFile_full):
            if os.path.isfile(os.path.join(path_exportFile_full, path)):
                if path[:len(prefix) + 1] == str(prefix + '@'):
                    p = path[:path.find('__')]
                    if p not in alt_list:
                        alt_list.append(p)

        id_exec += len(alt_list)

        while prefix + '@' + str(id_exec) in alt_list:
            id_exec += 1

        if typeLog not in [0, 1, 2, 3]:
            raise TlogErrorParameterValue(typeLog)
        else:
            start_time = f'id:{id_exec} Start time: {str(datetime.now())}'
            log_time = str(datetime.now())
            prefix_file = prefix + '@' + str(id_exec)
            path_try = path_exportFile_full + prefix_file + '__' + log_time[:10] + '_' + log_time[11:19].replace(':',
                                                                                                                 '_') + '.txt'
            try:
                if typeLog == 1 or typeLog == 0:
                    arquivo = open(str(path_try), 'w')
                    arquivo.write('---| teste log |---\n')
                    arquivo.write('generated with TLOG by sbk v{}\n'.format(tlog_version))
                    arquivo.close()
            except FileNotFoundError:
                raise TlogErrorWriteFile(path_try)
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
                self.path_exportFile_full = path_exportFile_full
                self.hist_filelog = []
                self.hist_filelog_size = 0
                self.force_mode = force_mode

    def _verify_len_log(self):
        if len(self.filelog) >= self.limit_lines:
            cl = 0
            for l in self.filelog:
                self.hist_filelog.append(l)
                cl += 1
            self.hist_filelog_size += cl
            self.filelog = [self.Startime]
            self.exportFile = self.path_exportFile_full + self.prefix + '__' + self.time[:10] + '_' + self.time[
                                                                                                      11:19].replace(
                ':', '_') + f'_l_{self.hist_filelog_size}.txt'
        else:
            pass

    def msg(self, mess, call=''):
        mess = self._treatmentMess(mess, call)
        if self.conf == 2:
            print(mess)
        else:
            pass

    def mLog(self, mess, call=''):
        mess = self._treatmentMess(mess, call)

        if self.conf >= 0 and self.conf < 2:
            self.filelog.append(mess)
            self.exportlog()
        elif self.conf == 2:
            self.filelog.append(mess)
        else:
            pass

    def mDebug(self, mess, call=''):
        mess = self._treatmentMess(mess, call)

        if self.conf == 0:
            print(mess)
            self.filelog.append(mess)
            self.exportlog()
        elif self.conf == 1:
            self.filelog.append(mess)
            self.exportlog()
        elif self.conf == 2:
            print(mess)
            self.filelog.append(mess)
        else:
            pass

    def printlog(self, full=False):
        if self.conf in [0, 1, 2]:
            if full == True:
                dst_log = self.hist_filelog
            else:
                dst_log = self.filelog
            try:
                print('|----------------------|')
                for line in dst_log:
                    print(line)
                print('-----| FIM DE LOG |-----')
                print('|----------------------|')
                self.filelog.append(self.defMsg_simple.format(datetime.now(), "Executado um print do log"))
                self.exportlog()
            except:
                pass
        else:
            pass

    def exportlog(self):
        try:
            if self.conf == 1 or self.conf == 0:
                lfile = open(str(self.exportFile), 'w')
                lfile.write('---| ARQUIVO DE LOG |---\n')
                for line in self.filelog:
                    lfile.write(line)
                    lfile.write('\n')
                lfile.write('Ultima execução: {}'.format(str(datetime.now())))
                lfile.write('\n')
                lfile.write('-----| FIM DE LOG |-----\n')
                if self.nosrc == True: lfile.write('generated with TLOG by sbk v{}\n'.format(tlog_version))
                lfile.close()
                self._verify_len_log()
            return True
        except FileNotFoundError:
            if self.force_mode:
                os.makedirs(self.path_exportFile_full)
                if self.conf == 1 or self.conf == 0:
                    lfile = open(str(self.exportFile), 'w')
                    lfile.write('---| ARQUIVO DE LOG |---\n')
                    for line in self.filelog:
                        lfile.write(line)
                        lfile.write('\n')
                    lfile.write('Ultima execução: {}'.format(str(datetime.now())))
                    lfile.write('\n')
                    lfile.write('-----| FIM DE LOG |-----\n')
                    if self.nosrc == True: lfile.write('generated with TLOG by sbk v{}\n'.format(tlog_version))
                    lfile.close()
                    self._verify_len_log()
                return True
            raise TlogErrorWriteFileOrForce(self.exportFile)
        except FileExistsError:
            # estranho
            if self.conf == 1 or self.conf == 0:
                lfile = open(str(self.exportFile), 'w')
                lfile.write('---| ARQUIVO DE LOG |---\n')
                for line in self.filelog:
                    lfile.write(line)
                    lfile.write('\n')
                lfile.write('Ultima execução: {}'.format(str(datetime.now())))
                lfile.write('\n')
                lfile.write('-----| FIM DE LOG |-----\n')
                if self.nosrc == True: lfile.write('generated with TLOG by sbk v{}\n'.format(tlog_version))
                lfile.close()
                self._verify_len_log()

    def _treatmentMess(self, mess, call):
        if call == '':
            mess = self.defMsg_simple.format(datetime.now(), str(mess))
        else:
            mess = self.defMsg_full.format(datetime.now(), str(call), str(mess))
        return mess

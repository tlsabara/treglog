from datetime import datetime
import tlog_errors

tlog_version = '1.2'

class Treglog:
    def __init__(self, path_exportFile: str, typeLog: int, credits = True, prefix = ''):
        if typeLog not in [0,1,2,3] or type(credits) !=  bool:
            if type(credits) !=  bool:
                raise tlog_errors.TlogErrorInvalidTypeBool(credits, 'credits')
            else:
                raise tlog_errors.TlogErrorParameterValue(typeLog)
        else:
            start_time = 'Start time: {}'.format(str(datetime.now()))
            log_time = str(datetime.now())
            path_try = path_exportFile +'\\'+ prefix + '-' + log_time[:10] +'-' + log_time[11:19].replace(':','-') + '.txt'
            try:
                if typeLog == 1 or typeLog == 0:
                    arquivo = open(str(path_try),'w')
                    arquivo.write('---| teste log |---\n')
                    arquivo.write('generated with TLOG by sbk v{}\n'.format(tlog_version))
                    arquivo.close()
            except FileNotFoundError:
                raise tlog_errors.TlogErrorWriteFile(path_try)
            else:
                self.time = log_time
                self.Startime = start_time
                self.filelog = [self.Startime]
                self.prefix = str(prefix)
                self.exportFile = path_exportFile +'\\'+ self.prefix + '-' + self.time[:10] +'-' + self.time[11:19].replace(':','-') + '.txt'
                self.conf = typeLog
                self.defMsg_full = 'Call: {} - Hora: {} - Mensagem: {}' 
                self.defMsg_simple = 'Hora: {} - Mensagem: {}'
                self.nosrc = credits
            
    def msg(self, mess, call=''):
        mess = self._treatmentMess(mess, call)
        if self.conf == 2 :
            print(mess)
        else:
            pass

    def mLog(self, mess, call = ''):
        mess = self._treatmentMess(mess, call)
            
        if self.conf >= 0 and self.conf < 2 :
            self.filelog.append(mess)
            self.exportlog()
        elif self.conf == 2: 
            self.filelog.append(mess)
        else:
            pass

    def mDebug(self, mess, call = ''):
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
            
    def printlog(self):
        if self.conf in [0,1,2]:
            try:
                print('|----------------------|')
                for line in self.filelog:
                    print(line)
                print('-----| FIM DE LOG |-----')
                print('|----------------------|')
                self.filelog.append(self.defMsg_simple.format(datetime.now(), " - Executado um print do log - "))
                self.exportlog()
            except:
                pass
        else:
            pass

    def exportlog(self):
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
                if self.nosrc == True: lfile.write('generated with TLOG by sbk v{}\n'.format(tlog_version))
                lfile.close()
            return True
        except:
            raise tlog_errors.TlogErrorWriteFile(self.exportFile)

        
    def _treatmentMess(self, mess, call):
        if call == '':
            mess = self.defMsg_simple.format(datetime.now(), str(mess))
        else:
            mess = self.defMsg_full.format(str(call), datetime.now(), str(mess) )
        return mess
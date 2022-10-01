from datetime import datetime
import warnings

# Método tlog
# Para a gestão de um log eficiente
# Exportação do log

#Criado por Thiago Sabará
#Data de Criação: 18/02/2022
#v 1.0 - 18/02/2022
#v 1.1 - 19/02/2022

tlog_version = '1.1'

#função para testar a escrita do arquivo no momento da instanciação do objeto
def letsTry(path_try, lvLog):
        try:
            if lvLog == 1 or lvLog == 0:
                print('Arquivo de log: {}'.format(path_try))
                arquivo = open(str(path_try),'w')
                arquivo.write('---| teste log |---\n')
                arquivo.write('generated with TLOG by sbk v{}\n'.format(tlog_version))
                arquivo.close()
                return str(path_try)
            else:
                return 'Não foi gerado log.'
        except:
            warnings.warn('Erro no arquivo de escrita')
            #preciso fazer encerrar o programa aqui

#método para salvar o arquivo de log
def exportlog(ctrl, dstFile, content):
        #metodo de exportação do arquivo
        if ctrl == 1 or ctrl == 0:
            lfile = open(str(dstFile),'w')
            lfile.write('---| ARQUIVO DE LOG |---\n')
            for line in content:
                lfile.write(line)
                lfile.write('\n')
            lfile.write('Ultima execução: {}'.format(str(datetime.now())))
            lfile.write('\n')
            lfile.write('-----| FIM DE LOG |-----\n')
            lfile.write('generated with TLOG by sbk v{}\n'.format(tlog_version))
            lfile.close()
            
class startLog:
    def __init__(self, path_exportFile, typeLog):
        self.time = str(datetime.now())
        self.Startime = 'Start time: {}'.format(str(datetime.now()))
        self.filelog = [self.Startime]
        self.exportFile = letsTry(path_exportFile +'\\'+ self.time[:10] +'-' + self.time[11:19].replace(':','-') + '.txt',typeLog)
        self.conf = typeLog
        self.defMsg = 'Registro: {} - Mensagem: {}'
        #preciso criar um modo de printar o nome do modulo/classe que deu erro
            
    def msgLog(self, mess):
        mess = str(mess)
        #Apenas dou um print na mensagem sem armazenar em log
        if self.conf >= 0 and self.conf < 3:
            print(mess)
        elif self.conf == 3:
            #Modo slient
            pass
        else:
            #parametro com valor inválido
            warnings.warn('"msgLog()": parâmetro de tipo de log errado!')
            pass

    def onLog(self, mess):
        mess = str(mess)
        #com esta função eu apenas mando para o arquivo de log, sem printar mesmo em modos visuais
        #Apenas envio a mensagem para o vetor do log
        if self.conf >= 0 and self.conf < 2 :
            self.filelog.append(self.defMsg.format(datetime.now(), mess))
            exportlog(self.conf, self.exportFile, self.filelog)
        elif self.conf == 2: #modo 2 não envia para o aquivo de log
            self.filelog.append(self.defMsg.format(datetime.now(), mess))
            warnings.warn('A função esta sendo chamada sem o nível de log (nv: 0 ou 1).')
        elif self.conf == 3:
            #Modo slient
            pass
        else:
            #parametro com valor inválido
            warnings.warn('"onLog()": parâmetro de tipo de log errado!')
            pass

    def mdebug(self, mess):
        mess = str(mess)
        #com esta função eu posso ativar e desativar o log, mas se ativo com o  nv 1 ou maior irá exibir um print
        #print envio da mensagem para o vetor do log
        if self.conf == 0: #visual e no arquivo
            log_line = self.defMsg.format(datetime.now(), mess)
            print(log_line)
            self.filelog.append(log_line)
            exportlog(self.conf, self.exportFile, self.filelog)
        elif self.conf == 1: #apenas no arquivo
            log_line = self.defMsg.format(datetime.now(), mess)
            self.filelog.append(log_line)
            exportlog(self.conf, self.exportFile, self.filelog)
        elif self.conf == 2: #apenas visual
            log_line = self.defMsg.format(datetime.now(), mess)
            print(log_line)
            self.filelog.append(log_line)
        elif self.conf == 3:
            #Modo slient
            pass
        else:
            #parametro com valor inválido
            warnings.warn('"mdebug()": parâmetro de tipo de log errado!')
            pass
            
    def printlog(self):
        #metodo de print em tela de todo o log armazenado no buffer
        if self.conf in [0,1,2]:
            try:
                print('|----------------------|')
                for line in self.filelog:
                    print(line)
                print('-----| FIM DE LOG |-----')
                print('|----------------------|')
                self.filelog.append(self.defMsg.format(datetime.now(), " - Executado um print do log - "))
                exportlog(self.conf,self.exportFile, self.filelog)
            except:
                pass
        elif self.conf == 3:
            #Modo slient
            pass
        else:
            #parametro com valor inválido
            warnings.warn('"printlog()": parâmetro de tipo de log errado!')

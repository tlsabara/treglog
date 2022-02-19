from datetime import datetime
import warnings
# Método tlog
# Para a gestão de um log eficiente
# Exportação do log

#Criado por Thiago Sabará
#Data de Criação: 18/02/2022
#v 1.0


def letsTry(path_try):
        try:
            print(path_try)
            arquivo = open(str(path_try),'w')
            arquivo.write('---| teste log |---')
            arquivo.close()
            return str(path_try)
        except:
            warnings.warn('Erro no arquivo de escrita')
            #preciso fazer encerrar o programa aqui

def exportlog(controle, dstFile, conteudo):
        #metodo de exportação do arquivo
        if controle == 1:
            arquivo = open(str(dstFile),'w')
            arquivo.write('---| ARQUIVO DE LOG |---\n')
            arquivo.write('Inicialização do Log: {}'.format(conteudo[0]))
            arquivo.write('\n')
            for line in conteudo:
                arquivo.write(line)
                arquivo.write('\n')
            arquivo.write('-----| FIM DE LOG |-----\n')
            arquivo.write('|----------------------|\n')
            arquivo.close()
            
class startLog:
    def __init__(self, path_exportFile, aciveLog):
        self.filelog = []
        self.exportFile = letsTry(path_exportFile + str(datetime.now())[:10] +'-' + str(datetime.now())[11:19].replace(':','-') + '.txt')
        self.conf = aciveLog
        self.defMsg = 'Registro: {} - Mensagem: {}'
            
    def msgLog(self, mess):
        #Apenas dou um print na mensagem sem armazenar em log
        if self.conf == 1:
            print(mess)
        else:
            pass

    def debug(self, mess):
        #Apenas envio a mensagem para o vetor do log
        if self.conf == 1:
            self.filelog.append(self.defMsg.format(datetime.now(), mess))
            exportlog(self.conf, self.exportFile, self.filelog)
        else:
            pass

    def mdebug(self, mess):
        #print envio da mensagem para o vetor do log
        if self.conf == 1:
            log_line = self.defMsg.format(datetime.now(), mess)
            print(log_line)
            self.filelog.append(log_line)
            exportlog(self.conf, self.exportFile, self.filelog)
        else:
            pass
            
    def printlog(self):
        #metodo de print em tela de todo o log armazenado3
        if self.conf == 1:
            print('|----------------------|')
            print('---| ARQUIVO DE LOG |---')
            for line in self.filelog:
                print(line)
            print('-----| FIM DE LOG |-----')
            print('|----------------------|')
            self.filelog.append(self.defMsg.format(datetime.now(), " - Executado um print do log - "))
            exportlog(self.conf,self.exportFile, self.filelog)
        else:
            pass

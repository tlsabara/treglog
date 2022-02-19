# tlog
 Minha biblioteca para controle de log pessoal

## Meta
Uma forma de controle dos logs sem ter de reeescrever ou sair dando print para entende o que está acontecendo com o código, com apenas uma varável é póssível printar ou não a tela. Conforme a necessidade. As varáveis e print ficam ocultos e somente são ativados se necessário. Além de exportar um arquivo de log pela timestamp.

## Utilização
#### **Importação:**
~~~python
# modelo de importação
from tlog import startLog
#ou
import tlog
~~~

#### **Inicialização:**
~~~python
caminho = 'C:\\Pasta_de_log'
tipoLog = 0
myLog = startLog(caminho,tipoLog)
#ou
myLog = tlog.startLog(caminho,tipoLog) 
#Dependendo do modo como foi realizada a importação
~~~

#### **Parâmetros:**
~~~python
tlog.startLog(path_exportFile, typeLog)
~~~
* **path_exportFile:** Caminho da pasta onde o arquivo deve ser salvo
* **typeLog:** Tipo de log a ser utilizado no código
    * **0** - Log completo, dependendo do método ocorre print em tela e impressão no arquivo
    * **1** - Log separado, dependendo do método ocorre o print ou a impressão no arquivo
    * **2** - Log visual, ocorre apenas a impressão em tela, ref ao método.
    * **3** - Silient Mode, não imprime no arquivo nem print em tela.


#### **Funções:**
* **onLog(self, mess)**
        
    Código:
    ~~~python
    def onLog(self, mess):
        mess = str(mess)
        if self.conf >= 0 and self.conf < 2 :
            self.filelog.append(self.defMsg.format(datetime.now(), mess))
            exportlog(self.conf, self.exportFile, self.filelog)
        elif self.conf == 2:
            self.filelog.append(self.defMsg.format(datetime.now(), mess))
            warnings.warn('A função esta sendo chamada sem o nível de log (nv: 0 ou 1).')
        elif self.conf == 3:
            pass
        else:
            warnings.warn('"onLog()": parâmetro de tipo de log errado!')
            pass
    ~~~

    Utilização:
    ~~~python
    #Instanciado tlog no objeto myLog:
    myLog.onLog('Esta mensagem não foi printada na tela mas veio para o arquivo')
    ~~~

* **mdebug(self, mess)**
        
    Código:
    ~~~python
    def mdebug(self, mess):
        mess = str(mess)
        if self.conf == 0:
            log_line = self.defMsg.format(datetime.now(), mess)
            print(log_line)
            self.filelog.append(log_line)
            exportlog(self.conf, self.exportFile, self.filelog)
        elif self.conf == 1: 
            log_line = self.defMsg.format(datetime.now(), mess)
            self.filelog.append(log_line)
            exportlog(self.conf, self.exportFile, self.filelog)
        elif self.conf == 2:
            log_line = self.defMsg.format(datetime.now(), mess)
            print(log_line)
            self.filelog.append(log_line)
        elif self.conf == 3:
            pass
        else:
            warnings.warn('"mdebug()": parâmetro de tipo de log errado!')
            pass
    ~~~

    Utilização:
    ~~~python
    #Instanciado o tlog no objeto myLog:
    myLog.mdebug('Esta mensagem é printada na tela e armazanada para o arquivo de log')
    ~~~

* **msgLog(self, mess)**
        
    Código:
    ~~~python
    def msgLog(self, mess):
        mess = str(mess)
        if self.conf >= 0 and self.conf < 3:
            print(mess)
        elif self.conf == 3:
            pass
        else:
            warnings.warn('"msgLog()": parâmetro de tipo de log errado!')
            pass
    ~~~

    Utilização:
    ~~~python
    #Instanciado o tlog no objeto myLog:
    myLog.msgLog('Mensagem printada na tela, mas não vai para o arquivo')
    ~~~

* **printlog(self)**
        
    Código:
    ~~~python
    def printlog(self):
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
            pass
        else:
            warnings.warn('"printlog()": parâmetro de tipo de log errado!')
    ~~~

    Utilização:
    ~~~python
    #Instanciado tlog no objeto myLog:
    myLog.printlog()
    ~~~

--
#### **Versões**
* **1.0** - Inicial
* **1.1** - Modificações no fluxo, melhoria de tratamento e retorno ao usuário, criação do modo slient(nv 3)
* **Proxima versções:**
    * Quebra dos fluxos em casos de erros
    * Tratamento de erros
    * Criação de um nivel 2 para os logs.

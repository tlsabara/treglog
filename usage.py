from datetime import datetime
import tlog

caminho = 'C:\\Users\\root_main\\Documents\\'
myLog = tlog.startLog(caminho,1)
myLog.msgLog('Mensagem printada na tela, mas não vai para o arquivo')
myLog.debug('Esta mensagem não foi printada na tela mas veio para o arquivo')
myLog.mdebug('Esta mensagem é printada na tela e armazanada para o arquivo de log')

myLog.printlog()





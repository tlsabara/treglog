from datetime import datetime
# modelo de importação
from tlog import startLog

#Caminho da pasta, lembrando que cada execução gera um aqrquivo
caminho = 'C:\\Users\\root_main\\Documents\\logs\\log_tlog_homolog'
tipoLog = 0

#meu objeto no script será o myLog mas o nome pode ser qualquer um
#o primeiro parâmetro é o caminho
#o segundo parametro é o tipo de log (0, 1 , 2 OU 3) todas as funções/métodos são sensíveis a ele, mais informações no README.md
myLog = startLog(caminho,tipoLog)
print('inciei')

#método msgLog, apenas printa a mensagem na tela
myLog.msgLog('Mensagem printada na tela, mas não vai para o arquivo')
print('msglog')

#método mlog, apenas registra no arquivo
myLog.onLog('Esta mensagem não foi printada na tela mas veio para o arquivo')
print('mlog')

#método mdebug, printa na tela e armazena no buffer do arquivo de log
myLog.mdebug('Esta mensagem é printada na tela e armazanada para o arquivo de log')
print('mdebug')

#printLog, printa todo o buffer de log em tela, sem imprimir no arquivo, adiciona um registro ao log
myLog.printlog()
print('print log simples')


#print iterativo para demonstrar aque o salvamento do arquivo é do buffer a cada chamadas de função
#em tela teremos inumeras demonstação do log, incluindo cada linha da nova chamada deprint
i = 0 
while i < 1000000:
    a = i % 150000
    if a == 0:
        myLog.onLog(i)
        myLog.printlog()
        print('print Log da interação')
    i = i+1
    
#fim da execução
print('Executei')




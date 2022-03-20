
# ~~Tlog~~ Treglog 

Uma bilbioteca de python simples que antes se chamava tlog agora chama-se treglog, leve para gerar arquivos de log em txt. 

> Autor: Esta é minha primeira bilbioteca, desde já peço desculpas por qualquer erro, ou algo que não foi constuido seguindo as melhores praticas ou convenções. PR/Issues são extremamente bem vindas! Ex: Como lidar com arquivos enormes?

## Meta

Uma forma de controle dos logs sem ter de reeescrever ou sair dando print para entender o que está acontecendo com o código, com apenas uma varável é póssível printar ou não na tela. Conforme a necessidade do dev. As varáveis e prints ficam ocultos e somente são ativados se necessário. Além de exportar um arquivo de log com a timestamp.
  

## Utilização

#### **Instalação:**

~~~python

# modelo de instalação
pip install treglog

~~~

#### **Importação:**
~~~python

# modelo de importação
from treglog import Treglog
#ou
import treglog 

~~~
#### **Inicialização:**
~~~python

caminho =  'C:\\Pasta_de_log'
tipoLog =  0
log = Treglog(caminho,tipoLog)
#ou
log = treglog.Treglog(caminho,tipoLog)
#Dependendo do modo como foi realizada a importação

~~~

  

#### **Parâmetros:**

~~~python

treglog.Treglog(path_exportFile: str, typeLog: int, prefix  =  '')

~~~

*  **path_exportFile:** Caminho da pasta onde o arquivo deve ser salvo

*  **typeLog:** Tipo de log a ser utilizado no código
    *  **0** - Log completo, dependendo do método ocorre print em tela e impressão no arquivo
    *  **1** - Log separado, dependendo do método ocorre o print ou a impressão no arquivo
    *  **2** - Log visual, ocorre apenas a impressão em tela, ref ao método.
    *  **3** - Silient Mode, não imprime no arquivo nem print em tela.
* **prefix:** Prefixo para o nome do arquivo de log.


#### **Funções:**

*  **msg(mess, *call = ''*)**
* Utilizada apenas para printar em tela a mensagem. Pensada para ser utilizada em debugs. Não é registrada no arquivo de log em nenhum modo.

Utilização:
~~~python

destPath  =  'C:\\Users\\root_main\\Documents\\logs\\log_tlog_homolog'
logtype  =  3
log  = Treglog(destPath, logtype, prefix= f'TESTv1-2-Tlog_LOG={logtype}')
#Com a variável call
log.msg(f'Mensagem de erro no log tipo = {logtype}, visivel somente no tipo 2','Com o Nome do método especificado')
#Sem a variável call
log.msg(f'Mensagem de erro no log tipo = {logtype}, visivel somente no tipo 2')

~~~

  

* **mDebug(mess, *call  =  ''*)**
* pensada totalmente para o debug, este método é altamente influenciado pelo parametro **typeLog**.
* Utilização:
~~~python

#Instanciado o tlog no objeto log:
#Com a variável call
log.mDebug(f'Mensagem do mLog no log tipo = {logtype}','Com nome do método')
#Sem a variável call
log.mDebug(f'Mensagem do mLog no log tipo = {logtype}',) 

~~~

  

* **mLog(mess, *call  =  ''*)**
* Nunca printa em tela. Envia apenas para o arquivo. Para ver os registros realizados com desta função em tela, somente utilizando a função **printlog()**.
Utilização:
~~~python

#Instanciado o tlog no objeto log:
#Com a variável call
log.mLog(f'Mensagem do mLog no log tipo = {logtype}','Com nome do método')
#Sem a variável call
log.mLog(f'Mensagem do mLog no log tipo = {logtype}',) )

~~~

  

*  **printlog()**
*  parte destinada a printar em tela o log dos arquivos

Utilização:

~~~python

#Instanciado o tlog no objeto log:
log.printlog()

~~~

  

--

#### **Versões**

*  **1.0.0** - Inicial
*  **1.1.0** - Modificações no fluxo, melhoria de tratamento e retorno ao usuário, criação do modo slient(nv 3)
*  **2.0.0** - Criação do pacote PyPI, Primeiro pacote (13/03/2022)
*  **2.0.1** a **2.0.5** - Correção de bugs
*  **2.0.6** - modificação completa, tratamento de erros ETC, primeira versão completa.

*  **Proxima versções:**

* Tratamento de arquivos grandes. (concorrencia talvez? (kkkkk))
* Quebra em arquivos por dia. (O que ja soluciona parte do problema de arquivos grandes)

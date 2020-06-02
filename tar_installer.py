#!/usr/bin/env python
import os
import sys
'''
Script feito para automatizar a instalação de programas 
compactados em alguma variante de .tar
Compatível com 
Falta terminar...
'''
def limpa_terminal():
    system = os.uname().sysname
    if(system.lower() == "linux"):
        os.system('clear')
    else:
        os.system('cls')
		
limpa = input("Limpar conteúdo anterior da tela [S/N]? ")
if (limpa.lower() == 's'):
    limpa_terminal()
else:
	pass

try:
    arq = sys.argv[1].split('.') 	#Se houver erro aqui, arg[1] inexistente, não foi informado arquivo para descompactação
except:
    print('Não foi informado arquivo nenhum arquivo')
    sys.exit()

tipos = ['bz2', 'rar', 'tar', 'tar.bz2', 'tar.gz', 'tar.xz', 'zip']  #talvez possa ser procura na lista, ideia futura
	
if(arq[len(arq)-1] == 'rar'):
    os.system('unrar x ' + arq) 		# Arquivo .rar
elif(arq[len(arq)-1] == 'tar'):
    os.system('tar -xvf ' + arq)		# Arquivo .tar
elif(arq[len(arq)-1] == 'bz2'):
	if(arq[len(arq)-2] == 'tar'):
    	os.system('tar -jxvf ' + arq)		# Arquivo .tar.bz2
	else:
		print("modelo " + sys.argv[1] + "ainda não suportado")
elif(arq[len(arq)-1] == 'xz'):
	if(arq[len(arq)-2] == 'tar'):
    	os.system('tar -Jxxvf ' + arq)		# Arquivo .tar.xz
	else:
		print("modelo " + sys.argv[1] + "ainda não suportado")    
elif(arq[len(arq)-1] == 'gz'):
	if(arq[len(arq)-2] == 'tar'):
    	os.system('tar -zxvf ' + arq)		# Arquivo .tar.gz
	else:
		print("modelo " + sys.argv[1] + "ainda não suportado")
elif(arq[len(arq)-1] == 'zip'):
	os.system('unzip ' + arq)		# Arquivo .zip
else:
	print('O arquivo não se enquadra nos parâmetros de descompactação')

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
    os.system('unrar x ' + arq)
elif(arq[len(arq)-1] == 'tar'):
    os.system('tar -xvf ' + arq)
elif(arq[len(arq)-1] == 'bz2'):			# ressalva futura
	if(arq[len(arq)-2] == 'tar'):
    	os.system('tar -jxvf ' + arq)
	else:
		print("modelo " + sys.argv[1] + "ainda não suportado")
elif(arq[len(arq)-1] == 'xz'):
    os.system('tar -Jxxvf ' + arq)
elif(arq[len(arq)-1] == 'gz'):
    os.system('tar -zxvf ' + arq)
elif(arq[len(arq)-1] == 'zip'):
	os.system('unzip ' + arq)
else:
	print('Não se enquadra nos parâmetros de descompactação')

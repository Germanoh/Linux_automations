#!/usr/bin/env python
import os
import sys
'''
Script feito para automatizar a instalação de programas 
compactados em alguma variante de .tar
Falta terminar...
'''
try:
    arq = sys.argv[1].split('.')
    print('linha 12')
except:
    print('Não foi informado arquivo nenhum arquivo')
    sys.exit()

if arq[len(arq)-1] == 'tar':
    print('Arquivo .tar incompleto, sem especificação .gz ou .bz2 ou .xz')
    sys.exit()

if(arq[len(arq)-1] == 'bz2'):
    os.system('tar -jxvf ' + arq)
elif(arq[len(arq)-1] == 'xz'):
    os.system('tar -Jxxvf ' + arq)
elif(arq[len(arq)-1] == 'gz'):
    os.system('tar -zxvf ' + arq)
else:
	print('Não é um arquivo formato .tar para instalação')

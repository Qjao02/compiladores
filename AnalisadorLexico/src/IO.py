# -*- coding: utf-8 -*-

import easygui
import sys
from PyQt5.QtGui import *


class IO:
    bufferCodigo = ""
    arc = ''
    bufferTabelaTokens = ''
    numeroAtualDaLinha = 1

    def __init__(self):
        while True:
            if self.read() == 1:
                break
            else:
                self.expectionIOErrorMenssage()
       
    def getNextChar(self):
        c = self.arc.read(1)
        if not c:
            print("End of file")
        if c == '\n':
            self.numeroAtualDaLinha = self.numeroAtualDaLinha + 1
        return c

    def read(self):
        #easygui.msgbox('O arquivo de entrada foi montado a partir de um txt que é a cópia do código presente na especificação do trabalho. Selecione o arquivo entrada.txt e posteriormente o arquivo tabelaToken.txt e por útimo selecione o diretorio destino para que a saída do possa ser armazenada', 'IMPORTANTE')
        pathToEntrada = '../entrada/entrada.txt'
        try:
           
            self.arc = open(pathToEntrada, "r")
            self.arc = open(pathToEntrada,"rU")
            return  1
        except:
            return 0


    def generateOutputFile(self):
        #easygui.msgbox('selecione o diretorio do arquivo de saida', 'IMPORTANTE')
        pathOutput ='../saida.json'
        return open(pathOutput,'w')

    def expectionIOErrorMenssage(self):
        #easygui.msgbox('O arquivo entrada.txt não foi selecionado, tente novamente','ERRO')
        pass
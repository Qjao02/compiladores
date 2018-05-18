# -*- coding: utf-8 -*-

import easygui
import re
from Token import Token



class AnalisadorLexico:
    estado = 0
    tabelaToken = {}
    buffer = None
    
    '''
    construtor para a classe analisador lexico, inicia o estado com o padrão e faz a leitura da tabela de tokens conhecidos
    pela Linguagem c small
    '''
    def __init__(self):
        self.estado = 0
        while True:
            #easygui.msgbox('selecione o arquivo tabelaToken.txt','IMPORTANTE')
            if self.carregaTabelaToken() == 1:
                break
    
    #Getters and Setters
    def setEstado(self, estado):
        self.estado = 0
        self.estado = estado

    def getEstado(self):
        return self.estado

    def setBuffer(self, caracter):
        self.buffer = caracter

    def getBuffer(self):
        return self.buffer

    #tabela Token contida em um arquivo informa as palavras reservadas da linguagem c small, além das expressões regulares para IDS
    #Floats e Inteiros
    def carregaTabelaToken(self):
        try:
            pathToTabelaToken = '../entrada/tabelaToken.txt'
            tabelaArc = open(pathToTabelaToken, "r")
            while True:
                linha = tabelaArc.readline()

                if not linha:
                    break

                aux = linha.split()
                chave = aux[0]
                valor = aux[1]
                self.tabelaToken[chave] = valor
            return 1
        except:
            self.tabelaIOMessageError()
            return 0 

     

       
    def proximoEstado(self, caracter, numLinha, vetorToken):
        
        token = None
        
        #conjunto de estados para a representação do meu automato
        if self.estado == 0:
            self.classfica(caracter, numLinha)
                
        else:            

            if self.getEstado() == 1:
                self.setEstado(1)
                token = self.estadoUm(caracter, numLinha)

            elif self.getEstado() == 2:
                self.setEstado(2)
                token = self.estadoDois(caracter, numLinha)

            elif self.getEstado() == 3:
                self.setEstado(3)
                token = self.estadoTres(caracter, numLinha)
            elif self.getEstado() == 4:
                self.setEstado(4)
                token = self.estadoQuatro(caracter,numLinha)

        if not (token is None):
            vetorToken.append(token)
        
       


    def estadoUm (self, caracter, numLinha):
 
        validCharacter = re.fullmatch('[A-Za-z]|[0-9]|_', caracter)
        if not(validCharacter is None):
            
            self.concat(caracter)
            return None

        else:
            
            self.setEstado(0)
            keys = self.tabelaToken.keys()
            if self.buffer in keys:
                token = Token(self.tabelaToken[self.buffer], self.buffer, numLinha)
                self.classfica(caracter,numLinha)
            else:
                token = Token(self.tabelaToken['[A-Za-z]([A-Za-z]|[0-9]|_)*'], self.buffer, numLinha)
                self.classfica(caracter, numLinha)

            return token

            
    def estadoDois (self, caracter, numLinha):
        
        validCharacter = re.fullmatch('[0-9]', caracter)
        if not(validCharacter is None):    
            self.concat(caracter)
            return None

        elif caracter == '.':
            self.setEstado(3)    
            self.concat(caracter)
            
        else:  
            self.setEstado(0)

            keys = self.tabelaToken.keys()
            
            if self.buffer in keys:
                token = Token(self.tabelaToken[self.buffer], self.buffer, numLinha)
                self.classfica(caracter, numLinha)

            else:
                token = Token(self.tabelaToken['[0-9]([0-9])*'], self.buffer, numLinha)
                self.classfica(caracter, numLinha)
            
            return token
        
    def estadoTres(self, caracter, numLinha):
        
        validCharacter = re.match('[0-9]',caracter)
        if not (validCharacter is None):    
            self.concat(caracter)

            return None
        
        else:    
            keys = self.tabelaToken.keys()
            
            if self.buffer in keys:
                token = Token(self.tabelaToken[self.buffer], self.buffer, numLinha)
                self.classfica(caracter,numLinha)
            else:
                token = Token(self.tabelaToken['[0-9]([0-9])*.[0-9]([0-9])*'], self.buffer, numLinha)
                self.classfica(caracter,numLinha)
            
            return token

    def estadoQuatro(self, caracter, numLinha):
        validCharacter = re.fullmatch('\w',caracter)
        if not(validCharacter is None):
            token = Token(self.tabelaToken[self.getBuffer()],self.buffer,numLinha)
            self.setBuffer(caracter)
            self.classfica(caracter,numLinha)
        else:
            try:
                aux = self.getBuffer() + caracter
                token = Token(self.tabelaToken[aux],aux ,numLinha)
                self.setEstado(0)

            except:
                token = Token(self.tabelaToken[self.getBuffer()],self.getBuffer(),numLinha)
                self.setBuffer(caracter)
                self.classfica(caracter,numLinha)


        return token
    def concat(self, character):
        self.buffer = self.buffer+character
   

    def tabelaIOMessageError(self):
        easygui.msgbox('o diretorio do arquivo selecionado encontrou algum erro, tente Novamente','ERRO')   


    def classfica(self,caracter, numLinha):
        choice = re.fullmatch('[A-Za-z]',caracter)
        if not(choice is None):
            self.setEstado(1)
            self.setBuffer(caracter)
        
        choice2 = re.fullmatch('[0-9]',caracter)
        if not(choice2 is None):
            self.setEstado(2)
            self.setBuffer(caracter)

        if (choice is None) and (choice2 is None) and (caracter is not ' ' )and (caracter is not '\n'):
            self.setEstado(4)
            self.setBuffer(caracter)
        
        if caracter is ' ' or caracter is '\n':
            self.setEstado(0)

# -*- coding: utf-8 -*-

class Token ():
    codigoToken = ""
    lexema = ""
    num_linha = ""

    #construtor da classe Token
    def __init__(self, codigoToken, lexema, num_linha):
        self.codigoToken = codigoToken
        self.lexema = lexema
        self.num_linha = num_linha

    #Getters and Setters
    def getNomeToken(self):
        return self.nomeToken

    def setNomeToken(self, nomeToken):
         self.nomeToken = nomeToken

    def getCodigoToken(self):
        return self.codigoToken

    def setCodigoToken(self, codigoToken):
        self.codigoToken = codigoToken
        
    def getLexema(self):
        return self.nomeToken

    def setLexema(self, lexema):
        self.lexema = lexema

    def getNumLinha(self):
        return self.num_linha

    def setNuminha(self, num_linha):
        self.num_linha = num_linha

    

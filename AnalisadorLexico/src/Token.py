# -*- coding: utf-8 -*-

class Token ():
    codigoToken = ""
    lexema = ""
    num_linha = ""
    value = ""

    #construtor da classe Token
    def __init__(self, codigoToken, lexema, num_linha):
        self.codigoToken = codigoToken
        self.lexema = lexema
        self.num_linha = num_linha
        self.value = None


    def getCodigoToken(self):
        return self.codigoToken

    def setCodigoToken(self, codigoToken):
        self.codigoToken = codigoToken
        
    def getLexema(self):
        return self.lexema

    def setLexema(self, lexema):
        self.lexema = lexema

    def getNumLinha(self):
        return self.num_linha

    def setNuminha(self, num_linha):
        self.num_linha = num_linha

    
    def __str__(self):
        return 'Codigo: ' + self.getCodigoToken() + ' lexema: ' + self.getLexema() + ' num_linha: ' + str(self.getNumLinha())
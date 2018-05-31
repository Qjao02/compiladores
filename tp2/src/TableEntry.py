
class TableEntry(object):
    
    def __init__(self, lexema, tipo, num_linha, ref_valor):
        self.lexema = lexema
        self.tipo = tipo
        self.num_linha = num_linha
        self.ref_valor = ref_valor

    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    def setRefValor(self, rv):
        self.ref_valor = rv

    def setLexema(self,lexema):
        self.lexema = lexema
    
    def setNumLinha(self,numLinha):
        self.num_linha = numLinha

    def getNumLinha(self):
        return self.num_linha

    def getLexema(self):
        return self.lexema

    def toString(self):
        return str('Lexema: ' + str(self.lexema) + ', tipo: '+ str(self.tipo) +  ', num_Linha: ' + str(self.num_linha) + ', valor referenciado: ' + str(self.ref_valor))



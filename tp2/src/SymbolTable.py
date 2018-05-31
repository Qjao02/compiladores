"""
 TableEntry é uma classe que possui os seguintes campos:
     - lexema
     - tipo
     - ponteiro para o valor
     - num da linha
"""



class SymbolTable(object):
    def __init__(self):
        self.symbolTable = {}

    def insertEntry(self, lexema, entry):
        self.symbolTable[lexema] = entry;

    def getEntry(self, lexema):
        return self.symbolTable[lexema]
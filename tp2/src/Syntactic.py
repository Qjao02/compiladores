#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sat Aug 26 10:28:28 2017

    @author: alexandre
"""

from Token import Token
from SymbolTable import SymbolTable
from TableEntry import TableEntry
from SymbolTableTree import SymbolTableTree

class Syntactic():
    token = ''
    arrayToken = []
    indexToken = ''
    ASA = ''
    symbolTableTree = ''
    tableEntry = ''
    actualTable = ''

    def __init__ (self, arrayToken):
        self.arrayToken = arrayToken
        self.token = self.arrayToken[0]
        self.indexToken = 0
        self.actualTable = SymbolTable()
        self.symbolTableTree = SymbolTableTree(self.actualTable)
        
    def match(self,tok):
        if(self.token.getCodigoToken() == tok):
            '''for k,v in self.actualTable.symbolTable.items():
                print(v.toString())'''
            self.indexToken = self.indexToken + 1
            if (self.indexToken < len(self.arrayToken)):
                self.token = self.arrayToken[self.indexToken]
                print('Token atual: ' + self.token.getCodigoToken())

        else:
            print('token invalido ' + self.token.getCodigoToken())

    def imprimeErro(self):
        print ('bla')
        i = self.indexToken - 1;
        #print('Tokens ' + str(Follow[sync_token.type]) + ' esperados na entrada.')
        #continua a análise para verificar outros erros
        self.indexToken = self.indexToken + 1
        self.token = self.arrayToken[self.indexToken]
        #sincroniza(sync_token)



    def program(self):
       
        #match first token for any code in c-small
        print(self.token.__str__())
        input()
        self.match('INT')
        self.match('MAIN')
        self.match('LBRACKET')
        self.match('RBRACKET')
        self.match('LBRACE')


        #start recursion and build ASA
        self.decl_comand()

        print('analise sintática realizada com sucesso')
        print('resultado')

        a = open('../../tp2/output/saidateste.txt','w')
        for k,v in self.actualTable.symbolTable.items():
            a.write(v.toString() + '\r\n')

        a.close()

    
    def decl_comand(self):
        print('decl_comand')
        if(self.token.getCodigoToken() == 'INT' or self.token.getCodigoToken() == 'FLOAT'):
            self.declaration()
            self.decl_comand()

        elif(self.token.getCodigoToken() == 'LBRACE' or self.token.getCodigoToken() == 'ID' or self.token.getCodigoToken() == 'IF' or self.token.getCodigoToken() == 'WHILE' or self.token.getCodigoToken() == 'READ' or self.token.getCodigoToken() == 'PRINT' or self.token.getCodigoToken() == 'FOR'):
            self.comand()
            self.decl_comand()
        

    


    def types(self):
        
        if(self.token.getCodigoToken() == 'INT'):
            self.match('INT')
            self.tableEntry.setTipo('int')
        elif(self.token.getCodigoToken() == 'FLOAT'):
            self.match('FLOAT')
            self.tableEntry.setTipo('float')
     

    def declaration(self):

        if (self.token.getCodigoToken() == 'INT' or self.token.getCodigoToken() == 'FLOAT'):
            
            self.tableEntry = TableEntry(None, None, None, None)
            self.types()            
            self.tableEntry.setLexema(self.token.getLexema())
            self.tableEntry.setNumLinha(self.token.getNumLinha())
       

            self.match('ID')
            self.declaration2()
            

    def declaration2(self):
        
        if (self.token.getCodigoToken() == 'COMMA'):
            self.match('COMMA')
            tipo = self.tableEntry.getTipo()
            self.actualTable.symbolTable[self.tableEntry.getLexema()] = self.tableEntry
            self.tableEntry = TableEntry(tipo, None, None, None)
            
            
            self.tableEntry.setLexema(self.token.getLexema())
            self.tableEntry.setNumLinha(self.token.getNumLinha())

            self.match('ID')
            self.declaration2()

        elif(self.token.getCodigoToken() == 'PCOMMA'):
            self.match('PCOMMA')
            self.actualTable.symbolTable[self.tableEntry.getLexema()] = self.tableEntry
            self.tableEntry = TableEntry(None, None, None, None)

        elif(self.token.getCodigoToken() == 'ATTR'):
            
            self.match('ATTR')
            self.expression()
            self.declaration2()    

       

    def comand(self):
        if (self.token.getCodigoToken() == 'LBRACE'):
            self.block()
        
        elif(self.token.getCodigoToken() == 'ID'):
            self.attr()
        
        elif(self.token.getCodigoToken() == 'IF'):
            self.comand_if()
        
        elif(self.token.getCodigoToken() == 'WHILE'):
            self.comand_while()
        
        elif(self.token.getCodigoToken() == 'READ'):
            self.comand_read()
        
        elif(self.token.getCodigoToken() == 'PRINT'):
            self.comand_print()
        
        elif(self.token.getCodigoToken() == 'FOR'):
            self.comand_for()
        


    def block(self):
        self.match('LBRACE')
        self.decl_comand()
        self.match('RBRACE')


    def attr(self):
        self.match('ID')
        self.match('ATTR')
        self.expression()
        self.match('PCOMMA')
    
    def comand_if(self):
        self.match('IF')
        self.match('LBRACKET')
        self.expression()
        self.match('RBRACKET')
        self.comand()
        if(self.token == 'ELSE'):
            self.comand_else()
        
    
    def comand_else(self):
        self.match('ELSE')
        self.comand()

    def comand_while(self):
        self.match('WHILE')
        self.match('LBRACKET')
        self.expression()
        self.match('RBRACKET')
        self.comand()

    
    def comand_read(self):
        self.match('READ')
        self.match('ID')
        self.match('PCOMMA')
    
    def comand_print(self):
        self.match('PRINT')
        self.match('LBRACKET')
        self.expression()
        self.match('RBRACKET')
        self.match('PCOMMA')

    def comand_for(self):
        self.match('FOR')
        self.match('LBRACKET')
        self.att_for()
        self.match('PCOMMA')
        self.expression()
        self.match('PCOMMA')
    
    def att_for(self):
        self.match('RBRACKET')
        self.comand()

    def expression(self):
        if (self.token.getCodigoToken() == 'ID' or self.token.getCodigoToken() == 'INTEGER_CONST' or self.token.getCodigoToken() == 'FLOAT_CONST' or self.token.getCodigoToken() == 'LBRACKET'):
            self.conjunction()
            
            if (self.token.getCodigoToken() == 'OR'):
                self.expressaoOpc()

    
    def expressaoOpc(self):
        self.match('OR')
        self.conjunction()
        self.expressaoOpc() 
    
    def conjunction(self):
        if (self.token.getCodigoToken() == 'ID' or self.token.getCodigoToken() == 'INTEGER_CONST' or self.token.getCodigoToken() == 'FLOAT_CONST' or self.token.getCodigoToken() == 'LBRACKET'):
            self.equal()
            
            if(self.token.getCodigoToken() == 'AND'):
                self.conjuction_opc() 
    
    def conjuction_opc(self):
        self.match('AND')
        self.equal()
        
        if(self.token == 'AND'):
            self.conjuction_opc

    def equal(self):
        if (self.token.getCodigoToken() == 'ID' or self.token.getCodigoToken() == 'INTEGER_CONST' or self.token.getCodigoToken() == 'FLOAT_CONST' or self.token.getCodigoToken() == 'LBRACKET'):
            self.relation()
            if (self.token.getCodigoToken() == 'EQ' or self.token.getCodigoToken() == 'NE'):
                self.equal_opc
    
    def equal_opc(self):
        self.op_equal()
        self.relation()
        
        if (self.token == 'EQ' or self.token == 'NE'):
            self.equal_opc()
    
    def relation(self):
        if (self.token.getCodigoToken() == 'ID' or self.token.getCodigoToken() == 'INTEGER_CONST' or self.token.getCodigoToken() == 'FLOAT_CONST' or self.token.getCodigoToken() == 'LBRACKET'):
            self.add()

            if(self.token.getCodigoToken() == 'LT' or self.token.getCodigoToken() == 'LE' or self.token.getCodigoToken() == 'GT' or self.token.getCodigoToken() == 'GE'):
                self.relac_opc()

    def op_equal(self):
        self.match('EQ')
        self.match('NE')

    def relac_opc(self):
        self.op_rel()
        self.add()
        if(self.token == 'LT' or self.token == 'LE' or self.token == 'GT' or self.token == 'GE'):
            self.relac_opc()
    
    def op_rel(self):
        
        if (self.token.getCodigoToken() == 'LT'):
            self.match('LT')
        
        elif(self.token.getCodigoToken() == 'LE'):
            self.match('LE')

        elif(self.token.getCodigoToken() == 'GT'):
            self.match('GT')

        elif (self.token.getCodigoToken() == 'GE'):
            self.match('GE')
              
    def add(self):
        if (self.token.getCodigoToken() == 'ID' or self.token.getCodigoToken() == 'INTEGER_CONST' or self.token.getCodigoToken() == 'FLOAT_CONST' or self.token.getCodigoToken() == 'LBRACKET'):
            self.term()
            if (self.token.getCodigoToken() == 'PLUS' or self.token.getCodigoToken() == 'MINUS'):
                self.add_opc()
    
    def add_opc(self):
        self.op_add()
        self.term()
        if (self.token.getCodigoToken() == 'PLUS' or self.token.getCodigoToken() == 'MINUS'):
            self.add_opc()
    
    def op_add(self):
        if(self.token.getCodigoToken() == 'PLUS'):
            self.match('PLUS')
       
        if(self.token == 'MINUS'):
            self.match('MINUS')

    def term(self):
        if (self.token.getCodigoToken() == 'ID' or self.token.getCodigoToken() == 'INTEGER_CONST' or self.token.getCodigoToken() == 'FLOAT_CONST' or self.token.getCodigoToken() == 'LBRACKET'):
            self.fact() 
            
            if(self.token.getCodigoToken() == 'MULT' or self.token.getCodigoToken() == 'DIV'):
                self.term_opc()

    def term_opc(self):
        self.op_mult()
        self.fact()
        if(self.token == 'MULT' or self.token == 'DIV'):
            self.term_opc()

    
    def op_mult(self):
        if(self.token.getCodigoToken() == 'MULT'):
            self.match('MULT')
        elif(self.token.getCodigoToken() == 'DIV'):
            self.match('DIV')
        
    
    def fact(self):
        if (self.token.getCodigoToken() == 'ID'):
            self.match('ID')
        
        elif(self.token.getCodigoToken() == 'INTEGER_CONST'):
            '''
            self.tableEntry.setLexema(self.token.getLexema())
            self.tableEntry.setNumLinha(self.token.getNumLinha())
        
            
            self.actualTable.symbolTable[self.token.getLexema()] = self.tableEntry
            self.tableEntry = TableEntry(None, None, None, None)
            '''
            self.match('INTEGER_CONST')
        
        elif(self.token.getCodigoToken() == 'FLOAT_CONST'):
            '''
            self.tableEntry.setLexema(self.token.getLexema())
            self.tableEntry.setNumLinha(self.token.getNumLinha())
    
            
            print('adicionando o simbolo na tabela de entrada')

            self.actualTable.symbolTable[self.token.getLexema()] = self.tableEntry
            self.tableEntry = TableEntry(None, None, None, None)
            '''
            self.match('FLOAT_CONST')

        elif(self.token.getCodigoToken() == 'LBRACKET'):
            self.match('LBRACKET')
            self.expression()
            self.match('RBRACKET')

    


    '''
    def E():
        global token;
        if (token.type == ID or token.type == NUM or token.type == LBRACKET):
            no_ope1 = T();
            no = E_(no_ope1);
            if(token.type == EOF):
                match(EOF)
                print('Fim da análise sintática.')
                return no;
            return no
        else:
            imprimeErro();
            return None

    def E_(no_ope1):
        global token;
        if(token.type == PLUS):
            match(PLUS);
            no_ope2 = T();
            no = ArithOp('+', no_ope1, no_ope2)
            return E_(no);
        elif (token.type == MINUS):
            match(MINUS);
            no_ope2 = T();
            no = ArithOp('-', no_ope1, no_ope2)
            return E_(no);
        return no_ope1

    def T():
        global token;
        no_ope1 = F();
        return T_(no_ope1);

    def T_(no_ope1):
        global token;
        if (token.type == MULT):
            match(MULT);
            no_ope2 = F();
            no = ArithOp('*', no_ope1, no_ope2)
            return  T_(no);
        elif(token.type == DIV):
            match(DIV);
            no_ope2 = F();
            no = ArithOp('/', no_ope1, no_ope2)
            return  T_(no);
        return no_ope1

    def F():
        global token;
        if(token.type == LBRACKET):
     /../tp2/src/Sintatico.py", line 116       match(LBRACKET);
            no = E();ef imprimeErro():
        i = self.indexToken - 1;
        sync_token = vetorTokens[i]
        #print('Tokens ' + str(Follow[sync_token.type]) + ' esperados na entrada.')
        #continua a análise para verificar outros erros
        i = self.indexToken + 1
        self.token = vetorTokens[i]
        #sincroniza(sync_token)


            match(RBRACKET);
            return no
        elif (token.type == ID):
            no = Id(token)
            match(ID);
            return no
        elif(token.type == NUM):
            no = Num(token)
            match(NUM)
            return no
        else:
            imprimeErro();
            return None
    '''
    """
    Início da análise sintática de descida recursiva
    """
    #print(str(root.__evaluate__()))

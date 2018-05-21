#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sat Aug 26 10:28:28 2017

    @author: alexandre
"""

import Token
import SymbolTable
import TableEntry
import ASA


class Syntactic():
    token = ''
    arrayToken = []
    indexToken = ''
    ASA = ''
    

    def __init__ (self, arrayToken):
        self.arrayToken = arrayToken
        self.token = self.arrayToken[0]
        self.indexToken = 0
    
    def match(self,tok):
        if(self.token.getCodigoToken() == tok):
            print('Token ' + self.token.getCodigoToken() + ' reconhecido na entrada.')
            self.indexToken = self.indexToken + 1
            if (self.indexToken < len(self.arrayToken)):
                self.token = self.arrayToken[self.indexToken]
        else:
            print(self.token)

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
        self.match('INT')
        self.match('MAIN')
        self.match('LBRACKET')
        self.match('RBRACKET')
        self.match('LBRACE')

        #start recursion and build ASA
        self.decl_comand()


    

    def decl_comand(self):
        
        

        if(self.token == 'INT ' or self.token == 'FLOAT'):
            self.declaration()
            self.decl_comand()

        elif(self.token == 'LBRACE' or self.token == 'ID' or self.token == 'IF' or self.token == 'WHILE' or self.token == 'READ' or self.token == 'PRINT' or self.token == 'FOR'):
            self.comand()

    


    def types(self):
        
        if(self.token == 'INT'):
            self.match(self.token)
        
        elif(self.token == 'FLOAT'):
            self.match('FLOAT')


    def declaration(self):

        if (self.token == 'INT' or self.token == 'FLOAT'):
            
            self.type()
            self.match('ID')
            
            if(self.token == 'COMMA' or self.token == 'PCOMMA' or self.token == 'ATTR'):
                self.declaration2()

    def declaration2(self):
        if (self.token == 'COMMA'):
            self.match('COMMA')
            self.match('ID')
            if(self.token == 'COMMA' or self.token == 'PCOMMA' or self.token == 'ATTR'):
                self.declaration2()
        
        elif(self.token == 'PCOMMA'):
            self.match('PCOMMA')

        elif(self.token == 'ATTR):
            self.match('ATTR')
            if (self.token == 'ID' or self.token == 'INTEGER_CONST' or self.token == 'FLOAT_CONST' or self.token == 'LBRACKET'):
                self.expression()
            if(self.token == 'COMMA' or self.token == 'PCOMMA' or self.token == 'ATTR'):
                self.declaration2()    

       

    def comand(self):
    elif(self.token == 'LBRACE' or self.token == 'ID' or self.token == 'IF' or self.token == 'WHILE' or self.token == 'READ' or self.token == 'PRINT' or self.token == 'FOR'):

        if (self.token == 'LBRACE'):
            self.block()
        
        elif(self.token == 'ID'):
            self.attr()
        
        elif(self.token == 'IF'):
            self.comand_if()
        
        elif(self.token == 'WHILE'):
            self.comand_while()
        
        elif(self.token == 'READ')
            self.self.comand_read()
        
        elif(self.token == 'PRINT'):
            self.comand_print('PRINT')
        
        elif(self.token == 'FOR'):
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
        self.match('LBRACKET')
        self.comand()
        if(self.token == 'ELSE'):
            self.comand_else()
    
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
        if (self.token == 'ID' or self.token == 'INTEGER_CONST' or self.token == 'FLOAT_CONST' or self.token == 'LBRACKET'):
            self.conjunction()
            
            if (self.token == 'OR'):
                self.expressaoOpc()

    
    def expressaoOpc(self):
        self.match('OR')
        self.conjunction()
        self.expressaoOpc() 
    
    def conjunction(self):
        if (self.token == 'ID' or self.token == 'INTEGER_CONST' or self.token == 'FLOAT_CONST' or self.token == 'LBRACKET'):
            self.equal()
            
            if(self.token == 'AND'):
                self.conjuction_opc() 
    
    def conjuction_opc(self):
        self.match('AND')
        self.equal()
        
        if(self.token == 'AND'):
            self.conjuction_opc

    def equal(self):
        if (self.token == 'ID' or self.token == 'INTEGER_CONST' or self.token == 'FLOAT_CONST' or self.token == 'LBRACKET'):
            self.relacao()
            if (self.token == 'EQ' or self.token == 'NE'):
                self.equal_opc
    
    def equal_opc(self):
        self.op_equal()
        self.relation()
        
        if (self.token == 'EQ' or self.token == 'NE'):
            self.equal_opc()
    
    def relation(self):
        if (self.token == 'ID' or self.token == 'INTEGER_CONST' or self.token == 'FLOAT_CONST' or self.token == 'LBRACKET'):
            self.add()

    def op_equal(self):
        self.match('EQ')
        self.match('NE')

    def relac_opc(self):
        self.op_rel()
        self.relation()
        if(self.token == 'LT' or self.token == 'LE' or self.token == 'GT' or self.token == 'GE'):
            self.relac_opc()
    
    def op_rel(self):
        if (self.token == 'LT'):
            self.match('LT')
        
        elif(self.token == 'LE'):
            self.match('LE')

        elif(self.token == 'GT'):
            self.match('GT')

        elif (self.token == 'GE'):
            self.match('GE')
            )   
    def add(self):
        if (self.token == 'ID' or self.token == 'INTEGER_CONST' or self.token == 'FLOAT_CONST' or self.token == 'LBRACKET'):
            self.term()
            if (self.token == 'PLUS' or self.token == 'MINUS'):
                self.add_opc()
    
    def add_opc(self):
        self.op_add()
        self.term()
        if (self.token == 'PLUS' or self.token == 'MINUS'):
            self.add_opc()
    
    def op_add(self):
        if(self.token == 'PLUS'):
            self.match('PLUS')
       
        if(self.token == 'MINUS'):
            self.match('MINUS')

    def term(self):
        if (self.token == 'ID' or self.token == 'INTEGER_CONST' or self.token == 'FLOAT_CONST' or self.token == 'LBRACKET'):
            self.fact() 

        if(self.token == 'MULT' or self.token == 'DIV'):
             self.term_opc()

    def term_opc(self):
        self.op_mult()
        self.fact()
        if(self.token == 'MULT' or self.token == 'DIV'):
            self.term_opc()

    
    def op_mult(self):
        if(self.token == 'MULT')
            self.match('MULT')
        elif(self.token == 'DIV')
            self.match('DIV')
        
    
    def fact(self):
        if (self.token == 'ID'):
            self.match('ID')
        
        elif(self.token == 'INTEGER_CONST'):
            self.match('INTEGER_CONST')
        
        elif(self.token == 'FLOAT_CONST'):
            self.match('FLOAT_CONST')

        elif(self.token == 'LBRACKET'):
            self.match('LBRACKET')
            if (self.token == 'ID' or self.token == 'INTEGER_CONST' or self.token == 'FLOAT_CONST' or self.token == 'LBRACKET'):
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

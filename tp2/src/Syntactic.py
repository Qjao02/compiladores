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
        
        if (self.token == 'INT' OR self.token == 'FLOAT'):
            
            self.type()
            self.match('ID')
            
            if(self.token == 'COMMA' or self.token == 'PCOMMA' or self.token == 'ATTR'):
                self.declaration2()


        elif(self.token == 'LBRACE' OR self.token == 'ID' or self.token == )
        
    


    def types(self):
        
        if(self.token == 'INT'):
            self.match(self.token)
        
        elif(self.token == 'FLOAT'):
            self.match('FLOAT')


    def declaration(self)
        pass

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
        pass
    
    def block(self):
        pass

    def assignmentt(self):
        pass

    def comand_if(self):
        pass
    
    def comand_else(self):
        pass

    def comand_when(self):
        pass
    
    def comand_read(self):
        pass
    
    def comand_print(self):
        pass

    def comand_for(self):
        pass
    
    def att_for(self):
        pass

    def expression(self):
        if (self.token == 'ID' or self.token == 'INTEGER_CONST' or self.token == 'FLOAT_CONST' or self.token == 'LBRACKET'):


    
    def expressaoOpc(self):
        pass
    
    def conjunction(self):
        pass
    
    def conjuction_opc(self):
        pass

    def equal(self):
        if (self.token == 'ID' or self.token == 'INTEGER_CONST' or self.token == 'FLOAT_CONST' or self.token == 'LBRACKET'):
            self.relacao()
        
    
    def relation(self):
        if (self.token == 'ID' or self.token == 'INTEGER_CONST' or self.token == 'FLOAT_CONST' or self.token == 'LBRACKET'):
            self.add()
    def op_equal(self):
        pass

    def relac_opc(self):
        pass
    
    def op_rel(self):
        pass
    
    def add(self):
        if (self.token == 'ID' or self.token == 'INTEGER_CONST' or self.token == 'FLOAT_CONST' or self.token == 'LBRACKET'):
            self.term()
    
    def add_opc(self):
        pass
    
    def op_add(self):
        pass

    def term(self):
        if (self.token == 'ID' or self.token == 'INTEGER_CONST' or self.token == 'FLOAT_CONST' or self.token == 'LBRACKET'):
            self.fact()
    
    def term_opc(self):
        pass
    
    def op_mult(self):
        pass
    
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

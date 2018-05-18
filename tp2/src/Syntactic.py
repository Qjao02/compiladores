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
        for l in self.arrayToken:
            print(l.getCodigoToken())
        self.match('INT')
        self.match('MAIN')
        self.match('LBRACKET')
        self.match('RBRACKET')
        self.match('LBRACE')


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

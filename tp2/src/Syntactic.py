#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

    @author: Juaumpc
"""

from Token import Token
from SymbolTable import SymbolTable
from TableEntry import TableEntry
from SymbolTableTree import SymbolTableTree
from ASA import *

class Syntactic():
    token = ''
    arrayToken = []
    indexToken = ''
    no = ''
    symbolTableTree = ''
    tableEntry = ''
    actualTable = ''

    def __init__ (self, arrayToken):
        self.arrayToken = arrayToken
        self.token = self.arrayToken[0]
        self.indexToken = 0
        self.actualTable = SymbolTable()
        self.symbolTableTree = SymbolTableTree(self.actualTable)
        self.no = AST('AST')
    def match(self,tok):
        if(self.token.getCodigoToken() == tok):
            '''for k,v in self.actualTable.symbolTable.items():
                print(v.toString())'''
            self.indexToken = self.indexToken + 1
            if (self.indexToken < len(self.arrayToken)):
                self.token = self.arrayToken[self.indexToken]

        else:
            print('token invalido ' + self.token.getCodigoToken())

    def imprimeErro(self):
        i = self.indexToken - 1;
        #print('Tokens ' + str(Follow[sync_token.type]) + ' esperados na entrada.')
        #continua a análise para verificar outros erros
        self.indexToken = self.indexToken + 1
        self.token = self.arrayToken[self.indexToken]
        #sincroniza(sync_token)



    def program(self):
       
        #match first token for any code in c-small
        print(self.token.__str__())
        self.match('INT')
        self.match('MAIN')
        self.match('LBRACKET')
        self.match('RBRACKET')
        self.match('LBRACE')

        print(self.token.value)
        #start recursion and build ASA
        print('bla ' + self.no.nome)
        self.decl_comand(self.no)

        print('analise sintática realizada com sucesso')
        print('resultado')
        print(self.no.children)
        
        print_tree(self.no)
        
        a = open('../../tp2/output/saidateste.txt','w')
        
        for k,v in self.actualTable.symbolTable.items():
            a.write(v.toString() + '\r\n')

        ToXML.toXML(self.no)
        a.close()


    
    def decl_comand(self,no):
        if(self.token.getCodigoToken() == 'INT' or self.token.getCodigoToken() == 'FLOAT'):
            self.declaration(no)
            
            if(self.token.getCodigoToken() == 'INT' or self.token.getCodigoToken() == 'FLOAT' or self.token.getCodigoToken() == 'LBRACE' or self.token.getCodigoToken() == 'ID' or self.token.getCodigoToken() == 'IF' or self.token.getCodigoToken() == 'WHILE' or self.token.getCodigoToken() == 'READ' or self.token.getCodigoToken() == 'PRINT' or self.token.getCodigoToken() == 'FOR'):
                self.decl_comand(no)

        elif(self.token.getCodigoToken() == 'LBRACE' or self.token.getCodigoToken() == 'ID' or self.token.getCodigoToken() == 'IF' or self.token.getCodigoToken() == 'WHILE' or self.token.getCodigoToken() == 'READ' or self.token.getCodigoToken() == 'PRINT' or self.token.getCodigoToken() == 'FOR'):
            no3 = self.comand()

            if(not(no3 is None)):
                no.children.append(no3)

            if(self.token.getCodigoToken() == 'INT' or self.token.getCodigoToken() == 'FLOAT' or self.token.getCodigoToken() == 'LBRACE' or self.token.getCodigoToken() == 'ID' or self.token.getCodigoToken() == 'IF' or self.token.getCodigoToken() == 'WHILE' or self.token.getCodigoToken() == 'READ' or self.token.getCodigoToken() == 'PRINT' or self.token.getCodigoToken() == 'FOR'):
                self.decl_comand(no)
           # print('O no attr aqui ')
            print(self.no.children)


        
        

    


    def types(self):
        
        if(self.token.getCodigoToken() == 'INT'):
            self.match('INT')
            self.tableEntry.setTipo('int')

        elif(self.token.getCodigoToken() == 'FLOAT'):
            self.match('FLOAT')
            self.tableEntry.setTipo('float')
     

    def declaration(self, no):

        if (self.token.getCodigoToken() == 'INT' or self.token.getCodigoToken() == 'FLOAT'):
            
            self.tableEntry = TableEntry(None, None, None, None)
            self.types()            
            self.tableEntry.setLexema(self.token.getLexema())
            self.tableEntry.setNumLinha(self.token.getNumLinha())

            #começo da criação da asa
            no_id = ''
            if(self.token.getCodigoToken() == 'ID'):
                no_id= Id(self.token)
            self.match('ID')
            
            no_attr = None
            if(self.token.getCodigoToken() == 'ATTR'):
                no_attr = Assign(no_id, '=', None)

                
            self.declaration2(self.no, no_attr)
            
            if(not(no_attr is None)):
                print('FILHOS DO NO ATTR DE DECLARACAO \r\n\r\n\r\n')
                print(no_attr.children)
            

    def declaration2(self, no_pai, no):
        
        if (self.token.getCodigoToken() == 'COMMA'):
            self.match('COMMA')
            self.actualTable.symbolTable[self.tableEntry.getLexema()] = self.tableEntry
            lastType = self.tableEntry.getTipo()
            self.tableEntry = TableEntry(None, lastType, None, None)
            
            
            self.tableEntry.setLexema(self.token.getLexema())
            self.tableEntry.setNumLinha(self.token.getNumLinha())
            
            no2 = Id(self.token)
            self.match('ID')
            
            no_attr = None
            if(self.token.getCodigoToken() == 'ATTR'):
                no_attr = Assign(no2, '=', None)


            self.declaration2(no_pai, no_attr)


        elif(self.token.getCodigoToken() == 'PCOMMA'):
            self.match('PCOMMA')
            self.actualTable.symbolTable[self.tableEntry.getLexema()] = self.tableEntry
            self.tableEntry = TableEntry(None, None, None, None)


        elif(self.token.getCodigoToken() == 'ATTR'):
            

            self.match('ATTR')
            no2 = self.expression()
            no.children.append(no2)
            no.right = no2
            no_pai.children.append(no)
            
            print('Atribuiu o no: ' + no.op + ' que tem os filhos :')
            print(no.children)
            
            self.declaration2(no_pai, no)
    
            

       

    def comand(self):
        if (self.token.getCodigoToken() == 'LBRACE'):
            no = self.block()
            print('FILHOS DO NO BLOCO \r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n')
            print(no.children)
            return no
        
        elif(self.token.getCodigoToken() == 'ID'):
            no = self.attr()
            return no
        
        elif(self.token.getCodigoToken() == 'IF'):
            no = self.comand_if()
            print(no.children)
            return no
        
        elif(self.token.getCodigoToken() == 'WHILE'):
            no = self.comand_while()
            return no
        
        elif(self.token.getCodigoToken() == 'READ'):
            no = self.comand_read()
            return no
        
        elif(self.token.getCodigoToken() == 'PRINT'):
            no = self.comand_print()
            return no
        
        elif(self.token.getCodigoToken() == 'FOR'):
            no = self.comand_for()
            return no
        


    def block(self):
        self.match('LBRACE')
        no_block = Compound()
        self.decl_comand(no_block)
        self.match('RBRACE')
        
        print('FILHOS DO NO BLOCO ------ \r\n\r\n\r\n\r\n')
        print(no_block.children)
        return no_block


    def attr(self):
        no1 = Id(self.token)
        print(no1.nome)
        no_attr = Assign(no1 , '=', None)

        self.match('ID')
        self.match('ATTR')

        no2 = self.expression()
        print(no2.nome)
        no_attr.children.append(no2)
        no_attr.right = no2

        print('FILHOS DO NO ATTR \r\n\r\n\r\n\r\n\r\n')
        print(no_attr.children)

        self.match('PCOMMA')

        return no_attr
    
    def comand_if(self):

        no_if = If(None,None,None)

        self.match('IF')
        self.match('LBRACKET')

        no_expr = self.expression()
        no_if.children.append(no_expr)
        no_if.exp = no_expr

        self.match('RBRACKET')
        
        no_comand = self.comand()
        no_if.children.append(no_comand)

        if(self.token == 'ELSE'):
            no_else = self.comand_else()
            no_if.children.append(no_else)

        print(no_if.children)
        return no_if
        
    
    def comand_else(self):
        
        self.match('ELSE')
        no_else = self.comand()
        
        return no_else

    def comand_while(self):

        no_while = While(None,None)

        self.match('WHILE')
        self.match('LBRACKET')

        no_expr = self.expression()
        no_while.children.append(no_expr)
        no_while.exp = no_expr

        self.match('RBRACKET')

        no_comand = self.comand()
        no_while.children.append(no_comand)
        no_while.commands = no_comand
        
        return no_while

    def comand_read(self):
        no_read = Read(None)

        self.match('READ')

        no_id = Id(self.token)
        no_read.children.append(no_id)
        
        print(no_read.children)
        self.match('ID')
        self.match('PCOMMA')

        print('test')
        return no_read

    def comand_print(self):

        no_print = Print(None)

        self.match('PRINT')
        self.match('LBRACKET')

        no_expr = self.expression()
        no_print.children.append(no_expr)
        no_print.exp = no_expr

        print('O NO COMAND PRINT -------\r\n\r\n\r\n\r\n')
        print(no_print.children)

        self.match('RBRACKET')
        self.match('PCOMMA')

        return no_print

    #sem for por enquanto =('''
    def comand_for(self):

        no_for = For(None,None,None,None)
        self.match('FOR')
        self.match('LBRACKET')
        
        no_attr = self.att_for()
        no_for.children.append(no_attr)
        no_for.attr = no_attr
        
        print('FILHOS DO NO ATTR DO FOR: --------------------- \r\n\r\n\r\n')
        print(no_attr.children)
        self.match('PCOMMA')
        
        no_expr = self.expression()
        no_for.children.append(no_expr)
        no_for.exp = no_expr
        
        self.match('PCOMMA')
        
        no_attr2 = self.att_for()
        no_for.children.append(no_attr2)
        no_for.attr2 = no_attr2

        self.match('RBRACKET')

        no_comand = self.comand()
        if(not(no_comand is None)):
            no_for.children.append(no_comand)
            no_for.commands = no_comand
        
        print('Filhos do FOR ----------------')
        print(no_for.children)
        return no_for

    def att_for(self):
       

        no_id = Id(self.token)
        
        
        self.match('ID')
        
        no_attr_for = Assign(no_id,'=',None)
        
        self.match('ATTR')
        no_expr = self.expression()

       
        no_attr_for.children.append(no_expr)
        no_attr_for.right = no_expr


        return no_attr_for

    def expression(self):
        no = self.conjunction()
        
        if (self.token.getCodigoToken() == 'OR'):
            no_expr_opc = self.expressaoOpc()
            no_expr_opc.children.append(no)
            no_expr_opc.left = no

            return no_expr_opc
        
        return no

    
    def expressaoOpc(self):
        no_expr_opc = LogicalOp('OR', None, None)
        self.match('OR')
        self.conjunction()

        if(self.token.getCodigoToken() == 'OR'):
            no_expr_opc2 = self.expressaoOpc() 
            no_expr_opc2.children.left(no_expr_opc)
            no_expr_opc2.left = no_expr_opc
            
            return no_expr_opc2
        
        return no_expr_opc

    def conjunction(self):

        no = self.equal()
            
        if(self.token.getCodigoToken() == 'AND'):
            no_conj = self.conjuction_opc() 
            no_conj.children.append(no)
            no_conj.left = no

        return no
    
    def conjuction_opc(self):
        no_conj = LogicalOp('AND', None, None)
        self.match('AND')
        no = self.equal()
        no_conj.children.append(no)
        no_conj.right = no
        
        if(self.token == 'AND'):
            no_conj2 = self.conjuction_opc()
            no_conj2.children.left(no_conj)
            no_conj2.left = no_conj
            return no_conj2
        
        return no_conj

    def equal(self):
        no = self.relation()

        if (self.token.getCodigoToken() == 'EQ' or self.token.getCodigoToken() == 'NE'):
            no_equal_opc = self.equal_opc()
            no_equal_opc.children.append(no)
            return no_equal_opc
    
        return no

    def equal_opc(self):
        no_op_equal = self.op_equal()
        no = self.relation()
        no_op_equal.children.append(no)
        no_op_equal.right = no
        
        if (self.token == 'EQ' or self.token == 'NE'):
            no_equal_opc2 = self.equal_opc()
            no_equal_opc2.children.append(no)
            return no_equal_opc2


        return no_op_equal

    def op_equal(self):
        if(self.token.getCodigoToken() == 'EQ' ):
            self.match('EQ')
            return RelOp(None, '==', None)
        
        elif(self.token.getCodigoToken() == 'NE'):
            self.match('NE')
            return RelOp(None, '!=', None)

    def relation(self):
        no = self.add()

        if(self.token.getCodigoToken() == 'LT' or self.token.getCodigoToken() == 'LE' or self.token.getCodigoToken() == 'GT' or self.token.getCodigoToken() == 'GE'):
            no_relac_opc = self.relac_opc()
            no_relac_opc.children.append(no)
            no_relac_opc.left = no
            print('filhos do no > \r\n\r\n\r\n\r\n\r\n')
            print(no_relac_opc.children)

            return no_relac_opc

       
        return no 

   

    def relac_opc(self):
        no_op_rel = self.op_rel()
        no2 = self.add()
        no_op_rel.children.append(no2)
        no_op_rel.right = no2

        if(self.token == 'LT' or self.token == 'LE' or self.token == 'GT' or self.token == 'GE'):
            no_op_rel2 = self.relac_opc()
            no_op_rel2.append(no_op_rel)
            no_op_rel2.left = no_op_rel

            return no_op_rel2

       
        return no_op_rel
    def op_rel(self):
        
        if (self.token.getCodigoToken() == 'LT'):
            self.match('LT')
            return RelOp(None,'<',None)
            
        elif(self.token.getCodigoToken() == 'LE'):
            self.match('LE')
            return RelOp(None,'<=',None)

        elif(self.token.getCodigoToken() == 'GT'):
            self.match('GT')
            return RelOp(None, '>', None)

        elif (self.token.getCodigoToken() == 'GE'):
            self.match('GE')
            return RelOp(None, '>=', None)

              
    def add(self):
        no = self.term()
        
        if (self.token.getCodigoToken() == 'PLUS' or self.token.getCodigoToken() == 'MINUS'):
            no_plus_minus = self.add_opc()
            no_plus_minus.children.append(no)
            no_plus_minus.left = no
            
            print('FILHOS DO NO MINUS --------')
            print(no_plus_minus.children)

            return no_plus_minus

        return no

    def add_opc(self):
        no_plus_minus = self.op_add()
        
        no2 = self.term()
        no_plus_minus.children.append(no2)
        no_plus_minus.right = no2

        
        if (self.token.getCodigoToken() == 'PLUS' or self.token.getCodigoToken() == 'MINUS'):
            no_plus_minus2 = self.add_opc()
            no_plus_minus2.children.append(no_plus_minus)
            no_plus_minus.left = no_plus_minus
            return no_plus_minus2
        
        return no_plus_minus

    def op_add(self):

        if(self.token.getCodigoToken() == 'PLUS'):
            no_add = ArithOp('+',None, None)
            self.match('PLUS')
            
            return no_add
       
        if(self.token.getCodigoToken() == 'MINUS'):
            no_minus = ArithOp('-',None, None)
            self.match('MINUS')
            
            return no_minus

    def term(self):
        no = self.fact() 
            
            
        if(self.token.getCodigoToken() == 'MULT' or self.token.getCodigoToken() == 'DIV'):
            no_div_mult = self.term_opc()
            no_div_mult.children.append(no)
            no_div_mult.left = no
            
            print('Criado um no div Mult que tem os filhos : =---------------------')
            print(no_div_mult.children)

            return no_div_mult


        return no

    def term_opc(self):
        no_div_mult = self.op_mult()
        no2 = self.fact()
        no_div_mult.children.append(no2)
        no_div_mult.right = no2
        
        if(self.token == 'MULT' or self.token == 'DIV'):
            no_div_mult2 = self.term_opc()
            no_div_mult2.children.append(no_div_mult)
            no_div_mult.left = no_div_mult
            return no_div_mult2

        return no_div_mult
    
    def op_mult(self):
        if(self.token.getCodigoToken() == 'MULT'):
            no_div_mult = ArithOp('*',None,None)
            self.match('MULT')
            return no_div_mult

        elif(self.token.getCodigoToken() == 'DIV'):
            no_div_mult = ArithOp('/',None,None)
            self.match('DIV')
            return no_div_mult

        
    
    def fact(self):
        if (self.token.getCodigoToken() == 'ID'):
            
            no = Id(self.token)
            self.match('ID')
            return no 
        
        elif(self.token.getCodigoToken() == 'INTEGER_CONST'):
            '''
            self.tableEntry.setLexema(self.token.getLexema())
            self.tableEntry.setNumLinha(self.token.getNumLinha())
        
            
            self.actualTable.symbolTable[self.token.getLexema()] = self.tableEntry
            self.tableEntry = TableEntry(None, None, None, None)
            '''

            no = Num(self.token)
            print('valor do token criado')
            print(no.token.getLexema())

            self.match('INTEGER_CONST')
            return no

        elif(self.token.getCodigoToken() == 'FLOAT_CONST'):
            '''
            self.tableEntry.setLexema(self.token.getLexema())
            self.tableEntry.setNumLinha(self.token.getNumLinha())
    
            
            print('adicionando o simbolo na tabela de entrada')

            self.actualTable.symbolTable[self.token.getLexema()] = self.tableEntry
            self.tableEntry = TableEntry(None, None, None, None)
            '''
            no = Num(self.token)
            print(no.value)
            self.match('FLOAT_CONST')
            return no 

        elif(self.token.getCodigoToken() == 'LBRACKET'):
            self.match('LBRACKET')
            no = self.expression()
            self.match('RBRACKET')
            return no
    



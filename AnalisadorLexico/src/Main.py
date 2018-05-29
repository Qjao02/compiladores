# -*- coding: utf-8 -*-

import json
from AnalisadorLexico import AnalisadorLexico
from IO import IO
import sys
sys.path.insert(0, '../../tp2/src')
from Syntactic import Syntactic

def main():
    
    #objetos instanciados
    io = IO()
    analisadorLexico = AnalisadorLexico()
    
    #vetor De Tokens para o analisador sintático
    vetorToken = []

    while True:
        caracter = io.getNextChar()
       

        if not caracter :
            break
        token = analisadorLexico.proximoEstado(caracter,io.numeroAtualDaLinha, vetorToken)

       
            

    output = io.generateOutputFile()
    json.dump([ob.__dict__  for ob in vetorToken], output)
    output.close()

    #print do vetor de token
    arc = open('teste.txt','w')
    for element in vetorToken:
        arc.write(element.getCodigoToken() + '\n')

    syntactic = Syntactic(vetorToken)
    syntactic.program()

    
if __name__ == '__main__':
    main()

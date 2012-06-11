'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 22/06/2011
@author: Alfonso Kim
'''

import sys
import operator

def next(num):
    if num & 1: # inpar
        return (3*num)+1
    else:
        return int(num/2)
        

def chain(num):
    chain = [num]
    while num != 1:
        num = next(num)
        chain.append(num)
    return len(chain)


def e_14(num):
    lenghts = []
    for i in range(num, 1, -1):
        if i % 10000 == 0:
            sys.stdout.write('\rVoy en %i' % i)
        lenghts.append((i, chain(i)))
    print
    print max(lenghts, key=operator.itemgetter(1)) 



if __name__ == '__main__':
    e_14(1000000)
'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 21/06/2011
@author: Alfonso Kim
'''

import itertools
import sys

def factors(num):
    #print '>[%s]' % [n for n in range(1, num+1) if num % n == 0]
    return ([n for n in range(1, num+1) if num % n == 0])
    #print [n for n in range(num)]
    #return 1

def e_12():
    rows = 1
    row = []
    last_count = 0
    for i in itertools.count(1):
        if i % 10000 == 0:
            sys.stdout.write('\rVoy en %i con %i divisores' % (i, last_count))
        row.append(i)
        if len(row) == rows:
            factors_list = factors(row[-1])
            last_count = len(factors_list)
            if last_count >= 100:
                print 
                print 'Es %i' % row[-1]
                break
            row = []
            rows += 1

if __name__ == '__main__':
    e_12()
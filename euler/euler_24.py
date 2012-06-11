'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 12/07/2011
@author: Alfonso Kim
'''

import itertools


def e_24():
    for c, x in enumerate(itertools.permutations(range(10))): 
        if c == 999999:
            return ''.join([str(n) for n in x])


if __name__ == '__main__':
    print e_24()
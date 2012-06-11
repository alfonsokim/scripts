'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 30/06/2011
@author: Alfonso Kim
'''

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


def e_20():
    return sum(int(d) for d in '%i' % fact(100))

if __name__ == '__main__':
    print e_20()
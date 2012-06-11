'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 20/09/2011
@author: Alfonso Kim
'''

def e_30():
    return sum([i if i == sum([int(d)**5 for d in str(i)]) else 0 for i in range(2, 2354294)])


if __name__ == '__main__':
    print e_30()
'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 01/07/2011
@author: Alfonso Kim
'''

import string

def e_22():
    letters = string.ascii_uppercase
    names = sorted(open('names.txt', 'r').read().replace('"', '').split(','))
    total = 0
    for c, name in enumerate(names):
        name_sum = sum([letters.find(name_char)+1 for name_char in name])
        total += (name_sum * (c+1))
    return total


if __name__ == '__main__':
    print e_22()
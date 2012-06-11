'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 22/08/2011
@author: Alfonso Kim
'''

import math

def e_29(min, max):
    nums = set([])
    for a in range(min, max+1):
        for b in range(min, max+1):
            nums.add(int(math.pow(a, b)))
    #return ', '.join([str(n) for n in sorted(nums)])
    return len(nums)


if __name__ == '__main__':
    print e_29(2, 100)
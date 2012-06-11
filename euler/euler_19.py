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

from datetime import date, timedelta

def e_19():
    current = date(1901, 1, 1)
    stop = date(2000, 12, 31)
    sunday_count = 0
    while True:
        current += timedelta(days=1)
        if current.weekday() == 6 and current.day == 1:
            sunday_count += 1
        if current == stop:
            break
    return sunday_count


if __name__ == '__main__':
    print e_19()
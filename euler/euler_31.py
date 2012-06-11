'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 04/10/2011
@author: Alfonso Kim
'''

COINS = [[1], [2], [5], [10], [20], [50], [100], [200]]

def e_31():
    for coin in COINS:
        coin.append([c[0] for c in COINS if c[0] <= coin[0]])
        print coin
    
    for coin in COINS:
        target = coin[0]
        this_coins = [c for c in coin[1] if target % c == 0]
        print this_coins

if __name__ == '__main__':
    e_31()
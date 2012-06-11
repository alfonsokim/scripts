'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 26/09/2011
@author: Alfonso Kim
'''

FIBO_CACHE = {}

def fibo_slooow(n):
    if n <= 1:
        return n
    return fibo_slooow(n-1)+fibo_slooow(n-2)


def fibo(n):
    if n <= 1:
        return n
    FIBO_CACHE[n] = FIBO_CACHE.get(n) or (fibo(n-1) + fibo(n-2)) 
    return FIBO_CACHE[n]
    

def fibo_generator():
    i = 0
    f = fibo(i)
    while True:
        yield i, f
        i += 1
        f = fibo(i)
        


if __name__ == '__main__':
    for num, num_fibo in fibo_generator():
        print num, num_fibo
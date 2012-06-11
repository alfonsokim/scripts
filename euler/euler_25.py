'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 13/07/2011
@author: Alfonso Kim
'''

import itertools
import math
import numpy

def e_25():
    
    def fibo(n):
        if n <= 2:
            return 1
        return fibo(n-1) + fibo(n-2)
    
    def fibo_lineal(n):
        i = 1
        j = 0
        for k in range(1, n):
            t = i+j
            i = j
            j = t
        return j
    
    def fibo_fast_and_furious(n):
        root5 = math.sqrt(5)
        phi = 0.5 + root5/2
        return long(0.5 + phi**n/root5)
    
    def fibo_matrix(n):
        fibonacci_matrix = numpy.matrix([[1,1],[1,0]])
        return (fibonacci_matrix**(n-1)) [0,0]
    

    memo = {0:0, 1:1}
    def fibo_memo(n):
        if not n in memo:
            memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
        return memo[n]
    
    for n in itertools.count(1):
        fib_n = fibo_memo(n)
        if len('%i' % fib_n) == 1000:
            return n

if __name__ == '__main__':
    print e_25()
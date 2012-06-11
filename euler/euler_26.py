'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 14/07/2011
@author: Alfonso Kim
'''

def is_prime(n):
    '''check if integer n is a prime'''
    n = abs(int(n))     # make sure n is a positive integer
    if n < 2:           # 0 and 1 are not primes
        return False
    if n == 2:          # 2 is the only even prime number
        return True    
    if not n & 1:       # all other even numbers are not primes
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def e_26():
    for i in range(997, 1, -2):
        if is_prime(i):
            print 'i=%i [%.19f]' % (i, float(float(1)/float(i)))
            c = 1
            while (pow(10, c) - 1) % i != 0:
                c += 1
            if (i-c) == 1: break
    return i
                


if __name__ == '__main__':
    print e_26()
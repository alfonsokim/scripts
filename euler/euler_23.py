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

import math

not_sums = []

def get_abundant_numbers(myrange):
    nums = []
    for x in xrange(1, myrange+1):
        if x % 1000 == 0: print 'GAN [%i]' % (x)
        factors = []
        for y in xrange(1, int(math.sqrt(x)+1)):
            if x%y == 0:
                factors.append(x/y)
                factors.append(y)
        if sum(set(factors)) > x:
            nums.append(x)
    return nums

def get_sums(myrange):
    sums = []
    for x in get_abundant_numbers(myrange):
        print 'GS [%i]' % (x)
        for y in get_abundant_numbers(myrange):
            sums.append(x+y)
    return sums


def e_23_lento():
    sums_list = get_sums(28123)
    for x in range(28123+1):
        print 'X [%i]' % (x)
        if x not in sums_list:
            not_sums.append(x)
    return sum(not_sums)


def get_abundant(n):
    start = 1
    t = math.sqrt(n)
    for i in range(2, int(t)+1):
        if n % i == 0: start += i + n / i
    if t == int(t): start -= t
    return start

def e_23(): 
    limit = 20162
    start = 0
    abundants = set()
    for n in range(1, limit):
        if get_abundant(n) > n:
            abundants.add(n)
        if not any( (n-abundant in abundants) for abundant in abundants ):
            start += n
    return start
    

if __name__ == '__main__':
    print e_23()
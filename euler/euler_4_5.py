'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 16/06/2011
@author: Alfonso Kim
'''

def es_palindromo(num):
    return str(num) == str(num)[::-1]


def palindromos():
    start = 1000
    palindromos = []
    for outer in range(start, 0, -1):
        for inner in range(outer, start):
            if es_palindromo(outer*inner):
                #print 'Yupi:%i [%i*%i]' % ((outer*inner), outer, inner)
                palindromos.append(outer*inner)
                break
    print max(palindromos)


def gcd(a, b):
    while b != 0:
        temp = b
        b = a%b
        a = temp
    return a
    

def smallest():
    #a = reduce(lambda x, y: x*y, range(1, 20))
    num = 1
    while True:
        #print ','.join([str(num%i == 0) for i in range(1,20)])
        #232 792 560
        if all([num%i == 0 for i in range(1,20)]):
            return num
        num += 1
        if num % 50000 == 0:
            print num
        
    
    
    
if __name__ == '__main__':
    print 'Tatataaaan:', smallest()
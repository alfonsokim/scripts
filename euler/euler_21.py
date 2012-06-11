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


def e_21():
    even_nums = []
    for num in range(10000):
        #a_even_divisors = [i for i in range(1, int(num/2)+1) if num % i == 0]
        even_func = lambda x: [i for i in range(1, int(x/2) + 1) if x % i == 0] 
        a_even = even_func(num)
        a_sum = sum(a_even)
        b_even = even_func(a_sum)
        if num != sum(a_even) and sum(b_even) == num:
            even_nums.append(num)
    return sum(even_nums)

if __name__ == '__main__':
    print e_21()
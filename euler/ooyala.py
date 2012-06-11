'''
Calcula la representacion en espaniol de todos los numeros 
(con algunos 'ceros' de mas).

Se puede hacer un metodo eficiente hasta la muerte, ya que
realmente se deben de calcular pocas representaciones -- del
 0 al 15, 20, 2?, luego decenas y centenas -- Sin embargo
segun la primera y segunda regla de la optimizacion 
(http://en.wikipedia.org/wiki/Program_optimization) decidi
dejarlo asi y que el metodo sea mas compacto y entendible.

@author: Alfonso Kim
'''

_QUINCE = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 
           'seis', 'siete', 'ocho', 'nueve', 'diez', 'once',
           'doce', 'trece', 'catorce', 'quince']


_DECENAS = ['diez', 'dieci', 'veinti', 'treinta y ', 'cuarenta y ', 
            'cincuenta y ', 'sesenta y ', 'setenta y ', 'ochenta y ', 
            'noventa y ', 'ciento ']


## ======================================================================
def letras(numero):
    ''' Devuelve las letras diferentes que se usan para representar  
        en espaniol desde cero hasta el numero dado.
        @param numero: El numero limite a evaluar
        @return: Una cadena con las letras usadas para escribir los numeros
        @attention: Se asume que el numero esta validado (es un entero menor o igual a 1000) '''
    usados = set([])
    if numero == 1000:
        usados |= set('mil')
    for num in range(numero+1):
        c, d, u = (num/100, (num/10)%10, num%10) #c=cientos, d=decenas, u=unidades
        if num <= 15:
            u, d = num, 0
        str_num = '%s%s%s' % (('%s cientos ' % _QUINCE[c] if c > 1 else ('ciento ' if c == 1 else '')), 
                              (_DECENAS[d] if d > 0 else ''), 
                              _QUINCE[u])
        print str_num
        usados |= set(str_num.replace(' ', ''))
    return ','.join(sorted(usados))


## ======================================================================
if __name__ == '__main__':
    ''' Punto de entrada. Validacion de los numeros a procesar '''
    import sys
    if len(sys.argv) <= 1:
        print >> sys.stderr, 'Uso: ooyala num1 [, num2 [, num3 [, ...]]]'
        sys.exit(1)
    for str_num in sys.argv[1:]:
        try:
            num = int(str_num)
            if num > 1000:
                print >> sys.stderr, 'Arg debe ser menor a mil [%i]... no procesado' % (num)
            else:
                print '%i: %s' % (num, letras(num))
        except:
            print >> sys.stderr, 'Error [%s]... no procesado' % str_num 
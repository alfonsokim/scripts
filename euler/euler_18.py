'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 29/06/2011
@author: Alfonso Kim
'''

SOURCE_TRIANGLE = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''.strip()

TRIANGLE = [[int(v) for v in r.split(' ')] for r in [row for row in SOURCE_TRIANGLE.split('\n')]]

def e_18():
    for i in range(14, 0, -1):
        for j in range(i):
            #print 'S:%i: %s' % (TRIANGLE[i-1][j], TRIANGLE[i][j:j+3])
            TRIANGLE[i-1][j] += max(TRIANGLE[i][j:j+2])
    #print '\n'.join([str(n) for n in TRIANGLE])
    return TRIANGLE[0][0]


if __name__ == '__main__':
    print e_18()
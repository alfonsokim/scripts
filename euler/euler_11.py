'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 20/06/2011
@author: Alfonso Kim
'''

STR_MATRIX = '''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
'''.strip()



def q_11_diag_1():
    matrix = [[int(num) for num in line.split(' ')] for line in STR_MATRIX.split('\n')]
    def diag(x, y):
        #print '%i %i %i %i ' % (matrix[x][y], matrix[x+1][y+1], matrix[x+2][y+2], matrix[x+3][y+3])
        return matrix[x][y]*matrix[x+1][y+1]*matrix[x+2][y+2]*matrix[x+3][y+3]
    max = 0
    for x in range(20-3):
        for y in range(20-3):
            this_num = diag(x, y)
            if this_num > max:
                max = this_num
    return max

def q_11_diag_2():
    matrix = [[int(num) for num in line.split(' ')] for line in STR_MATRIX.split('\n')]
    def diag(x, y):
        #print x, y
        print 'x=%i y=%i %i %i %i %i ' % (x, y, matrix[x][y], matrix[x-1][y+1], matrix[x-2][y+2], matrix[x-3][y+3])
        return matrix[x][y]*matrix[x-1][y+1]*matrix[x-2][y+2]*matrix[x-3][y+3]
    max = 0
    for x in range(3, 19):
        for y in range(0, 16):
            this_num = diag(x, y)
            if this_num > max:
                max = this_num
    return max
                


def q_11_down():
    matrix = [[int(num) for num in line.split(' ')] for line in STR_MATRIX.split('\n')]
    max = 0
    for row in range(20):
        for col in range(20-3):
            this_num = matrix[col][row]*matrix[col+1][row]*matrix[col+2][row]*matrix[col+3][row]
            if this_num > max:
                max = this_num
    return max
    

def q_11_left():
    matrix = [[int(num) for num in line.split(' ')] for line in STR_MATRIX.split('\n')]
    left = lambda x,y: matrix[x][y:y+4]
    max = 0
    for i in range(20*20):
        row = int(i/20)
        col = int(i%20)
        if col <= 16:
            #print 'R[%i] C[%s] l=%s' % (row, col, left(row, col))
            this_max = reduce(lambda x,y: x*y, left(row, col))
            if this_max > max:
                max = this_max
    return max
    

def q_11_bad4():
    matrix = [int(num) for num in STR_MATRIX.split()]
    for row in range(20):
        for col in range(20):
            if col <= 16:
                #print left((row*20)+col)
                print 'r[%i] c[%i] i[%s]' % (row, col, [matrix[(col*20)+(row*n)] for n in range(4)])
                

def q_11_bad_2():
    matrix = [int(num) for num in STR_MATRIX.split()]
    for i in range(20):
        for j in range(20-3):
            left = lambda x: matrix[x:x+4]
            print 'i=%i j=%i, M=%s' % (i, j, left((i*20)+j))

def q_11_bad():
    matrix = [[int(num) for num in line.split(' ')] for line in STR_MATRIX.split('\n')]
    for i in range(20-3):
        for j in range(20-3):
            product = lambda x,y: x*y
            left = lambda x,y: matrix[x][y:y+4]
            down = lambda x,y: matrix[x][x*20]
            print 'i=%i j=%i, M=%s' % (i, j, down(i, j))

if __name__ == '__main__':
    #32719995
    #51267216
    #locura()
     
    left = q_11_left()
    down = q_11_down()
    diag_1 = q_11_diag_1()
    diag_2 = q_11_diag_2()
    print 'Left:%i' % left
    print 'Down:%i' % down
    print 'Diag1:%i' % diag_1
    print 'Diag2:%i' % diag_2
    
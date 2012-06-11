'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 22/06/2011
@author: Alfonso Kim
'''
        
grid_size = 2


class Path():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        


def route(path, step_x, step_y):
    n = 0
    if step_x < grid_size:
        if path.x != 0 or path.y != 0:
            print 'Regenerando path'
            path = Path(step_x, step_y)
        n += route(path, step_x+1, step_y)
    if step_y < grid_size:
        if path.x != 0 or path.y != 0:
            print 'Regenerando path'
            path = Path(step_x, step_y)
        n += route(path, step_y, step_y+1)
    if step_x == grid_size and step_y == grid_size:
        if path.x == 0 and path.y == 0:
            return 1
        else:
            return 0
    return n



def e_15(surfaces, grid_size, step_x, step_y):
    surface = (grid_size-step_x) * (grid_size-step_y)
    i = 0
    if not surface:
        return 1
    grid_name = '%i*%i' % (step_x, step_y)
    if not grid_name in surfaces:
        if step_x < grid_size:
            i += e_15(surfaces, grid_size, step_x+1, step_y)
        if step_y  < grid_size:
            i += e_15(surfaces, grid_size, step_x, step_y+1)
        surfaces[grid_name] = i
    return surfaces[grid_name]
    


def e_15_nana():
    path = Path(0, 0)
    print route(path, 0, 0)

if __name__ == '__main__':
    print e_15({}, 20, 0, 0)
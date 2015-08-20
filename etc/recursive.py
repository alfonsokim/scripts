import os

# ==================================================

def create(current, dir_list, depth):
    """ Crea una lista de directorios anidados
        :param current: El directorio actual
        :param dir_list: La lista de directorios a generar en cada directorios
        :param depth: El nivel en la estructura de la ejecucion actual
    """
    for a_dir in dir_list:
        new_path = os.path.join(current, a_dir)
        os.makedirs(new_path)
        print 'Path: %s, dirs: %s, depth: %i' % (new_path, str(dir_list), depth)
        if 1+depth < len(dir_list):
            create(new_path, dir_list, 1+depth)

# ==================================================

if __name__ == '__main__':
    """ Punto de entrada a la consola
    """
    create('/Volumes/R/', list('merol'), 0)

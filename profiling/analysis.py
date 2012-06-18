''' 
Created on 15/06/2012

@author: Alfonso Kim
'''

import sys, os
import numpy
import matplotlib.pyplot as plt

# ==================================================================
# ------------------------------------------------------------------

class Spec():
    ''' Representa el analisis de un archivo de tiempos '''
    
    def __init__(self, x, spec, average, std_dev, variance, total, min_n, max_n):
        ''' '''
        self.x = x
        self.spec = spec
        self.average = average
        self.std_dev = std_dev
        self.variance = variance
        self.total = total
        self.min_n = min_n
        self.max_n = max_n
        
    
    def __str__(self):
        ''' '''
        return 'spec:%s avg:%.3f std_dev:%.3f var:%.3f total:%i min:%.3f max:%.3f' % (
                self.spec, self.average, self.std_dev, self.variance, self.total, self.min_n, self.max_n)
        
    def legend(self):
        ''' '''
        return r'$\mu=%.2f,\ \sigma=%.2f$' % (self.average, self.std_dev)
    
    
    def label(self):
        ''' '''
        return 'Min:%.2f Max:%.2f' % (self.min_n, self.max_n)


# ==================================================================
# ------------------------------------------------------------------

def read_file(file_path, eval_code):
    ''' Lee un archivo y devuelve su representacion para la grafica
        @param file_path: Ruta al archivo
    '''
    in_file = open(os.path.abspath(file_path), 'r')
    first_line = in_file.readline()
    spec = first_line if first_line.strip()[0] == '#' else file_path
    data = [float(eval(eval_code)) for s in in_file]
    if spec == file_path:
        s = first_line
        data.insert(0, float(eval(eval_code)))
    sorted_data = sorted(data)
    return Spec(x=sorted_data,
                spec=spec, 
                average=numpy.average(data), 
                std_dev=numpy.std(data), 
                variance=numpy.var(data),
                total=len(data),
                min_n=sorted_data[0],
                max_n=sorted_data[-1])


# ===================================================================
# ------------------------------------------------------------------
def analysis(files, options):
    ''' '''
    specs = [read_file(file, options.eval) for file in files]
    for spec in specs:
        n, bins, patches = plt.hist(spec.x, facecolor='green', alpha=0.75, label=spec.label())
        plt.xlabel('Milisegundos')
        plt.ylabel('Frecuencia')
        plt.title(spec.spec)
        plt.text(1, 1-spec.max_n, spec.legend())
        plt.grid(True)
        plt.legend()
        plt.savefig('%s.png' % spec.spec.split('.')[0])
        #plt.show()

# ===================================================================
# ------------------------------------------------------------------
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser(usage='Procesa y grafica analisis de tiempos')
    parser.add_option('-e', '--eval',
                      dest='eval',
                      default='s',
                      metavar='EVAL',
                      help='Codigo a ejecutar para obtener el tiempo de la linea')
    options, args = parser.parse_args()
    if not args or len(args) == 0:
        parser.error('Especificar archivos')
    analysis(args, options)
'''
  Copyright (C) 2010-2011 Sm4rt Security Systems. 
                Todos los derechos reservados.

  La informacion y codigo fuente contenido en este archivo
  es propiedad exclusiva de Sm4rt Security Systems. Ninguna parte
  de este software puede ser usado, reproducido, almacenado o
  distribuido de  ninguna forma sin la autorizacion explicitamente
  escrita de Sm4rt Security Systems
---

Created on 27/06/2011
@author: Alfonso Kim
'''

TO_TEN = ['', 'ONE', 'TWO', 'THREE', 'FOUR', 
          'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN']
TO_TWENTY = ['', 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 
             'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN', 'TWENTY']
REST = ['', '', 'TWENTY', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def menor_a_100(i):
    string = ''
    if i <= 10:
        string = TO_TEN[i]
    elif i <= 20:
        string = TO_TWENTY[i%10]
        if i == 20:     # harcodeadisimo, pero ya estoy harto
            string = 'TWENTY'
    elif i < 100:
        idx = int(i/10)
        small = (i%10)
        string = '%s%s' % (REST[idx], TO_TEN[small])
    return string


def e_17(to):
    total = 0
    for i in range(1, to+1):
        if i < 100:
            total += len(menor_a_100(i))
        elif i < 1000:
            str_i = str(i)
            high = int(str_i[0])
            med = int(str_i[1])
            small = int(str_i[2])
            hundreds = menor_a_100(int(i%100))
            if len(hundreds):
                total_hundreds = '%s hundred and %s' % (TO_TEN[high], hundreds)
            else:
                total_hundreds = '%s hundred' % (TO_TEN[high])
            print 'i=%i (%i, %i, %i) [%s]' % (i, high, med, small, total_hundreds)
            total += len(total_hundreds.replace(' ', ''))
        elif i == 1000:
            total += len('onethousand')
        else:
            print 'WTF [%s]' % (i)
    return total


if __name__ == '__main__':
    print e_17(1000)
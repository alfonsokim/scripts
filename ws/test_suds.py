
# import suds.bindings.binding as b
# print 'Antes: %s' % str(b.envns)
# b.envns = ('SOAP-ENV', 'http://www.w3.org/2003/05/soap-envelope/')
#print 'Despues: %s' % str(b.envns)

from suds.client import Client

client = Client('https://servicios.publipayments.com/Servicios.svc?wsdl', 
                location='https://servicios.publipayments.com/Servicios.svc')

print client.service.Echo()
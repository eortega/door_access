#!/usr/bin/python

import sys
from request import verify_customer


if len(sys.argv) == 3:
    response=  verify_customer("url", sys.argv[2])

     #print response

    if(response):
        if(response['status']== True):
            print 'Abrir la puerta'
        else:
            print 'rojito de no  puede pasar'
    else:
        print 'Encender el rojito de no puede pasar'

else:
    print 'Parametros insuficientes'

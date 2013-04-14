#!/usr/bin/python

import sys
from request import verify_customer
import doors as DOORS

if len(sys.argv) == 3:
    response=  verify_customer("url", sys.argv[2])

     #print response

    if(response):
        if(response['status']== True):
            DOORS.open_(25)
        else:
            DOORS.warning_(24)
    else:
        DOORS.warning_(24)

else:
    print 'Parametros insuficientes'

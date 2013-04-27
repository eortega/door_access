#!/usr/bin/python

import sys
from request import verify_customer
import doors as DOORS

print("Pi Door Acces Started")

while True:
    code=raw_input("pass card:")
    response=  verify_customer("url", code)

    #print response

    if(response):
        if(response['status']== True):
            DOORS.open_(25)
        else:
            DOORS.warning_(24)
    else:
        print("Server not found")
        DOORS.warning_(24)

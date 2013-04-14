from urllib2 import urlopen
from urllib2 import HTTPError
from urllib2 import URLError
import json

def verify_customer(url, credencial):  

    
    mi_url = "http://192.168.1.86/pachanguitos/web/api/view/model/cliente/id/"
    mi_url+=credencial
    mi_url+="/servicio/16"

    try:
        response = urlopen(mi_url)
        data = json.loads(response.read())
        return  data
    except HTTPError, err:
        if err.code == 404:
            print 'Page not found!'
        elif err.code == 403:
            print 'Access denied'
        else:
            print 'Ha sucedido un error:',err.code
        return False
    except URLError, err:
        print "Paso algun error con codigo:", err.reason
        return False
        

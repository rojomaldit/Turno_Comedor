# importing the requests library 
import requests 
import json
from bs4 import BeautifulSoup
import urllib2
import requests
import sys
import re
import random
import string

session = requests.Session()

#Get dates
URL = 'http://comedor.unc.edu.ar/reserva/'

page = urllib2.urlopen(URL)
soup = BeautifulSoup(page, 'html.parser')

cstoken = soup.find('input', attrs={'id': 'cstoken'})['value']
form = str(soup.find('form', attrs={'id': 'formulario_toba'})['action'])
ah = form.split('&')[0].split('=')[1]
ai = form.split('&')[1].split('=')[1]

path = URL + "aplicacion.php?" + "ah=" + ah + "&ai=" + ai
#print(cstoken, ah, ai, path)
  
# api-endpoint 

boundary = "----WebKitFormBoundary" + ''.join(random.choice(string.ascii_uppercase + string.digits +  string.ascii_lowercase) for _ in range(16))
user = "0475D9542DE289D"

login_data = "--" + boundary + "\nContent-Disposition: form-data; name=\"cstoken\"\n\n" + cstoken  + "\n--" + boundary + "\nContent-Disposition: form-data; name=\"form_2689_datos\"\n\n" + "ingresar" + "\n--" + boundary  + "\nContent-Disposition: form-data; name=\"form_2689_datos_implicito\"\n\n" + "\n--" + boundary  + "\nContent-Disposition: form-data; name=\"ef_form_2689_datosusuario\"\n\n" + user + "\n--" + boundary  + "--"
print(login_data)
query_str_params = {
    'ah' : ah,
    'ai' : ai,
}

form_data = {
    'cstoken' : cstoken,
    'form_2689_datos' : 'ingresar',
    'form_2689_datos_implicito' : '',
    'ef_form_2689_datosusuario' : user1
}

response = session.request("POST", URL + path, data = login_data, headers = {'cache-control': "no-cache", 'Content-Type' : "multipart/form-data; boundary=" + boundary})
data = response.text
print(data)

r = requests.post(url = URL, data = form_data)
#print(r.text)

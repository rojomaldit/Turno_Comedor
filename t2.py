# importing the requests library 
import requests 
import json
from bs4 import BeautifulSoup
import urllib2
import requests

#Get dates
URL = "http://comedor.unc.edu.ar/reserva"

page = urllib2.urlopen(URL)
soup = BeautifulSoup(page, 'html.parser')

cstoken = soup.find('input', attrs={'id': 'cstoken'})["value"]
form = str(soup.find('form', attrs={'id': 'formulario_toba'})['action'])
ah = form.split('&')[0].split('=')[1]
ai = form.split('&')[1].split('=')[1]
print(cstoken, ah, ai)
  
# api-endpoint 

boundary = "16216400248655893201210934546"
user = "0475D9542DE289D"

login_data = "--" + boundary + "\nContent-Disposition: form-data; name=\"cstoken\"\n\n" + cstoken  + "\n--" + boundary + "\nContent-Disposition: form-data; name=\"form_2689_datos\"\n\n" + "ingresar" + "\n--" + boundary  + "\nContent-Disposition: form-data; name=\"form_2689_datos_implicito\"\n\n" + "\n--" + boundary  + "\nContent-Disposition: form-data; name=\"ef_form_2689_datosusuario\"\n\n" + user + "\n--" + boundary  + "--"


data = {
    'ah': ah,
    'ai': ai,
    'value': user,
}


r = requests.post(url = URL, data = data)
print(r.text)
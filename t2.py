# importing the requests library 
from bs4 import BeautifulSoup
import requests
import string

session = requests.Session()

def get_data(response):
    soup = BeautifulSoup(response.text,'html.parser')
    cstoken = soup.find('input',attrs={'id':'cstoken'})['value']
    form = str(soup.find('form',attrs={'id':'formulario_toba'})['action'])
    ah = form.split('&')[0].split('=')[1]
    ai = form.split('&')[1].split('=')[1]
    path = URL+"aplicacion.php?"+"ah="+ah+"&ai="+ai
    return ah, ai, path, cstoken

# Dates of the page
URL = 'http://comedor.unc.edu.ar/reserva/'
page = session.request("GET",URL+"/",data="",headers={'cache-control':"no-cache"})

###IMPORTANT DATA FOR USERS###
ah, ai, path, cstoken = get_data(page)
boundary = "----WebKitFormBoundary"+"8913455937355731132109892795"
users = "0475D9542DE289D"

cd = "\nContent-Disposition: form-data;"
login_data ="--"+boundary+cd+"name=\"cstoken\"\n\n"+cstoken+"\n--"+boundary+cd+"name=\"form_2689_datos\"\n\n"+"ingresar"+"\n--"+boundary+cd+"name=\"form_2689_datos_implicito\"\n\n"+"\n--"+boundary+cd+"name=\"ef_form_2689_datosusuario\"\n\n"+users+"\n--"+boundary+"--"

#LOGIN
response = session.request("POST",path,data=login_data,headers={'cache-control':"no-cache",'Content-Type':"multipart/form-data;boundary="+boundary})
data = response.text

#RESERVATION
ah, ai, path, cstoken = get_data(response)
reservarion_data = "--"+boundary+"\nContent-Disposition:form-data;name=\"cstoken\"\n\n"+cstoken+"\n--"+boundary+"\nContent-Disposition:form-data;name=\"ci_2695\"\n\n"+"procesar"+"\n--"+boundary+"\nContent-Disposition:form-data;name=\"ci_2695__param\"\n\n"+"undefined"+"\n--"+boundary+"--"

response = session.request("POST",path,data=reservarion_data,headers={'cache-control':"no-cache",'Content-Type':"multipart/form-data;boundary="+boundary})

#FIND ALERT
soup = BeautifulSoup(response.text,'html.parser')
alert = str(soup.find('script',attrs={'language':'JavaScript'})).split('alert')[1].split(';')[0]
print(alert)
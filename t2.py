# importing the requests library 
import requests 
import json
  
# api-endpoint 
URL = "http://comedor.unc.edu.ar/reserva"

boundary = "16216400248655893201210934546"
token = "BEeuMPwSHLe5dCrGhi7W6fiK0VWW1sQjb2nmrFwqw5o="
user = "0475D9542DE289D"

login_data = "--" + boundary + "\nContent-Disposition: form-data; name=\"cstoken\"\n\n" + token  + "\n--" + boundary + "\nContent-Disposition: form-data; name=\"form_2689_datos\"\n\n" + "ingresar" + "\n--" + boundary  + "\nContent-Disposition: form-data; name=\"form_2689_datos_implicito\"\n\n" + "\n--" + boundary  + "\nContent-Disposition: form-data; name=\"ef_form_2689_datosusuario\"\n\n" + user + "\n--" + boundary  + "--"


data = {
    'ah':'st5d5963a74a6a18.86069042',
    'ai': 'migestion||3614',
}


r = requests.post(url = URL, data = data, headers=hee)
print(r.text)

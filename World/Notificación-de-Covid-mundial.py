# !/usr/bin/env python3
# Notificador de escritorio construido para actualizaciones de la pandemia de covid en el mundo
# Hecho por traditionallimb  - Refinado y partes agregadas por Callum Disney
# Hecho 10.11.20
# Refinado y piezas añadidas 04.01.21




# Las importaciones necesitan dependencias.
import datetime
import time
import requests
from plyer import notification

covidData = None
try:
  covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/World/")
except:
  print("Please check your internet connection!")

if (covidData != None):
    # Convierte datos en formato JSON
    data = covidData.json()['Success']

    # Repite el ciclo para siempre / hasta que el código se detenga
    while(True):
        notification.notify(
            # El título de la notificación
            title = "Estadísticas mundiales de COVID-19 hoy ({})".format(datetime.date.today()),
            # El cuerpo de la notificación
            message = "Total de Casos: {totalDeCasos}\nCasos de Hoy: {casosDeHoy}\nMuertes de Hoy: {muertesDeHoy}\nCasos Críticos: {casosCríticos}".format(
                        totalDeCasos = data['cases'],
                        casosDeHoy = data['todayCases'],
                        muertesDeHoy = data['todayDeaths'],
                        casosCríticos = data["critical"]),
            app_icon = "", # Si desea tener un icono personalizado, coloque la ruta a su icono entre las comas (""). ¡Asegúrese de que sea un archivo .ico!
            timeout  = 50
        )

        # La notificación se repite cada 4 horas
        time.sleep(60*30) # (Dormir durante 4 horas => 60 * 60 * 4 seg)

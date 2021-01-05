# !/usr/bin/env python3
# Desktop notifier built for updates for the covid pandemic in Russia
# Made by traditionallimb - Refined and parts added by Callum Disney
# Made 10.11.20
# Refined and parts added 04.01.21




# Imports need dependencies.
import datetime
import time
import requests
from plyer import notification

covidData = None
try:
  covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/Russia/")
except:
  print("Please check your internet connection!")

if (covidData != None):
    # Converts data into JSON format
    data = covidData.json()['Success']

    # Repeats the loop forever/until code stopped
    while(True):
        notification.notify(
            # The title of the notification
            title = "Russia COVID-19 Stats today ({})".format(datetime.date.today()),
            # The body of the notification
            message = "Total Cases: {totalCases}\nToday\'s Cases: {casesToday}\nToday\'s Deaths: {deathsToday}\nCritical Cases: {criticalCases}".format(
                        totalCases = data['cases'],
                        casesToday = data['todayCases'],
                        deathsToday = data['todayDeaths'],
                        criticalCases = data["critical"]),
            app_icon = "", # If you wish to have a custom icon, put the path to your icon in between the inverted commas (""). Make sure it's a .ico file!
            # The notification will stay for 50 seconds unless dismissed
            timeout  = 50
        )

        # Notification repeats after every 4 hours
        time.sleep(60*30) # (Sleep for 4 hours => 60*60*4 sec)

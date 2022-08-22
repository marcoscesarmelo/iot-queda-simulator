import requests
from datetime import datetime
import random
import time
from datetime import date

thingsboard_server = "http://34.170.18.196:8080"
thingsboken = "ESP32-hb-sim"
last_time_sent = ''

while True:
    #ATRIBUI VALORES RANDOMICOS PARA EIXOS
    time.sleep(3)
    hb=round(random.uniform(60,130),1)
    date_hour_now = datetime.now()
    formatted_datetime = date_hour_now.strftime('%Y-%m-%dT%H:%M:%S')
    print("Now is: " + formatted_datetime)
    dados_payload = {
        'hb': hb,
        'date': formatted_datetime
    }
    send_data = requests.post(thingsboard_server+'/api/v1/'+thingsboard_token+'/telemetry', json=dados_payload)

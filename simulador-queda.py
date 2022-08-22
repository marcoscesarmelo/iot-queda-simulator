import requests
from datetime import datetime
import random
import time
from datetime import date

thingsboard_server = "http://34.170.18.196:8080"
thingsboard_token = "simulator-iot-esp32"
last_time_sent = ''

while True:
    #ATRIBUI VALORES RANDOMICOS PARA EIXOS
    time.sleep(3)
    x_axis = round(random.uniform(-2,2),1)
    y_axis = round(random.uniform(-2,2),1)
    z_axis = round(random.uniform(-2,2),1)

    print("X: " + str(x_axis) + " Y: " + str(y_axis) + " Z: " + str(z_axis))
    date_hour_now = datetime.now()
    formatted_datetime = date_hour_now.strftime('%Y-%m-%dT%H:%M:%S')
    print("Now is: " + formatted_datetime)
    if(z_axis >= 1 and last_time_sent != date.today()):
        #ENVIA AO THINGSBOARD:
        print("Sending to THINGSBOARD ...")
        dados_payload = {
            'x_axis': x_axis,
            'y_axis': y_axis,
            'z_axis': z_axis,
            'date': formatted_datetime
        }
        print(dados_payload)
        print(thingsboard_server+'/api/v1/'+thingsboard_token+'/telemetry')
        send_data = requests.post(thingsboard_server+'/api/v1/'+thingsboard_token+'/telemetry', json=dados_payload)
        print("Status code: ", send_data.status_code)
        if(send_data.status_code ==  200):
          last_time_sent = date.today()

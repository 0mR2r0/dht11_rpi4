#Programa de para sensor de humedad y temperatura dht11
#Biblioteca usada es: pip install adafruit-circuitpython-dht
#Programacion basada en https://RandomNerdTutorials.com/raspberry-pi-dht11-dht22-python/
#Se usa la configuracion del BOARD del GPIO de RPi4 / Verifique los pines antes de conectar 

import time
import board
import adafruit_dht

#Tipo de sensor
sensor = adafruit_dht.DHT11(board.D18)

while True:
        try:
                #Muestra los valores del puerto serial
                temperatura=sensor.temperature
                humedad=sensor.humidity
                #resultado='{:.2f}'.format(temperatura)
                #print (resultado)
                print ('T={0:0.1f}ºC, H={1:0.1f}%'.format(temperatura, humedad))
        except RuntimeError as error:
                print (error.args[0])
                time.sleep(2)
                continue
        time.sleep(3)


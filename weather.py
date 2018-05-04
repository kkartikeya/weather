#!/usr/bin/python

import configparser
import urllib.request, urllib.error
import json
import pika
from com.kkartikeya.home.weather.weather_pb2 import Weather

CONFIG_FILE_PATH='/Users/kk/work/personal/github.com/configuration/config.properties'
SAN_JOSE_LAT='37.340576'
SAN_JOSE_LONG='-121.894922'
WeatherService='OPENWEATHER'  # OPENWEATHER or DARKSKY

OPENWEATHER_APISCHEME='https://'
OPENWEATHER_APIHOST=OPENWEATHER_APISCHEME+'api.openweathermap.org'
OPENWEATHER_BASE_URI=OPENWEATHER_APIHOST+'/data/2.5'
OPENWEATHER_CurrentConditionsURI=OPENWEATHER_BASE_URI+'/weather'

#api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID=1111111111&units=imperial

def getAMQPURL():
	config=configparser.RawConfigParser()
	config.read(CONFIG_FILE_PATH)

	return config.get('Messaging', 'CLOUDAMQP_URL')

def getAPIKey():
    config=configparser.RawConfigParser()
    config.read(CONFIG_FILE_PATH)

    return config.get('Weather', WeatherService+'_API_KEY')

def getOpenWeatherCurrentCondition():
    URL= OPENWEATHER_CurrentConditionsURI+'?lat='+SAN_JOSE_LAT+'&lon='+SAN_JOSE_LONG+'&APPID='+getAPIKey()+'&units=imperial'
    httprequest=urllib.request.Request(URL)

    try:
        response=urllib.request.urlopen(httprequest)
        responseJson=response.read().decode('utf-8')
        return responseJson
    except (urllib.error.URLError, urllib.error.HTTPError) as err:
        print(err.reason)

def getDarkWeatherCurrentCondition():
	print('DarkSky')

def getCurrentWeather():
	currentWeather=Weather()
	if WeatherService=='OPENWEATHER':
		currentWeatherResponse=getOpenWeatherCurrentCondition()
		currentWeatherJson=json.loads(currentWeatherResponse)
		currentWeather.timestamp=currentWeatherJson.get('dt')
		currentWeather.temp=currentWeatherJson.get('main').get('temp')
		currentWeather.humidity=currentWeatherJson.get('main').get('humidity')
		currentWeather.windspeed=currentWeatherJson.get('wind').get('speed')
		currentWeather.cloud=currentWeatherJson.get('clouds').get('all')
		currentWeather.sunrise=currentWeatherJson.get('sys').get('sunrise')
		currentWeather.sunset=currentWeatherJson.get('sys').get('sunset')
	elif WeatherService=='DARKSKY':
		print('DarkSky')
	return currentWeather.SerializeToString()

def publishToAMQP(queue, exchange, routing_key, message):
    AMQPURL=getAMQPURL()
    params = pika.URLParameters(AMQPURL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel
    channel.queue_declare(queue) # Declare a queue
    channel.basic_publish(exchange,
                          routing_key,
                          message)
    connection.close()

def main():
	currentWeather=getCurrentWeather()
	queue='weather'
	exchange='weather'
	routing_key='current'
	publishToAMQP(queue, exchange, routing_key, currentWeather)

if __name__ == "__main__":
	main()

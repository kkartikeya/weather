#!/usr/bin/python

import configparser
import urllib.request, urllib.error
import json
import weather_pb2.py

CONFIG_FILE_PATH='/Users/kk/work/personal/github.com/configuration/config.properties'
SAN_JOSE_LAT='37.340576'
SAN_JOSE_LONG='-121.894922'
WeatherService='OPENWEATHER'

OPENWEATHER_APISCHEME='https://'
OPENWEATHER_APIHOST=OPENWEATHER_APISCHEME+'api.openweathermap.org'
OPENWEATHER_BASE_URI=OPENWEATHER_APIHOST+'/data/2.5'
OPENWEATHER_CurrentConditionsURI=OPENWEATHER_BASE_URI+'/weather'

#api.openweathermap.org/data/2.5/weather??lat={lat}&lon={lon}&APPID=1111111111&units=metric

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

def getCurrentWeather():
    if WeatherService=='OPENWEATHER':
        currentWeatherResponse=getOpenWeatherCurrentCondition()
        currentWeatherJson=json.loads(currentWeatherResponse)
        print(currentWeatherJson.get('main').get('temp'))
        print(currentWeatherJson.get('main').get('humidity'))
        print(currentWeatherJson.get('wind').get('speed'))
        print(currentWeatherJson.get('clouds').get('all'))
        print(currentWeatherJson.get('dt'))
        print(currentWeatherJson.get('sys').get('sunrise'))
        print(currentWeatherJson.get('sys').get('sunset'))


def main():
    getCurrentWeather()

if __name__ == "__main__":
	main()

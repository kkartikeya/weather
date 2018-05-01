#!/usr/bin/python

import configparser

CONFIG_FILE_PATH='/Users/kk/work/personal/github.com/configuration/config.properties'
WEATHERSERVICE='OPENWEATHER'

def getAMQPURL():
	config=configparser.RawConfigParser()
	config.read(CONFIG_FILE_PATH)

	return config.get('Messaging', 'CLOUDAMQP_URL')

def getAPIKey():
    config=configparser.RawConfigParser()
    config.read(CONFIG_FILE_PATH)

    return config.get('Weather', WEATHERSERVICE+'_API_KEY')

def main():
    print(getAMQPURL())
    print(getAPIKey())

if __name__ == "__main__":
	main()

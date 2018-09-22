#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import json
import urllib.request



 # URL ask for geographic information
 
 
 # # get stream in return (JSON stream) - make it an object. Deseralize JSON (list, dictionary)
 # return temperature, etc
 
 # send data to giannis. calling URL


def time_converter():
    converted_time = datetime.datetime.now().strftime('%I:%M %p')
    return converted_time


def url_builder(geoX,geoY):
    user_api = '14bb2f82a98398dc88df2d0bdb338538'  # Obtain yours form: http://openweathermap.org/
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    api = 'http://api.openweathermap.org/data/2.5/weather?lat='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

# api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon} 



    full_api_url = api + str(geoY) + '&lon=' + str(geoX) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url


def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data


def data_output(data):
    m_symbol = '\xb0' + 'C'
    print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('---------------------------------------')
    iTemp = data['temp']
    fWindSpeed = data['wind']
    fHumidity = data['humidity']
    fCloud = data['cloudiness']
    fPressure = data['pressure']
    sSky = data['sky']
    
    lWeatherData = [iTemp , fWindSpeed , fHumidity , fCloud , fPressure , sSky]
    
    return lWeatherData
    

geoX = 21.781894
geoY = 36.919710
data_output(data_organizer(data_fetch(url_builder(geoX,geoY))))


        

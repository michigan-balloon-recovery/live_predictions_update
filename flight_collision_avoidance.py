#!/usr/bin/python

import sys
from suds import null, WebFault
from suds.client import Client
import logging

username = 'fortmcas'
apiKey = '113dbde052d45892c914639637c8a6a41913ba6e'
url = 'http://flightxml.flightaware.com/soap/FlightXML2/wsdl'

logging.basicConfig(level=logging.INFO)
api = Client(url, username=username, password=apiKey)
#print api

def get_api_data(latitude, longitude, altitude_feet, delta_miles, delta_feet):
    delta_degrees = delta_miles/69.0
    min_lat = str(latitude - delta_degrees)
    max_lat = str(latitude + delta_degrees)
    min_long = str(longitude - delta_degrees)
    max_long = str(longitude + delta_degrees)
    min_alt = str((altitude_feet - delta_feet)/100)
    max_alt = str((altitude_feet + delta_feet)/100)


    search_string = "{range lat " + min_lat + " " + max_lat + "} {range lon "\
    + min_long + " " + max_long + "} {< alt " + max_alt + "} {> alt " + min_alt\
    + "}"

    print search_string
    result = api.service.SearchBirdseyeInFlight(search_string, 15, 0)
    return  result

import json
import requests
import numpy as np

callsign = "P0520293"

# get JSON data from APRS
json_response= requests.get("http://api.aprs.fi/api/get?name="+callsign+"&what=loc&apikey=42457.M4AFa3hdkXG31&format=json")
aprs_dict = json.loads(json_response.text)

#np.float()

APRSaltitude = np.float(aprs_dict['entries'][0]['altitude'])#m
APRSlat = np.float(aprs_dict['entries'][0]['lat']) 
APRSlon = np.float(aprs_dict['entries'][0]['lng'])
APRSlasttime = np.float(aprs_dict['entries'][0]['lasttime']) 

print(str(APRSlat)+","+str(APRSlon)+","+str(APRSaltitude)+","+str(APRSlasttime))

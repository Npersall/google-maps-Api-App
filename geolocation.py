import httplib2
import json

def getGeoLocation(inputString):
    google_api_key = "AIzaSyCijUeimMV3MPDc_4jX4Q_zHQKjRdS60p0"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = httplib2.Http()
    resonse, content = h.request(url, 'GET')
    result = json.loads(content)
    latitude = result['results'] [0] ['geometry'] ['location']['lat']
    longitude = result['results'] [0] ['geometry'] ['location']['lng']
    return (latitude, longitude)
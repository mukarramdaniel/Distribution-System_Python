import googlemaps
import math

def distance_between_places(lat1, lon1, lat2, lon2):
  R = 6371 
  lati = math.radians(lat2-lat1)
  longi = math.radians(lon2-lon1)
  a = math.sin(lati/2) * math.sin(lati/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(longi/2) * math.sin(longi/2)
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
  d = R * c 
  return d
############################################

API_key = 'AIzaSyBebwTrA8E0hXbyw8R2dUQRTFOg7q517U0'
map_client = googlemaps.Client(API_key)

def get_place_info(Location_name) :
    #location_name = "Abdul Samad Printing Point"
    response1 = map_client.places(query=Location_name)
    results = response1.get('results')[0]
    return results
def getLocation(Location_name):
    result = get_place_info(Location_name)
    address=result['formatted_address']
    coordinates=(result['geometry'])['location']
    lati=coordinates['lat']
    longi=coordinates['lng']
    return(address,lati,longi)

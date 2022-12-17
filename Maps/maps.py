import googlemaps
import math

def distance_between_places(lat1, lon1, lat2, lon2):
  R = 6371  # Radius of the Earth in kilometers
  dlat = math.radians(lat2-lat1)
  dlon = math.radians(lon2-lon1)
  a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
  d = R * c  # Distance in kilometers
  return d




API_key = 'AIzaSyBebwTrA8E0hXbyw8R2dUQRTFOg7q517U0'
map_client = googlemaps.Client(API_key)

#is m location do wo uski info de de ga 
#using geocode
work_place = "Shell, Khan Pur Road, Liaquatpur Rd, Liāqatpur, Rahim Yar Khan, Punjab 64000, Pakistan"
response = map_client.geocode(work_place)
#latitude lognitude info
loc = response[0]["geometry"]
Location = (loc['location'])
latitude = (Location['lat'])
longitude = (Location['lng'])
#To get Complete Address according to google maps
'''address = (response[0]["address_components"])'''


#same kaam with .places
def get_place_info(Location_name) :
    #location_name = "Abdul Samad Printing Point"
    response1 = map_client.places(query=Location_name)
    results = response1.get('results')[0]
    return results

result = get_place_info("Abdul Samad Printing Point")



# Test the function
lat1 = latitude#31.58060073946487, 74.35624319553045
lon1 = longitude
lat2 = 31.58060073946487
lon2 = 74.35624319553045
print(distance_between_places(lat1, lon1, lat2, lon2))  # Output: 2874.55951523
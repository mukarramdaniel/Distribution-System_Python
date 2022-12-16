import googlemaps


API_key = 'AIzaSyBebwTrA8E0hXbyw8R2dUQRTFOg7q517U0'
map_client = googlemaps.Client(API_key)

#is m location do wo uski info de de ga 
#using geocode
work_place = "Gloria Jean's Coffees Hali Road"
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
#print(result)
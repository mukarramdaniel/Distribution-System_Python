import googlemaps
import folium
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow

# Set the API key for the Google Maps client
api_key = 'AIzaSyBebwTrA8E0hXbyw8R2dUQRTFOg7q517U0'

# Set the starting and ending points for the route
start = (float(31.57714030411648), float(74.35603665613657))
end = (float(31.577244438074196), float(74.358372424896))

# Set the waypoints for the route (optional)
waypoints = [(float(31.57552403504949), float(74.35429530639927)), (float(31.55043477797966), float(74.31304116179827))]

# Create a Google Maps client
gmaps = googlemaps.Client(key=api_key)

# Call the Google Maps Directions API to retrieve the route
route = gmaps.directions(start, end, waypoints=waypoints, mode='driving')

# Extract the polyline from the route and decode it
polyline = route[0]['overview_polyline']['points']
path = googlemaps.convert.decode_polyline(polyline)
path1=[]
for i in path:
    coord_list = [(lng, lat) for lng, lat in i.items()]
    path1.append((coord_list[0][1],coord_list[1][1]))
# Create a Map object
m = folium.Map()

# Add the route to the map
folium.PolyLine(path1, color='red', weight=3, opacity=0.5).add_to(m)

# Save the map to an HTML file
m.save('map.html')

# Create a QApplication and a QMainWindow
app = QApplication([])
window = QMainWindow()

# Create a QWebEngineView widget and set it as the central widget of the window
view = QWebEngineView()
window.setCentralWidget(view)

# Load the map HTML file into the QWebEngineView
view.load(QUrl.fromLocalFile('map.html'))

# Show the window
window.show()

# Run the Qt event loop
app.exec_()

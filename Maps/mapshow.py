import sys
from PyQt5.QtCore import QUrl
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView 
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
import googlemaps
import folium
import jinja2

class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QWebEngineView widget and set it as the central widget
        # of the main window
        self.webview = QWebEngineView(self)
        self.setCentralWidget(self.webview)
        locations = [
            (40.7128, -74.0060),  # New York City
            (34.0522, -118.2437), # Los Angeles
        ]
        gmaps = googlemaps.Client("AIzaSyBebwTrA8E0hXbyw8R2dUQRTFOg7q517U0")

        # Use the directions() method to retrieve the road route between the locations
        result = gmaps.directions(locations[0], locations[1])

        # Extract the polyline from the result
        polyline = result[0]['overview_polyline']['points']
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
        path = [
        {'lat': 31.58060073946487, 'lng': 74.35624319553045},
        {'lat': 31.573996, 'lng': 74.345461},
        {'lat': 31.573996, 'lng': 74.345461},
        {'lat': 31.578237, 'lng': 74.360331}
        ]

# Load the HTML template
        template = jinja2.Template(html)

        # Render the template with the list passed as a variable
        output = template.render(path=path)
        

        # Load a map from the Google Maps API
        #self.webview.load(QUrl('https://maps.google.com/'))
        html='''
        <html>
          <head>
            <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBebwTrA8E0hXbyw8R2dUQRTFOg7q517U0"></script>
            <script>
              function initMap() {
                var map = new google.maps.Map(document.getElementById('map'), {
                  zoom: 100,
                  center: {lat: 31.58060073946487, lng: 74.35624319553045}
                });

                var path = [
                  {lat: 31.58060073946487, lng: 74.35624319553045},
                  {lat: 31.573996, lng: 74.345461},
                  {lat: 31.573996, lng: 74.345461},
                  {lat: 31.578237, lng: 74.360331}
                  
                ];

                var pathCoordinates = [];
                for (var i = 0; i < path.length; i++) {
                  pathCoordinates.push(new google.maps.LatLng(path[i].lat, path[i].lng));
                }

                var pathLine = new google.maps.Polyline({
                  path: pathCoordinates,
                  strokeColor: '#FF0000',
                  strokeOpacity: 1.0,
                  strokeWeight: 2
                });

                pathLine.setMap(map);
              }
              window.onload = initMap;
            </script>
          </head>
          <body>
            <div id="map" style="width:600px;height:400px;"></div'''
        self.webview.setHtml(html)
        

if __name__ == '__main__':
    app = QApplication(os.sys.argv)
    window = MapWindow()
    window.show()
    os.sys.exit(app.exec_())





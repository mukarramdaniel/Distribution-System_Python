import sys
from PyQt5.QtCore import QUrl
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView 
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
import googlemaps


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        self.webview = QWebEngineView(self)
        self.setCentralWidget(self.webview)
        # locations = [
        #     (40.7128, -74.0060)
        #     (34.0522, -118.2437)
        # ]
        gmaps = googlemaps.Client("AIzaSyBebwTrA8E0hXbyw8R2dUQRTFOg7q517U0")

        #result = gmaps.directions(locations[0], locations[1])

        #polyline = result[0]['overview_polyline']['points']

        html='''
        <html>
          <head>
            <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBebwTrA8E0hXbyw8R2dUQRTFOg7q517U0"></script>
            <script>
              function initMap() {
                var map = new google.maps.Map(document.getElementById('map'), {
                  zoom: 20,
                  center: {lat: 31.58060073946487, lng: 74.35624319553045}
                });

                var path = [
                  {lat: 31.58060073946487, lng: 74.35624319553045},
                  {lat: 31.573996, lng: 74.345461},
                  {lat: 31.578237, lng: 74.360331}
                  
                ];

                var pathCoordinates = [];
                for (var i = 0; i < path.length; i++) {
                  pathCoordinates.push(new google.maps.LatLng(path[i].lat, path[i].lng));
                }

                var pathLine = new google.maps.Polyline({
                  path: pathCoordinates,
                  strokeColor: '#004300',
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



 
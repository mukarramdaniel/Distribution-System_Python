import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWebEngineView

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    # Set up the QWebEngineView widget
    self.view = QWebEngineView(self)
    self.view.setHtml('''
      <html>
        <head>
          <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>
          <script>
            function initMap() {
              var map = new google.maps.Map(document.getElementById('map'), {
                zoom: 8,
                center: {lat: 52.2296756, lng: 21.0122287}
              });

              var path = [
                {lat: 52.2296756, lng: 21.0122287},
                {lat: 41.89193, lng: 12.51133},
                {lat: 48.856614, lng: 2.3522219},
                {lat: 51.507351, lng: -0.127758}
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
          </script>
        </head>
        <body>
          <div id="map" style="width:600px;height:400px;"></div

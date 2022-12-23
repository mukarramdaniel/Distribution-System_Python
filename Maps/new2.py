import googlemaps
import folium
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow

api_key = 'AIzaSyBebwTrA8E0hXbyw8R2dUQRTFOg7q517U0'
start = (float(31.57714030411648), float(74.35603665613657))
end = (float(31.577244438074196), float(74.358372424896))
waypoints = [(float(31.57552403504949), float(74.35429530639927)), (float(31.55043477797966), float(74.31304116179827))]
gmaps = googlemaps.Client(key=api_key)
route = gmaps.directions(start, end, waypoints=waypoints, mode='driving')
polyline = route[0]['overview_polyline']['points']
path = googlemaps.convert.decode_polyline(polyline)
path1=[]
for i in path:
    coord_list = [(lng, lat) for lng, lat in i.items()]
    path1.append((coord_list[0][1],coord_list[1][1]))
m = folium.Map(location=[ 31.57714030411648,74.35603665613657],zoom_start=1000)
folium.Marker(location=[31.57714030411648,74.35603665613657], popup="New York City").add_to(m)
folium.PolyLine(path1, color='red', weight=3, opacity=0.5).add_to(m)
m.save('map.html')
app = QApplication([])
window = QMainWindow()
webview = QWebEngineView()
window = QMainWindow()
window.setCentralWidget(webview)
webview.load(QUrl.fromLocalFile(os.path.abspath('map.html')))
window.show()
app.exec_()

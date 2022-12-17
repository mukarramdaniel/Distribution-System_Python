import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEnginePage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
import googlemaps
class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the QWebEngineView to display a map
        self.view = QWebEngineView(self)
        self.view.setGeometry(0, 0, 800, 600)
        self.view.setUrl(QUrl('http://www.google.com/maps/'))
    
       
        
        
        # Set up the mouse click event handler
        self.view.mousePressEvent = self.get_location   

    def get_location(self, event):
        # Check if the left mouse button was clicked
        if event.button() == Qt.LeftButton:
            # Get the coordinates of the click
            x = event.pos().x()
            y = event.pos().y()

            # Use the coordinates to get the location from the map
            # (Note: This will depend on the map provider and may require additional code)
            #location = get_location_from_coordinates(x, y)
            print(x,y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec_())










# import os
# from PyQt5.QtCore import QUrl
# from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QVBoxLayout
# from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEnginePage
# from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
# import googlemaps
# import PyQt5

# class MapWidget(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Create a QWebEngineView widget and set it to display a map
#         self.web_view = QWebEngineView()
#         self.web_view.setUrl(QUrl('https://www.google.com/maps/'))

#         # Set up the layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.web_view)
#         self.setLayout(layout)

#         # Set up a signal to be emitted when the map is clicked
#         self.web_view.page().runJavaScript('document.addEventListener("click", function(event) {emit_signal("clicked");});')
#         self.web_view.page().runJavaScript('function emit_signal(signal) {py.emit_signal(signal);}')
#         self.web_view.page().runJavaScript('py = PyQt5.QtWebEngineWidgets.QWebEnginePage.Signal(str)')
#         self.web_view.page().runJavaScript('py.connect(function (signal) {PyQt5.QtCore.QCoreApplication.instance().quit();})')

#         # Connect the signal to a slot
#         self.web_view.page().runJavaScript('py.connect(self.onMapClicked())')

#     def onMapClicked(self):
#     # Retrieve the latitude and longitude of the clicked location
#         self.web_view.page().runJavaScript(
#             '''
#             navigator.geolocation.getCurrentPosition(function(position) {
#                 var lat = position.coords.latitude;
#                 var lng = position.coords.longitude;
#                 py.emit_signal(lat + ',' + lng);
#             });
#             ''',
#             self.onGeolocationReceived()
#         )

#     def onGeolocationReceived(self, result):
#         # Split the result string into latitude and longitude
#         latitude, longitude = result.split(',')

#         # Convert the latitude and longitude to floats
#         latitude = float(latitude)
#         longitude = float(longitude)

#         # Use the latitude and longitude in your program
#         print(latitude, longitude)


# if __name__ == '__main__':
#     app = QApplication(os.sys.argv)
#     window = MapWidget()
#     window.show()
#     os.sys.exit(app.exec_())
    

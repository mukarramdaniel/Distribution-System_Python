import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *

class MapViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QWebEngineView widget and set it as the central widget
        # of the main window
        self.view = QWebEngineView(self)
        self.setCentralWidget(self.view)

        # Load a web page containing a map
        self.view.load(QUrl("http://www.google.com/maps"))

        # Set the size of the main window
        self.setGeometry(100, 100, 800, 600)

        # Create a QPushButton widget and connect its clicked signal to a
        # custom slot
        self.button = QPushButton("Select", self)
        self.button.clicked.connect(self.get_location)

    def get_location(self):
        # Execute JavaScript code to get the latitude and longitude of the
        # location that was clicked on the map
        self.view.page().runJavaScript("""
            navigator.geolocation.getCurrentPosition(function(position) {
                console.log(position.coords.latitude, position.coords.longitude);
            });
        """)

def openMap():
    app = QApplication(sys.argv)
    viewer = MapViewer()
    viewer.show()
    sys.exit(app.exec_())

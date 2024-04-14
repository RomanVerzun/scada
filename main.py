import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, QObject, pyqtSlot
from PyQt6.QtWebChannel import QWebChannel


class Bridge(QObject):
    @pyqtSlot(int)
    def handleValue(self, value):
        print(f"Received value: {value}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1920, 980)
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.channel = QWebChannel()
        self.bridge = Bridge()
        self.channel.registerObject('bridge', self.bridge)
        self.browser.page().setWebChannel(self.channel)
        self.browser.load(QUrl.fromLocalFile('/home/trainer/Documents/scada/index.html'))

    def on_load_finished(self, success):
        if success:
            self.setup_connections()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

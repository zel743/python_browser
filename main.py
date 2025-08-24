import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import QUrl
#aqui se importa las librerias a usar
from PyQt5.QtWidgets import *
#esta libreria importa la ingenieria dle navegador
from PyQt5.QtWebEngineWidgets import *


#se hace una clase en donde estara la ventana del navegador
class mainwin(QMainWindow):
    def __init__(self):
        super(mainwin, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #aqui va el navbar

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        reload_btn = QAction('reload',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('home',self)
        home_btn.triggered.connect(self.browser_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit(self)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

    def browser_home(self):
        self.browser.setUrl(QUrl("http://google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


app = QApplication(sys.argv)
QApplication.setApplicationName('navegador')
window = mainwin()
app.exec_()
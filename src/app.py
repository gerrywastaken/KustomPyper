import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui

from gui import Ui_MainWindow
import reddit_window
import unsplash_window


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show_reddit_page()
        """ Moving the next two lines to the reddit window init results in the following warning 
        QWindowsWindow::setGeometry: Unable to set geometry 1920x1080+0+29 (frame: 1938x1127-9-9) on QWidgetWindow/"MainWindowWindow" 
        on " \\\.\DISPLAY1". Resulting geometry: 1920x1001+0+29 """
        self.screenSize = QDesktopWidget().screenGeometry(0)
        self.setMinimumSize(self.screenSize.width(), self.screenSize.height())
        self.pageRedditAction.triggered.connect(self.show_reddit_page)
        self.pageUnsplashAction.triggered.connect(self.show_unsplash_page)
        self.aboutAction.triggered.connect(self.show_about_page)
        self.helpAction.triggered.connect(self.open_help_url)
        self.showMaximized()

    def show_reddit_page(self):
        self.pageStackWidget.setCurrentIndex(0)

    def show_unsplash_page(self):
        self.pageStackWidget.setCurrentIndex(1)

    def show_about_page(self):
        self.pageStackWidget.setCurrentIndex(2)

    def open_help_url(self):
        url = QUrl("https://github.com/kriticalflare/KustomPyper/blob/master/README.md")
        if not QtGui.QDesktopServices.openUrl(url):
            QMessageBox.warning(
                self,
                "Open Url",
                "Could not open https://github.com/kriticalflare/KustomPyper/",
            )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    RedditWindow = reddit_window.RedditWindow(MainWindow)
    UnsplashWindow = unsplash_window.UnsplashWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

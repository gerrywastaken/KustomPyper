# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic_unsplash.u.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1239, 776)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pageStackWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.pageStackWidget.setObjectName("pageStackWidget")
        self.redditPage = QtWidgets.QWidget()
        self.redditPage.setObjectName("redditPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.redditPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.redditSubredditCombo = QtWidgets.QComboBox(self.redditPage)
        self.redditSubredditCombo.setEditable(True)
        self.redditSubredditCombo.setObjectName("redditSubredditCombo")
        self.redditSubredditCombo.addItem("")
        self.redditSubredditCombo.addItem("")
        self.gridLayout_2.addWidget(self.redditSubredditCombo, 2, 3, 1, 1)
        self.redditLimitLabel = QtWidgets.QLabel(self.redditPage)
        self.redditLimitLabel.setObjectName("redditLimitLabel")
        self.gridLayout_2.addWidget(self.redditLimitLabel, 4, 1, 1, 1)
        self.redditSubredditLabel = QtWidgets.QLabel(self.redditPage)
        self.redditSubredditLabel.setObjectName("redditSubredditLabel")
        self.gridLayout_2.addWidget(self.redditSubredditLabel, 2, 1, 1, 1)
        self.redditPhoto = QtWidgets.QLabel(self.redditPage)
        self.redditPhoto.setEnabled(True)
        self.redditPhoto.setScaledContents(False)
        self.redditPhoto.setAlignment(QtCore.Qt.AlignCenter)
        self.redditPhoto.setObjectName("redditPhoto")
        self.gridLayout_2.addWidget(self.redditPhoto, 0, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(784, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.redditCategoryLabel = QtWidgets.QLabel(self.redditPage)
        self.redditCategoryLabel.setObjectName("redditCategoryLabel")
        self.gridLayout_2.addWidget(self.redditCategoryLabel, 3, 1, 1, 1)
        self.redditLimitCombo = QtWidgets.QComboBox(self.redditPage)
        self.redditLimitCombo.setEditable(True)
        self.redditLimitCombo.setObjectName("redditLimitCombo")
        self.redditLimitCombo.addItem("")
        self.redditLimitCombo.addItem("")
        self.redditLimitCombo.addItem("")
        self.gridLayout_2.addWidget(self.redditLimitCombo, 4, 3, 1, 1)
        self.redditDarkModelabel = QtWidgets.QLabel(self.redditPage)
        self.redditDarkModelabel.setObjectName("redditDarkModelabel")
        self.gridLayout_2.addWidget(self.redditDarkModelabel, 5, 1, 1, 1)
        self.redditSaveButton = QtWidgets.QPushButton(self.redditPage)
        self.redditSaveButton.setObjectName("redditSaveButton")
        self.gridLayout_2.addWidget(self.redditSaveButton, 6, 2, 1, 1)
        self.redditNextWallButton = QtWidgets.QPushButton(self.redditPage)
        self.redditNextWallButton.setObjectName("redditNextWallButton")
        self.gridLayout_2.addWidget(self.redditNextWallButton, 6, 1, 1, 1)
        self.redditSearchTextEdit = QtWidgets.QTextEdit(self.redditPage)
        self.redditSearchTextEdit.setMaximumSize(QtCore.QSize(500, 21))
        self.redditSearchTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.redditSearchTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.redditSearchTextEdit.setAcceptRichText(False)
        self.redditSearchTextEdit.setObjectName("redditSearchTextEdit")
        self.gridLayout_2.addWidget(self.redditSearchTextEdit, 1, 3, 1, 1)
        self.redditDarkModeCheck = QtWidgets.QCheckBox(self.redditPage)
        self.redditDarkModeCheck.setText("")
        self.redditDarkModeCheck.setObjectName("redditDarkModeCheck")
        self.gridLayout_2.addWidget(self.redditDarkModeCheck, 5, 3, 1, 1)
        self.redditWallpaperButton = QtWidgets.QPushButton(self.redditPage)
        self.redditWallpaperButton.setObjectName("redditWallpaperButton")
        self.gridLayout_2.addWidget(self.redditWallpaperButton, 6, 3, 1, 1)
        self.redditCategoryCombo = QtWidgets.QComboBox(self.redditPage)
        self.redditCategoryCombo.setObjectName("redditCategoryCombo")
        self.redditCategoryCombo.addItem("")
        self.redditCategoryCombo.addItem("")
        self.redditCategoryCombo.addItem("")
        self.redditCategoryCombo.addItem("")
        self.redditCategoryCombo.addItem("")
        self.gridLayout_2.addWidget(self.redditCategoryCombo, 3, 3, 1, 1)
        self.redditSearchLabel = QtWidgets.QLabel(self.redditPage)
        self.redditSearchLabel.setObjectName("redditSearchLabel")
        self.gridLayout_2.addWidget(self.redditSearchLabel, 1, 1, 1, 1)
        self.pageStackWidget.addWidget(self.redditPage)
        self.unsplashPage = QtWidgets.QWidget()
        self.unsplashPage.setObjectName("unsplashPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.unsplashPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.unsplashPhoto = QtWidgets.QLabel(self.unsplashPage)
        self.unsplashPhoto.setEnabled(True)
        self.unsplashPhoto.setScaledContents(False)
        self.unsplashPhoto.setAlignment(QtCore.Qt.AlignCenter)
        self.unsplashPhoto.setObjectName("unsplashPhoto")
        self.gridLayout_4.addWidget(self.unsplashPhoto, 0, 0, 1, 4)
        self.unsplashSearchLabel = QtWidgets.QLabel(self.unsplashPage)
        self.unsplashSearchLabel.setObjectName("unsplashSearchLabel")
        self.gridLayout_4.addWidget(self.unsplashSearchLabel, 1, 1, 1, 1)
        self.unsplashSearchTextEdit = QtWidgets.QTextEdit(self.unsplashPage)
        self.unsplashSearchTextEdit.setMaximumSize(QtCore.QSize(500, 21))
        self.unsplashSearchTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.unsplashSearchTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.unsplashSearchTextEdit.setAcceptRichText(False)
        self.unsplashSearchTextEdit.setObjectName("unsplashSearchTextEdit")
        self.gridLayout_4.addWidget(self.unsplashSearchTextEdit, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(752, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 2, 0, 1, 1)
        self.unsplashFeaturedLabel = QtWidgets.QLabel(self.unsplashPage)
        self.unsplashFeaturedLabel.setObjectName("unsplashFeaturedLabel")
        self.gridLayout_4.addWidget(self.unsplashFeaturedLabel, 2, 1, 1, 1)
        self.unsplashDarkModeLabel = QtWidgets.QLabel(self.unsplashPage)
        self.unsplashDarkModeLabel.setObjectName("unsplashDarkModeLabel")
        self.gridLayout_4.addWidget(self.unsplashDarkModeLabel, 3, 1, 1, 1)
        self.unsplashDarkModeCheck = QtWidgets.QCheckBox(self.unsplashPage)
        self.unsplashDarkModeCheck.setText("")
        self.unsplashDarkModeCheck.setObjectName("unsplashDarkModeCheck")
        self.gridLayout_4.addWidget(self.unsplashDarkModeCheck, 3, 3, 1, 1)
        self.unsplashNextWallButton = QtWidgets.QPushButton(self.unsplashPage)
        self.unsplashNextWallButton.setObjectName("unsplashNextWallButton")
        self.gridLayout_4.addWidget(self.unsplashNextWallButton, 4, 1, 1, 1)
        self.unsplashSaveButton = QtWidgets.QPushButton(self.unsplashPage)
        self.unsplashSaveButton.setObjectName("unsplashSaveButton")
        self.gridLayout_4.addWidget(self.unsplashSaveButton, 4, 2, 1, 1)
        self.unsplashWallpaperButton = QtWidgets.QPushButton(self.unsplashPage)
        self.unsplashWallpaperButton.setObjectName("unsplashWallpaperButton")
        self.gridLayout_4.addWidget(self.unsplashWallpaperButton, 4, 3, 1, 1)
        self.unsplashFeaturedCheck = QtWidgets.QCheckBox(self.unsplashPage)
        self.unsplashFeaturedCheck.setText("")
        self.unsplashFeaturedCheck.setObjectName("unsplashFeaturedCheck")
        self.gridLayout_4.addWidget(self.unsplashFeaturedCheck, 2, 3, 1, 1)
        self.pageStackWidget.addWidget(self.unsplashPage)
        self.aboutPage = QtWidgets.QWidget()
        self.aboutPage.setObjectName("aboutPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.aboutPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.aboutLabel = QtWidgets.QLabel(self.aboutPage)
        self.aboutLabel.setTextFormat(QtCore.Qt.RichText)
        self.aboutLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.aboutLabel.setWordWrap(True)
        self.aboutLabel.setOpenExternalLinks(True)
        self.aboutLabel.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.aboutLabel.setObjectName("aboutLabel")
        self.gridLayout_3.addWidget(self.aboutLabel, 0, 0, 1, 1)
        self.pageStackWidget.addWidget(self.aboutPage)
        self.gridLayout.addWidget(self.pageStackWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1239, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuNavigate = QtWidgets.QMenu(self.menubar)
        self.menuNavigate.setObjectName("menuNavigate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.aboutAction = QtWidgets.QAction(MainWindow)
        self.aboutAction.setObjectName("aboutAction")
        self.helpAction = QtWidgets.QAction(MainWindow)
        self.helpAction.setObjectName("helpAction")
        self.redditAction = QtWidgets.QAction(MainWindow)
        self.redditAction.setCheckable(False)
        self.redditAction.setObjectName("redditAction")
        self.redditPageAction = QtWidgets.QAction(MainWindow)
        self.redditPageAction.setObjectName("redditPageAction")
        self.pageRedditAction = QtWidgets.QAction(MainWindow)
        self.pageRedditAction.setObjectName("pageRedditAction")
        self.pageUnsplashAction = QtWidgets.QAction(MainWindow)
        self.pageUnsplashAction.setObjectName("pageUnsplashAction")
        self.menuHelp.addAction(self.aboutAction)
        self.menuHelp.addAction(self.helpAction)
        self.menuNavigate.addAction(self.pageRedditAction)
        self.menuNavigate.addAction(self.pageUnsplashAction)
        self.menubar.addAction(self.menuNavigate.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.pageStackWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.redditSubredditCombo.setItemText(0, _translate("MainWindow", "wallpapers"))
        self.redditSubredditCombo.setItemText(1, _translate("MainWindow", "amoledbackgrounds"))
        self.redditLimitLabel.setText(_translate("MainWindow", "Limit :"))
        self.redditSubredditLabel.setText(_translate("MainWindow", "Subreddit : "))
        self.redditPhoto.setText(_translate("MainWindow", "Set a random wallpaper from reddit!"))
        self.redditCategoryLabel.setText(_translate("MainWindow", "Category :"))
        self.redditLimitCombo.setItemText(0, _translate("MainWindow", "10"))
        self.redditLimitCombo.setItemText(1, _translate("MainWindow", "25"))
        self.redditLimitCombo.setItemText(2, _translate("MainWindow", "50"))
        self.redditDarkModelabel.setText(_translate("MainWindow", "Dark Mode :"))
        self.redditSaveButton.setText(_translate("MainWindow", "Save to Pictures"))
        self.redditNextWallButton.setText(_translate("MainWindow", "Next wallpaper"))
        self.redditWallpaperButton.setText(_translate("MainWindow", "Set as wallpaper"))
        self.redditCategoryCombo.setItemText(0, _translate("MainWindow", "hot"))
        self.redditCategoryCombo.setItemText(1, _translate("MainWindow", "rising"))
        self.redditCategoryCombo.setItemText(2, _translate("MainWindow", "new"))
        self.redditCategoryCombo.setItemText(3, _translate("MainWindow", "top"))
        self.redditCategoryCombo.setItemText(4, _translate("MainWindow", "controversial"))
        self.redditSearchLabel.setText(_translate("MainWindow", "Search:"))
        self.unsplashPhoto.setText(_translate("MainWindow", "Set a random wallpaper from Unsplash!"))
        self.unsplashSearchLabel.setText(_translate("MainWindow", "Search:"))
        self.unsplashFeaturedLabel.setText(_translate("MainWindow", "Featured :"))
        self.unsplashDarkModeLabel.setText(_translate("MainWindow", "Dark Mode :"))
        self.unsplashNextWallButton.setText(_translate("MainWindow", "Next wallpaper"))
        self.unsplashSaveButton.setText(_translate("MainWindow", "Save to Pictures"))
        self.unsplashWallpaperButton.setText(_translate("MainWindow", "Set as wallpaper"))
        self.aboutLabel.setText(_translate("MainWindow", "KustomPyper - Get amazing wallpapers for your desktop. <br> Created by Kriticalflare (<a href=\"https://github.com/kriticalflare\">Github</a>) </br>"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuNavigate.setTitle(_translate("MainWindow", "Navigate"))
        self.aboutAction.setText(_translate("MainWindow", "About"))
        self.helpAction.setText(_translate("MainWindow", "Help"))
        self.redditAction.setText(_translate("MainWindow", "Reddit Walls"))
        self.redditPageAction.setText(_translate("MainWindow", "Reddit"))
        self.pageRedditAction.setText(_translate("MainWindow", "Reddit Walls"))
        self.pageUnsplashAction.setText(_translate("MainWindow", "Unsplash Walls"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

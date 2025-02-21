from main import *
import json
import os
# module to detect dark mode
import darkdetect
# module to edit/read registory
from winreg import *

# import dark and light theme
from files.ui.themes.dark import UIDark
from files.ui.themes.light import UILight

# load main setting
load_settings = open("settings.json")
Data = json.load(load_settings) 

# default theme 
defaultTheme = Data["app"]["theme"]["type"]
# print(defaultTheme)

class UIFunctions(MainWindow):
	# set theme of window
	def SetTheme(self):
		global defaultTheme  # Declare defaultTheme as global

		if defaultTheme == "system":
			isThemeDark = darkdetect.isDark()
			if isThemeDark:
				UIDark.SetStyleSheetDark(self)
			else:
				UILight.SetStyleSheetLight(self)
		elif defaultTheme == "light":
			UILight.SetStyleSheetLight(self)
			if Data["app"]["theme"]["mica"]["enabled"]:
				ApplyMica(self.winId(), MicaTheme.LIGHT, MicaStyle.DEFAULT)
		elif defaultTheme == "dark":
			UIDark.SetStyleSheetDark(self)
			if Data["app"]["theme"]["mica"]["enabled"]:
				ApplyMica(self.winId(), MicaTheme.DARK, MicaStyle.DEFAULT)
	
	# switch theme
	def SwitchTheme(self):
		global defaultTheme

		# Determine if the current theme is dark based on the defaultTheme
		if defaultTheme == "system":
			isThemeDark = darkdetect.isDark()
			defaultTheme = "dark" if isThemeDark else "light"  # Set defaultTheme based on detection

		# Apply the appropriate styles based on the defaultTheme
		if defaultTheme == "light":
			UILight.SetStyleSheetLight(self)
			if Data["app"]["theme"]["mica"]["enabled"]:
				ApplyMica(self.winId(), MicaTheme.LIGHT, MicaStyle.DEFAULT)
			defaultTheme = "dark"  # Change to dark theme for next call
		else:
			UIDark.SetStyleSheetDark(self)
			if Data["app"]["theme"]["mica"]["enabled"]:
				ApplyMica(self.winId(), MicaTheme.DARK, MicaStyle.DEFAULT)
			defaultTheme = "light"  # Change to light theme for next call

	# slider for left menu (with animation)
	def ToggleMenu(self, min, max):

		presentWidth = self.ui.leftMenu.width()

		startToggle = ""
		endToggle = ""

		if presentWidth == min:
			startToggle = min
			endToggle = max
			
			self.ui.home_btn.setText("Home")
			self.ui.settings_btn.setText("Settings")
			self.ui.theme_btn.setText("Theme")

		elif presentWidth == max:
			startToggle = max
			endToggle = min

			self.ui.home_btn.setText("")
			self.ui.settings_btn.setText("")
			self.ui.theme_btn.setText("")


		self.animation = QPropertyAnimation(self.ui.leftMenu, b"minimumWidth")
		self.animation.setDuration(200)
		self.animation.setStartValue(startToggle)
		self.animation.setEndValue(endToggle)
		# self.animation.setEasingCurve(QEasingCurve.InOutQuart)
		# self.animation.setEasingCurve(QEasingCurve.InOutCubic)  # Replacing InOutQuart

		self.animation.start()
	
	# setting up all ui functions
	def Setup_GUI(self):

		# set window title
		self.setWindowTitle(Data["app"]["name"])
		# UIFunctions.ToggleMenu(self, 50, 300)

		# set windows default size
		self.resize(Data["app"]["window"]["size"]["default"][0], Data["app"]["window"]["size"]["default"][1])

		# set window min size
		if Data["app"]["window"]["size"]["isMinimized"] != False:
			self.setMinimumSize(Data["app"]["window"]["size"]["min"][0], Data["app"]["window"]["size"]["min"][1])
		
		# set window max size
		if Data["app"]["window"]["size"]["isMaximized"] != False:
			self.setMaximumSize(Data["app"]["window"]["size"]["max"][0], Data["app"]["window"]["size"]["max"][1])
			
		# left bar click (change pages)
		self.ui.home_btn.clicked.connect(lambda : self.ui.switchPage.setCurrentIndex(0))
		self.ui.settings_btn.clicked.connect(lambda : self.ui.switchPage.setCurrentIndex(1))

		# theme change btn
		self.ui.theme_btn.clicked.connect(lambda : UIFunctions.SwitchTheme(self))

		# left bar toggle btn (min or max)
		self.ui.menu_btn.clicked.connect(lambda : UIFunctions.ToggleMenu(self, 50, 300))


		
		# setting custom icon for app
		customIcon = Data["app"]["icon"]["custom"]
		if customIcon == True:
			WindowIcon = QIcon()
			WindowIcon.addFile("icon.ico")
			self.setWindowIcon(WindowIcon)


		# setting mica effect
		if Data["app"]["theme"]["mica"]["enabled"]:
			# self.setAttribute(Qt.WA_TranslucentBackground)
			self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
			ApplyMica(self.winId(), MicaTheme.AUTO, MicaStyle.DEFAULT)

		# from files.ui.blurwindow import ExtendFrameIntoClientArea, GlobalBlur
		# # from PySide6.QtWinExtras import QtWin
		# if Data["app"]["theme"]["mica"]["enabled"] == True:
		# 	hwnd = self.winId().__int__()
		# 	self.setAttribute(Qt.WA_TranslucentBackground)
			
		# 	# from PySide6.QtWinExtras import QtWin
		# 	# if QtWin.isCompositionEnabled():
		# 	# 	QtWin.extendFrameIntoClientArea(self, -1, -1, -1, -1)
		# 	# else:
		# 	# 	QtWin.resetExtendedFrame(self)

		# 	# ExtendFrameIntoClientArea(hwnd)

		# setting mica effect
		# ApplyMica(self.winId(), MicaTheme.AUTO, MicaStyle.DEFAULT)






		# ###### add menu bar

		# self.menuBar = QMenuBar(self.ui.centralwidget)
		# self.menuBar.setEnabled(True)
		# self.menuBar.setGeometry(QRect(0, 0, 980, 63))
		# self.menuBar.setObjectName("menuBar")

		# self.menuFile = QMenu(self.menuBar)
		# self.menuFile.setObjectName("menuFile")
		# self.menuFile.setTitle("File")  # Set title for menu

		# self.menuEdit = QMenu(self.menuBar)
		# self.menuEdit.setObjectName("menuEdit")
		# self.menuEdit.setTitle("Edit")  # Set title for menu

		# self.menuHelp = QMenu(self.menuBar)
		# self.menuHelp.setObjectName("menuHelp")
		# self.menuHelp.setTitle("Help")  # Set title for menu

		# self.ui.centralwidget.setMenuBar(self.menuBar)

		# self.actionNew = QAction("New", self.ui.centralwidget)  # Create action for "New"
		# self.actionNew.setObjectName("actionNew")

		# self.actionPlain_Text_Document = QAction("Plain Text Document", MainWindow)
		# self.actionPlain_Text_Document.setObjectName("actionPlain_Text_Document")

		# self.actionRich_Text_Document = QAction("Rich Text Document", MainWindow)
		# self.actionRich_Text_Document.setObjectName("actionRich_Text_Document")

		# self.actionOpen = QAction("Open", self.ui.centralwidget)
		# self.actionOpen.setObjectName("actionOpen")

		# self.actionSave = QAction("Save", self.ui.centralwidget)
		# self.actionSave.setEnabled(True)
		# self.actionSave.setObjectName("actionSave")

		# self.actionExit = QAction("Exit", self.ui.centralwidget)
		# self.actionExit.setObjectName("actionExit")

		# self.actionUndo = QAction("Undo", self.ui.centralwidget)
		# self.actionUndo.setObjectName("actionUndo")

		# self.actionCut = QAction("Cut", self.ui.centralwidget)
		# self.actionCut.setObjectName("actionCut")

		# self.actionCopy = QAction("Copy", self.ui.centralwidget)
		# self.actionCopy.setObjectName("actionCopy")

		# self.actionPaste = QAction("Paste", self.ui.centralwidget)
		# self.actionPaste.setObjectName("actionPaste")

		# self.actionAbout = QAction("About", self.ui.centralwidget)
		# self.actionAbout.setEnabled(True)
		# self.actionAbout.setObjectName("actionAbout")

		# # Create submenu for New
		# self.subMenuNew = QMenu("New", self.ui.centralwidget)
		# self.subMenuNew.addAction(self.actionPlain_Text_Document)
		# self.subMenuNew.addAction(self.actionRich_Text_Document)

		# self.menuFile.addAction(self.subMenuNew.menuAction())
		# self.menuFile.addAction(self.actionOpen)
		# self.menuFile.addAction(self.actionSave)
		# self.menuFile.addAction(self.actionExit)

		# self.menuEdit.addAction(self.actionUndo)
		# self.menuEdit.addAction(self.actionCut)
		# self.menuEdit.addAction(self.actionCopy)
		# self.menuEdit.addAction(self.actionPaste)

		# self.menuHelp.addAction(self.actionAbout)

		# self.menuBar.addAction(self.menuFile.menuAction())
		# self.menuBar.addAction(self.menuEdit.menuAction())
		# self.menuBar.addAction(self.menuHelp.menuAction())
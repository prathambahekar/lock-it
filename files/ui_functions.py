from main import *
import json
import os
import darkdetect

load_settings = open("settings.json")
Data = json.load(load_settings) 
defaultTheme = Data["app-info"]["theme"]


class UIFunctions(MainWindow):

	def SetTheme(self):
		
		if defaultTheme == "sys":
			checkTheme = darkdetect.isDark()
			# print(checkTheme)
			if checkTheme == True:
				str = open(f"files/themes/dark.qss", 'r').read()
				self.ui.centralwidget.setStyleSheet(str)
			else:
				str = open(f"files/themes/light.qss", 'r').read()
				self.ui.centralwidget.setStyleSheet(str)

		else:
			str = open(f"files/themes/{defaultTheme}.qss", 'r').read()
			self.ui.centralwidget.setStyleSheet(str)
		
	def SwitchTheme(self):
		global defaultTheme

		# Directory where your .qss files are located
		qss_directory = "files/themes"

		# Get a list of all .qss files in the directory
		qss_files = [file for file in os.listdir(qss_directory) if file.endswith(".qss")]

		# Find the index of the current theme
		try:
			current_index = qss_files.index(defaultTheme + ".qss")
		except ValueError:
			current_index = -1

		# Calculate the next theme index
		next_index = (current_index + 1) % len(qss_files)
		next_theme = qss_files[next_index].replace(".qss", "")

		# Read and apply the next theme
		with open(os.path.join(qss_directory, qss_files[next_index]), 'r') as f:
			stylesheet = f.read()
		self.ui.centralwidget.setStyleSheet(stylesheet)
		defaultTheme = next_theme

		if Data["app-info"]["mica"]["enable"] == True:
			if defaultTheme == "light":
				ApplyMica(self.winId(), MicaTheme.LIGHT, MicaStyle.DEFAULT)
			elif defaultTheme == "dark":
				ApplyMica(self.winId(), MicaTheme.DARK, MicaStyle.DEFAULT)

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
		self.animation.setEasingCurve(QEasingCurve.InOutQuart)
		self.animation.start()

	def show_message(self, message, title):
		msg_box = QMessageBox(self)
		msg_box.setWindowTitle(title)
		msg_box.setText(message)

		# Apply custom style to the message box to match the light theme and make it large
		msg_box.setStyleSheet("""
			/* Overall message box style */
			QMessageBox {
				background-color: #f6f8fa;  /* Light background */
				color: #202325;  /* Text color */
				font: 600 16pt "Consolas";  /* Font size and family */
				border-radius: 10px;  /* Rounded corners */
				min-width: 400px;  /* Increased minimum width */
				min-height: 200px;  /* Increased minimum height */
				padding: 20px;  /* Padding inside the message box */
			}

			/* Styling the title of the message box */
			QMessageBox QLabel {
				font: 700 18pt "Consolas";  /* Bold title font */
				color: #202325;  /* Dark text for title */
				padding-bottom: 10px;  /* Space between title and content */
			}

			/* Styling the content text inside the message box */
			QMessageBox QLabel:!selected {
				font: 600 14pt "Consolas";  /* Regular font for the message */
				color: #202325;  /* Dark text color */
				margin-bottom: 20px;  /* Space between message and buttons */
			}

			/* Button styling inside the message box */
			QMessageBox QPushButton {
				background-color: #eff1f3;  /* Light button background */
				border: 2px solid #e1e1e1;  /* Light border for buttons */
				padding: 12px 20px;  /* Padding inside the button */
				font: 600 14pt "Consolas";  /* Button font */
				color: #202325;  /* Text color inside the button */
				border-radius: 6px;  /* Rounded corners for buttons */
				min-width: 120px;  /* Minimum width for buttons */
			}

			/* Button hover effect */
			QMessageBox QPushButton:hover {
				background-color: #ededed;  /* Hover effect on button */
				border-color: #d1d1d1;  /* Lighter border on hover */
			}

			/* Button pressed effect */
			QMessageBox QPushButton:pressed {
				background-color: #d1d1d1;  /* Darker color when button is pressed */
				border-color: #b0b0b0;  /* Even lighter border on press */
			}

			/* Adding a 'Cancel' button with a different style */
			QMessageBox QPushButton#cancelButton {
				background-color: #f0f0f0;  /* Slightly different color for cancel */
				border-color: #ccc;
			}

			/* Styling the button layout */
			QMessageBox QHBoxLayout {
				spacing: 15px;  /* More space between buttons */
			}

			/* Customizing the icon if you want */
			QMessageBox QLabel[icon] {
				background: transparent;  /* Remove default icon background */
			}
			
			/* Add a custom shadow around the box for extra depth */
			QMessageBox {
				box-shadow: 0 0 15px rgba(0, 0, 0, 0.15);  /* Soft shadow */
			}
		""")

		# Add the custom cancel button to be styled differently, if needed
		# cancel_button = msg_box.addButton(QMessageBox.Cancel)
		# cancel_button.setObjectName("cancelButton")
		
		# msg_box.setIcon(QMessageBox.Information)  # You can change this to other icons if needed
		# msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

		# Show the message box
		msg_box.exec()

	def select_folder(self):
		folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
		if folder_path:
			self.folder_path = folder_path
			self.ui.drag_n_drop_lbl.setText(f"Selected Folder : {os.path.basename(folder_path)}")
		else:
			self.ui.drag_n_drop_lbl.setText("No Folder selected")


	def Setup_GUI(self):

		# set window title
		self.setWindowTitle(Data["app-info"]["name"])

		# set windows default size
		self.resize(Data["app-info"]["window-size"]["default"][0], Data["app-info"]["window-size"]["default"][1])

		# set window min size
		if Data["app-info"]["window-size"]["isMin"] != False:
			self.setMinimumSize(Data["app-info"]["window-size"]["min"][0], Data["app-info"]["window-size"]["min"][1])
		
		# set window max size
		if Data["app-info"]["window-size"]["isMax"] != False:
			self.setMaximumSize(Data["app-info"]["window-size"]["max"][0], Data["app-info"]["window-size"]["max"][1])
			

		self.ui.home_btn.clicked.connect(lambda : self.ui.switchPage.setCurrentIndex(0))
		self.ui.settings_btn.clicked.connect(lambda : self.ui.switchPage.setCurrentIndex(1))

		self.ui.theme_btn.clicked.connect(lambda : UIFunctions.SwitchTheme(self))

		self.ui.menu_btn.clicked.connect(lambda : UIFunctions.ToggleMenu(self, 50, 300))

		WindowIcon = QIcon()
		WindowIcon.addFile("icon.ico")
		self.setWindowIcon(WindowIcon)

		self.ui.pass_input_box.setEchoMode(QLineEdit.Password)
		self.ui.app_title_lbl.setText("🔒 Folder Locker 🗝️")
		self.ui.open_folder_btn.clicked.connect(lambda : UIFunctions.select_folder(self))
		
		if Data["app-info"]["mica"]["enable"] == True:
			self.setAttribute(Qt.WA_TranslucentBackground)
			ApplyMica(self.winId(), MicaTheme.AUTO, MicaStyle.DEFAULT)
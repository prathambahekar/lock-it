from main import *
import json
import os
import darkdetect
import stat
import base64
import hashlib
from cryptography.fernet import Fernet
from winreg import *


load_settings = open("settings.json")
Data = json.load(load_settings) 
defaultTheme = Data["app-info"]["theme"]
MASTER_KEY = "flame"
key = ""
msgbox_theme = "dark"

class UIFunctions(MainWindow):

	def GetTheme(self):
		global msgbox_theme
		if defaultTheme == "sys":
			checkTheme = darkdetect.isDark()
			if checkTheme == True:
				msgbox_theme = "dark"
			else:
				msgbox_theme = "light"

		else:
			msgbox_theme = defaultTheme

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

	def show_message(self, message, title, theme='light'):
		msg_box = QMessageBox(self)
		msg_box.setWindowTitle(title)
		msg_box.setText(message)

		# Determine the stylesheet based on the selected theme
		if theme == 'dark':
			# Dark theme styles
			stylesheet = """
				QMessageBox {
					background-color: #2e2e2e;  /* Dark background */
					color: #e0e0e0;  /* Light text color */
					font: 600 16pt "Consolas";
					border-radius: 10px;
					min-width: 400px;
					min-height: 200px;
					padding: 20px;
				}
				QMessageBox QLabel {
					font: 700 18pt "Consolas";
					color: #e0e0e0;
					padding-bottom: 10px;
				}
				QMessageBox QLabel:!selected {
					font: 600 14pt "Consolas";
					color: #cfcfcf;
					margin-bottom: 20px;
				}
				QMessageBox QPushButton {
					background-color: #444;  /* Dark button background */
					border: 2px solid #555;  /* Border for buttons */
					padding: 12px 20px;
					font: 600 14pt "Consolas";
					color: #e0e0e0;
					border-radius: 6px;
					min-width: 120px;
				}
				QMessageBox QPushButton:hover {
					background-color: #555;  /* Hover effect */
					border-color: #666;
				}
				QMessageBox QPushButton:pressed {
					background-color: #666;
					border-color: #777;
				}
				QMessageBox QPushButton#cancelButton {
					background-color: #5a5a5a;
					border-color: #888;
				}
				QMessageBox QHBoxLayout {
					spacing: 15px;
				}
				QMessageBox QLabel[icon] {
					background: transparent;
				}
				QMessageBox {
					box-shadow: 0 0 15px rgba(0, 0, 0, 0.6);
				}
			"""
		else:
			# Light theme styles (default)
			stylesheet = """
				QMessageBox {
					background-color: #f6f8fa;
					color: #202325;
					font: 600 16pt "Consolas";
					border-radius: 10px;
					min-width: 400px;
					min-height: 200px;
					padding: 20px;
				}
				QMessageBox QLabel {
					font: 700 18pt "Consolas";
					color: #202325;
					padding-bottom: 10px;
				}
				QMessageBox QLabel:!selected {
					font: 600 14pt "Consolas";
					color: #202325;
					margin-bottom: 20px;
				}
				QMessageBox QPushButton {
					background-color: #eff1f3;
					border: 2px;
					padding: 12px 20px;
					font: 600 14pt "Consolas";
					color: #202325;
					border-radius: 6px;
					min-width: 120px;
				}
				QMessageBox QPushButton:hover {
					background-color: #ededed;
					border-color: #b0b0b0;
				}
				QMessageBox QPushButton:pressed {
					background-color: #d1d1d1;
					border-color: #a0a0a0;
				}
				QMessageBox QPushButton#cancelButton {
					background-color: #f0f0f0;
					border-color: #ccc;
				}
				QMessageBox QHBoxLayout {
					spacing: 15px;
				}
				QMessageBox QLabel[icon] {
					background: transparent;
				}
				QMessageBox {
					box-shadow: 0 0 15px rgba(0, 0, 0, 0.15);
				}
			"""
		
		# Apply the selected theme stylesheet
		msg_box.setStyleSheet(stylesheet)
		
		# Add the custom cancel button if needed
		# cancel_button = msg_box.addButton(QMessageBox.Cancel)
		# cancel_button.setObjectName("cancelButton")
		
		# msg_box.setIcon(QMessageBox.Information)
		# msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

		# Show the message box
		msg_box.exec()
	def encrypt_files(folder_path, password):
		# Generate a key from the password
		key = hashlib.sha256(password).digest()  # Use SHA-256 to create a fixed-length key
		fernet = Fernet(base64.urlsafe_b64encode(key))  # Create a Fernet instance with the key

		for filename in os.listdir(folder_path):
			file_path = os.path.join(folder_path, filename)

			if os.path.isfile(file_path):
				with open(file_path, 'rb') as file:
					original_data = file.read()
				encrypted_data = fernet.encrypt(original_data)

				with open(file_path, 'wb') as file:
					file.write(encrypted_data)

	def decrypt_files(folder_path, password):
		# Generate a key from the password
		key = hashlib.sha256(password).digest()  # Use SHA-256 to create a fixed-length key
		fernet = Fernet(base64.urlsafe_b64encode(key))  # Create a Fernet instance with the key

		for filename in os.listdir(folder_path):
			file_path = os.path.join(folder_path, filename)

			if os.path.isfile(file_path):
				with open(file_path, 'rb') as file:
					encrypted_data = file.read()
				decrypted_data = fernet.decrypt(encrypted_data)

				with open(file_path, 'wb') as file:
					file.write(decrypted_data)

	def select_folder(self):
		folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
		if folder_path:
			self.ui.folder_path = folder_path
			folder_name = os.path.basename(folder_path)
			self.ui.drag_n_drop_lbl.setText(f"Selected Folder: {folder_name}")
		else:
			self.ui.drag_n_drop_lbl.setText("No Folder selected")

	
	def lock_folder(self):
		global key
		UIFunctions.GetTheme(self)
		if not self.ui.folder_path:
			UIFunctions.show_message(self, "Please select a folder!", "Error", msgbox_theme)
			return
		password = self.ui.pass_input_box.text()

		if not password:
			UIFunctions.show_message(self, "Please enter a password!", "Error", msgbox_theme)
			return

		key = password.encode()  # Convert password to bytes
		try:
			UIFunctions.encrypt_files(self.ui.folder_path, key)
			UIFunctions.show_message(self, "Folder locked successfully!", "Success", msgbox_theme)
		except Exception as e:
			UIFunctions.show_message(self, f"Error: {str(e)}", "Error", msgbox_theme)
		self.ui.pass_input_box.clear()
		self.ui.folder_path = ""
		self.ui.drag_n_drop_lbl.setText("Drag and drop a folder here \n" "or use the button below")

	def unlock_folder(self):
		global key
		if not self.ui.folder_path:
			UIFunctions.show_message(self, "Please select a folder!", "Error", msgbox_theme)
			return

		password = self.ui.pass_input_box.text()

		if not password:
			UIFunctions.show_message(self, "Please enter a password or master key!", "Error", msgbox_theme)
			return

		key = password.encode()  # Convert password to bytes
		try:
			UIFunctions.decrypt_files(self.ui.folder_path, key)
			UIFunctions.show_message(self, "Folder unlocked successfully!", "Success", msgbox_theme)
		except Exception as e:
			UIFunctions.show_message(self, f"Error: {str(e)}", "Error", msgbox_theme)

		# Clear input fields and reset UI
		self.ui.pass_input_box.clear()
		self.ui.folder_path = ""
		self.ui.drag_n_drop_lbl.setText("Drag and drop a folder here \n" "or use the button below")


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

		self.ui.lock_folder_btn.clicked.connect(lambda : UIFunctions.lock_folder(self))
		self.ui.unlock_folder_btn.clicked.connect(lambda : UIFunctions.unlock_folder(self))


		# self.ui.drag_n_drop_lbldrag_n_drop_lbl.setText("Drag and drop a folder here \n" "or use the button below")
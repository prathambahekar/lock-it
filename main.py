from files.ui_functions import *
from files.ui_main import Ui_MainWindow
import json
from core import *

access_settings = open("settings.json")
Data = json.load(access_settings) 

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		global defaultTheme

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Enable drag-and-drop
		self.setAcceptDrops(True)
		self.ui.folder_path = ""

		# Applying Settings
		UIFunctions.Setup_GUI(self)
		# UIFunctions.ToggleMenu(self, 50, 300)
		# self.ui.setStyle('Fusion')
		self.show()
		UIFunctions.SetTheme(self)
		# SetTheme(self)

		# self.ui.lock_folder_btn.clicked.connect(lambda : UIFunctions.show_message(self, "hey", "Lock your file"))


	def dragEnterEvent(self, event: QDragEnterEvent):
		if event.mimeData().hasUrls():
			event.acceptProposedAction()

	def dropEvent(self, event: QDropEvent):
		for url in event.mimeData().urls():
			folder_path = url.toLocalFile()
			if os.path.isdir(folder_path):
				self.ui.folder_path = folder_path
				self.ui.drag_n_drop_lbl.setText(f"Selected Folder : {os.path.basename(folder_path)}")
				break
	

	
		
if __name__ == "__main__":
	
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec())

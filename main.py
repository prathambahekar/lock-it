import json
# importing core modules
from core import *
# importing ui files
from files.ui.ui_functions import *
from files.ui.ui_main import Ui_MainWindow
# importing app files
from files.app.app_functions import AppFunctions

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		global defaultTheme

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Enable drag-and-drop
		self.setAcceptDrops(True)
		self.ui.folder_path = ""
		
		# Applying UI Settings
		UIFunctions.Setup_GUI(self)

		# Applying App Settings
		AppFunctions.Setup_App(self)

		# AppFunctions.printline("")

		self.show()
		
		#setting theme
		UIFunctions.SetTheme(self)
		
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

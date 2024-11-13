import os
import stat
import base64
import hashlib
from cryptography.fernet import Fernet
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit,
    QLabel, QFileDialog, QVBoxLayout, QWidget, QMessageBox, QHBoxLayout
)
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QFont, QDragEnterEvent, QDropEvent

# Hardcoded master key (this is just an example)
MASTER_KEY = "flame"  # This should be a secure key, ideally encrypted or stored securely.

# Generate a key from the password using SHA-256 and base64 encoding
def generate_key(password):
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest[:32])



# Encrypt files in the folder and set folder to read-only
def encrypt_files(folder_path, key):
    cipher = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                data = f.read()
            encrypted_data = cipher.encrypt(data)
            with open(file_path, 'wb') as f:
                f.write(encrypted_data)
    
    # Set folder to read-only by removing write permissions
    os.chmod(folder_path, stat.S_IREAD | stat.S_IEXEC)
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            os.chmod(os.path.join(root, dir), stat.S_IREAD | stat.S_IEXEC)
        for file in files:
            os.chmod(os.path.join(root, file), stat.S_IREAD)

# Decrypt files in the folder and restore folder permissions
def decrypt_files(folder_path, key):
    cipher = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                encrypted_data = f.read()
            try:
                data = cipher.decrypt(encrypted_data)
                with open(file_path, 'wb') as f:
                    f.write(data)
            except:
                return False  # Return False if decryption fails
    
    # Restore folder permissions to read/write
    os.chmod(folder_path, stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            os.chmod(os.path.join(root, dir), stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)
        for file in files:
            os.chmod(os.path.join(root, file), stat.S_IWRITE | stat.S_IREAD)
    return True

# Main Window for the app with drag-and-drop support and master key fallback
class FolderLockerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folder Locker")
        self.setGeometry(500, 200, 500, 400)
        self.setStyleSheet("background-color: #121212;")
        self.folder_path = ""

        # Enable drag-and-drop
        self.setAcceptDrops(True)

        # Initialize UI
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # App Title
        title_label = QLabel("🔒 Folder Locker")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setStyleSheet("color: #e1e1e1; margin-bottom: 20px;")
        layout.addWidget(title_label)

        # Folder selection label
        self.folder_label = QLabel("Drag and drop a folder here or use the button below")
        self.folder_label.setAlignment(Qt.AlignCenter)
        self.folder_label.setFont(QFont("Arial", 12))
        self.folder_label.setStyleSheet("color: #e1e1e1;")
        layout.addWidget(self.folder_label)

        # Select folder button
        self.select_folder_btn = QPushButton("Select Folder")
        self.select_folder_btn.setStyleSheet("""
            QPushButton {
                background-color: #3A3A3A;
                color: #e1e1e1;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #5A5A5A;
            }
        """)
        self.select_folder_btn.clicked.connect(self.select_folder)
        layout.addWidget(self.select_folder_btn)

        # Password input
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter password or master key")
        self.password_input.setFont(QFont("Arial", 12))
        self.password_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #4A4A8E;
                border-radius: 5px;
                background-color: #2A2A2A;
                color: #e1e1e1;
            }
        """)
        layout.addWidget(self.password_input)

        # Buttons for Lock and Unlock
        button_layout = QHBoxLayout()
        
        self.lock_btn = QPushButton("Lock Folder")
        self.lock_btn.setStyleSheet("""
            QPushButton {
                background-color: #E94B3C;
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #D43C2F;
            }
        """)
        self.lock_btn.clicked.connect(self.lock_folder)
        button_layout.addWidget(self.lock_btn)

        self.unlock_btn = QPushButton("Unlock Folder")
        self.unlock_btn.setStyleSheet("""
            QPushButton {
                background-color: #2ECC71;
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #27AE60;
            }
        """)
        self.unlock_btn.clicked.connect(self.unlock_folder)
        button_layout.addWidget(self.unlock_btn)
        
        layout.addLayout(button_layout)

        # Status message
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont("Arial", 10))
        self.status_label.setStyleSheet("color: #e1e1e1;")
        layout.addWidget(self.status_label)

        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.folder_path = folder_path
            self.folder_label.setText(f"Selected: {os.path.basename(folder_path)}")
        else:
            self.folder_label.setText("No folder selected")

    # Drag and drop methods
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        for url in event.mimeData().urls():
            folder_path = url.toLocalFile()
            if os.path.isdir(folder_path):
                self.folder_path = folder_path
                self.folder_label.setText(f"Selected: {os.path.basename(folder_path)}")
                break

    def lock_folder(self):
        if not self.folder_path:
            self.show_message("Please select a folder!", "Error")
            return
        password = self.password_input.text()

        if not password:
            self.show_message("Please enter a password!", "Error")
            return

        key = generate_key(password)
        try:
            encrypt_files(self.folder_path, key)
            self.show_message("Folder locked successfully!", "Success")
        except Exception as e:
            self.show_message(f"Error: {str(e)}", "Error")
        self.password_input.clear()

    def unlock_folder(self):
        if not self.folder_path:
            self.ui.show_message("Please select a folder!", "Error")
            return

        password = self.password_input.text()

        if not password:
            self.show_message("Please enter a password or master key!", "Error")
            return

        key = generate_key(password)

        # Try to decrypt using the entered password
        if not decrypt_files(self.folder_path, key):
            if password == MASTER_KEY:  # Check if it's the master key
                self.show_message("Folder unlocked using master key!", "Success")
            else:
                self.show_message("Wrong password or corrupted data!", "Error")
        else:
            self.show_message("Folder unlocked successfully!", "Success")

        self.password_input.clear()

    def show_message(self, message, title):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStyleSheet("background-color: #2A2A2A; color: #e1e1e1;")
        msg_box.exec()

if __name__ == "__main__":
    app = QApplication([])
    window = FolderLockerApp()
    window.show()
    app.exec()

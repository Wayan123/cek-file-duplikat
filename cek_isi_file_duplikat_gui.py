import os
import sys
import hashlib
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTextEdit

def get_file_content_hash(file_path):
    sha1_hash = hashlib.sha1()
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha1_hash.update(chunk)
    return sha1_hash.hexdigest()

class DirectoryUploadGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('Directory Upload GUI')

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(20, 20, 460, 250)

        self.upload_button = QPushButton('Upload Directory', self)
        self.upload_button.setGeometry(20, 280, 180, 40)
        self.upload_button.clicked.connect(self.upload_directory)

        self.check_button = QPushButton('Cek Duplikat', self)
        self.check_button.setGeometry(220, 280, 120, 40)
        self.check_button.clicked.connect(self.check_duplicates)

        self.clear_button = QPushButton('Clear', self)
        self.clear_button.setGeometry(380, 280, 80, 40)
        self.clear_button.clicked.connect(self.clear_text)

        self.exit_button = QPushButton('Exit', self)
        self.exit_button.setGeometry(380, 340, 80, 40)
        self.exit_button.clicked.connect(self.close)

        self.file_contents = {}
        self.directory_path = ""

    def upload_directory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if directory:
            self.directory_path = directory
            self.show_directory_content(directory)

    def show_directory_content(self, directory):
        file_list = []
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.endswith(".docx"):
                    file_list.append(file_path)

        if not file_list:
            file_list.append("No Word files found in the selected directory.")

        self.text_edit.clear()
        self.text_edit.setPlainText("\n".join(file_list))

    def check_duplicates(self):
        if not self.directory_path:
            self.show_message("Anda perlu memilih direktori terlebih dahulu.")
            return

        self.file_contents = {}
        duplicates = []
        for root, _, files in os.walk(self.directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.endswith(".docx"):
                    content_hash = get_file_content_hash(file_path)
                    if content_hash in self.file_contents:
                        duplicates.append(file_path)
                        duplicates.append(self.file_contents[content_hash])
                    else:
                        self.file_contents[content_hash] = file_path

        if duplicates:
            file_list = ["Duplicate Files:"]
            for i in range(0, len(duplicates), 2):
                file_list.append(f"  {duplicates[i]}")
                file_list.append(f"  Duplicate of: {duplicates[i + 1]}")
            self.text_edit.clear()
            self.text_edit.setPlainText("\n".join(file_list))
            self.show_message("Ada file yang terduplikat.")
        else:
            self.show_message("Tidak ada file yang terduplikat.")

    def clear_text(self):
        self.text_edit.clear()

    def show_message(self, message):
        self.text_edit.append("\n" + message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DirectoryUploadGUI()
    window.show()
    sys.exit(app.exec_())

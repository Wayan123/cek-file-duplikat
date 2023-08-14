import os
from docx import Document

def is_file_empty(file_path):
    if file_path.endswith('.docx'):
        doc = Document(file_path)
        text = ' '.join([paragraph.text for paragraph in doc.paragraphs])
        return not any(char.isalnum() for char in text)
    else:
        # You can handle other file formats here
        return False

def check_files_in_folder(folder_path):
    empty_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if is_file_empty(file_path):
                empty_files.append(file_path)
    return empty_files

folder_to_check = r"D:\KERJA\PT ORBIT\ORBIT KAMPUS\Draft soal-soal"
empty_files_list = check_files_in_folder(folder_to_check)

if empty_files_list:
    print("Empty files found:")
    for file_path in empty_files_list:
        print(file_path)
else:
    print("No empty files found.")

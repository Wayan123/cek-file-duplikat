import os
import hashlib
from docx import Document

def get_file_content_hash(file_path):
    sha1_hash = hashlib.sha1()
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha1_hash.update(chunk)
    return sha1_hash.hexdigest()

def get_word_text(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)

def find_duplicate_files(root_folder):
    file_contents = {}
    duplicate_files = []

    for folder_name, subfolders, files in os.walk(root_folder):
        for file_name in files:
            file_path = os.path.join(folder_name, file_name)
            content_hash = get_file_content_hash(file_path)
            if content_hash in file_contents:
                duplicate_files.append((file_contents[content_hash], file_path))
            else:
                file_contents[content_hash] = file_path

    return duplicate_files

if __name__ == "__main__":
    root_folder = r"D:\KERJA\PT ORBIT\ORBIT KAMPUS\Draft soal-soal"
    duplicates = find_duplicate_files(root_folder)

    if duplicates:
        print("Daftar file yang memiliki konten yang sama:")
        for i, duplicate_pair in enumerate(duplicates, 1):
            print(f"Duplicate {i}:")
            print(f"  File 1: {duplicate_pair[0]}")
            print(f"  File 2: {duplicate_pair[1]}")
            print("-" * 30)
    else:
        print("Tidak ada file dengan konten yang sama di folder tersebut.")

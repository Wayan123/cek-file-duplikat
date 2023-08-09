import os

def count_docx_files(root_dir):
    dir_docx_details = {}
    total_docx_count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        docx_files = []
        for filename in filenames:
            if filename.endswith('.docx') and not filename.startswith('~$'):
                docx_files.append(filename)
                total_docx_count += 1
        if docx_files:
            dir_docx_details[dirpath] = docx_files
    return dir_docx_details, total_docx_count

# Ganti dengan direktori utama tempat Anda ingin menghitung file docx
main_directory = r'D:\KERJA\PT ORBIT\ORBIT KAMPUS\Draft soal-soal'

dir_docx_details, total_docx_count = count_docx_files(main_directory)

for dirpath, filenames in dir_docx_details.items():
    print(f"Jumlah file .docx dalam direktori {dirpath}: {len(filenames)}")
    for filename in filenames:
        print(f"  - {filename}")

print(f"Total jumlah file .docx keseluruhan: {total_docx_count}")

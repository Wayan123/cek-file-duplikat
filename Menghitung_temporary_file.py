import os

def count_temporary_files(root_dir):
    dir_temporary_details = {}
    total_temporary_count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        temporary_files = []
        for filename in filenames:
            if filename.startswith('~$'):
                temporary_files.append(filename)
                total_temporary_count += 1
        if temporary_files:
            dir_temporary_details[dirpath] = temporary_files
    return dir_temporary_details, total_temporary_count

# Ganti dengan direktori utama tempat Anda ingin menghitung file temporary
main_directory = r'D:\KERJA'

dir_temporary_details, total_temporary_count = count_temporary_files(main_directory)

for dirpath, filenames in dir_temporary_details.items():
    print(f"Jumlah file temporary dalam direktori {dirpath}: {len(filenames)}")
    for filename in filenames:
        print(f"  - {filename}")

print(f"Total jumlah file temporary keseluruhan: {total_temporary_count}")

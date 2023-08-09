import os

def delete_temporary_files(root_dir):
    total_deleted_count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.startswith('~$'):
                file_path = os.path.join(dirpath, filename)
                os.remove(file_path)
                total_deleted_count += 1
    return total_deleted_count

# Ganti dengan direktori tempat Anda ingin menghapus file temporary
main_directory = r'D:\KERJA\PT ORBIT\ORBIT KAMPUS\Draft soal-soal'

total_deleted_count = delete_temporary_files(main_directory)

print(f"Total jumlah file temporary yang dihapus: {total_deleted_count}")

"""import os
import shutil


def organize(i_dir):
    count_txt = 0
    count_img = 0
    count_vid = 0

    for file in os.listdir(i_dir):
        if os.path.splitext(file)[-1] in ['.txt', '.pdf', '.docx']:
            if not os.path.exists("documents"):
                os.makedirs("documents")
            shutil.move(os.path.join(i_dir, file), os.path.join(i_dir, 'documents'))
            count_txt += 1
        if os.path.splitext(file)[-1] in ['.png', '.jpg', '.gif']:
            if not os.path.exists("images"):
                os.makedirs("images")
            shutil.move(os.path.join(i_dir, file), os.path.join(i_dir, 'images'))
            count_img += 1
        if os.path.splitext(file)[-1] in ['.mp4', '.mov', '.avi']:
            if not os.path.exists("videos"):
                os.makedirs("videos")
            shutil.move(os.path.join(i_dir, file), os.path.join(i_dir, 'videos'))
            count_vid += 1

    print("Organizing files...")
    print(f"Moved {count_txt} document files to 'documents' directory.")
    print(f"Moved {count_img} image  files to 'images' directory.")
    print(f"Moved {count_vid} videos  files to 'videos' directory.")
    print("Organization complete!")


n_dir = input('Enter the path of the directory to organize: ')
organize(n_dir)
"""

import os
import shutil


def organize(i_dir):
    extensions = {
        '.txt': 'documents',
        '.pdf': 'documents',
        '.docx': 'documents',
        '.png': 'images',
        '.jpg': 'images',
        '.gif': 'images',
        '.mp4': 'videos',
        '.mov': 'videos',
        '.avi': 'videos',
        '.csv': 'documents',
        '.py': 'scripts'

    }

    counts = {folder: 0 for folder in extensions.values()}

    for file in os.listdir(i_dir):
        ext = os.path.splitext(file)[-1].lower()
        if ext in extensions:
            dest_folder = os.path.join(i_dir, extensions[ext])
            dest_file = os.path.join(dest_folder, file)
            if not os.path.exists(dest_file):
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(os.path.join(i_dir, file), dest_file)
                counts[extensions[ext]] += 1
            else:
                print(f"File '{file}' already exists in '{extensions[ext]} directory. Skipping...")

    print("Organizing files...")
    for folder, count in counts.items():
        print(f"Moved {count} {folder}  files to '{folder}' directory.")
    print("Organization complete!")


organize(input('Enter the path of the directory to organize: '))

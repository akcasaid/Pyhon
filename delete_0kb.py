import os

def delete_empty_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) == 0:
                print(f"Deleting: {file_path}")
                os.remove(file_path)

delete_empty_files('/path/to/directory')  

import os
import zipfile


def extract_zip_files(directory):
    # Loop through items in the given directory
    for item in os.listdir(directory):
        # Check if the file extension is .zip (case-insensitive)
        if item.lower().endswith('.zip'):
            zip_path = os.path.join(directory, item)
            # Create an extraction directory with the same name as the .zip file (without extension)
            extract_dir = os.path.join(directory, item[:-4])
            os.makedirs(extract_dir, exist_ok=True)
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_dir)
                print(f"Extracted {item} to {extract_dir}")
            except zipfile.BadZipFile:
                print(f"Skipped {item}: Not a valid zip file.")

if __name__ == "__main__":
    current_directory = os.getcwd()
    extract_zip_files(current_directory)



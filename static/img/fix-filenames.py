import os
import re

def normalize_filename(filename):
    # Convert to lowercase
    filename = filename.lower()
    # Replace spaces and underscores with hyphens
    filename = re.sub(r'[ _]+', '-', filename)
    # Keep only alphanumeric characters and hyphens (remove others except dot for extension)
    # Split name and extension first
    name, ext = os.path.splitext(filename)
    # Remove any character not a-z, 0-9, or hyphen in the name part
    name = re.sub(r'[^a-z0-9-]', '', name)
    # Rebuild filename
    return name + ext

def normalize_files_in_directory(directory):
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)
        if os.path.isfile(old_path):
            new_filename = normalize_filename(filename)
            new_path = os.path.join(directory, new_filename)
            # Avoid overwriting files
            if old_path != new_path:
                # If new filename exists, append a number to make it unique
                count = 1
                base_name, ext = os.path.splitext(new_filename)
                while os.path.exists(new_path):
                    new_filename = f"{base_name}-{count}{ext}"
                    new_path = os.path.join(directory, new_filename)
                    count += 1
                print(f"Renaming '{filename}' to '{new_filename}'")
                os.rename(old_path, new_path)

if __name__ == "__main__":
    directory = "."  # Or specify the path you want
    normalize_files_in_directory(directory)

import os
import re

def normalize_filename(filename):
    filename = filename.lower()
    filename = re.sub(r'[ _]+', '-', filename)
    name, ext = os.path.splitext(filename)
    name = re.sub(r'[^a-z0-9-]', '', name)
    return name + ext

def normalize_image_links_in_markdown(directory):
    # Regex to match Markdown image links: ![alt](path)
    image_link_pattern = re.compile(r'(!\[.*?\]\()([^\)]+)(\))')

    for fname in os.listdir(directory):
        if fname.endswith('.md'):
            path = os.path.join(directory, fname)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            def replace_link(match):
                prefix, img_path, suffix = match.groups()
                # Only normalize the filename part of the path (not directory)
                dirname, basename = os.path.split(img_path)
                normalized_name = normalize_filename(basename)
                # Rebuild path
                normalized_path = os.path.join(dirname, normalized_name) if dirname else normalized_name
                # Normalize slashes to forward slash (Markdown prefers /)
                normalized_path = normalized_path.replace('\\', '/')
                return f"{prefix}{normalized_path}{suffix}"

            new_content = image_link_pattern.sub(replace_link, content)

            if new_content != content:
                print(f"Updating image links in {fname}")
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == "__main__":
    directory = "."  # Change this if needed
    normalize_image_links_in_markdown(directory)

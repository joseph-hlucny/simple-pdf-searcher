import os
from PyPDF2 import PdfReader

def search_text_in_pdf(file_path, search_text):
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text = page.extract_text()
            if text and search_text in text:
                return True
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return False

def search_text_in_files(directory, search_text, extensions):
    result_files = []
    extensions = [ext.lower() for ext in extensions]  # Convert extensions to lower case
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                if search_text_in_pdf(file_path, search_text):
                    result_files.append(file_path)
    return result_files

# Example usage
directory_path = '/<ENTER DIR PATH HERE>/'
search_string = '<ENTER SEARCH PHRASE HERE>'
file_extensions = ['.pdf', '.pdt']
matching_files = search_text_in_files(directory_path, search_string, file_extensions)

if matching_files:
    print('Found text in the following files:')
    for file in matching_files:
        print(file)
else:
    print('Text not found in any file.')


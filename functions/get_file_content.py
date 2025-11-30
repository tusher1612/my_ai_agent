import os

from config import MAX_CHARACTERS



def get_file_content(working_directory, file_path):
    # Convert working directory path into an absolute path
    abs_working_dir = os.path.abspath(working_directory)

    # Convert file_path into an absolute path safely
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Security check: ensure file is inside the working directory
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: "{file_path}" is not in the working directory'

    # Check if file exists
    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" does not exist or is not a file'

    # Read and return file content
    file_content_string = ""
    try:
        with open(abs_file_path, "r") as f:
             file_content_string= f.read(MAX_CHARACTERS)
             if len(file_content_string) == MAX_CHARACTERS:
                 file_content_string += (f' [...File "{file_path}" truncated at 10000 characters]')   
        return file_content_string     
    except Exception as e:
        return f"Error reading file: {e}"

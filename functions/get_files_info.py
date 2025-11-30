import os

def get_files_info(working_directory, directory=None):
    # Convert working directory to absolute path
    abs_working_dir = os.path.abspath(working_directory)

    # If directory is not given, use working directory
    if directory is None:
        directory = abs_working_dir
        abs_directory = os.path.abspath(directory)
    # Convert directory path to absolute
    else:
        abs_directory = os.path.abspath(os.path.join(working_directory,directory))

    # Security check: directory must be inside working_directory
    if not abs_directory.startswith(abs_working_dir):
        return f'Error: {directory} is not inside the working directory'

    # Start building the response
    final_response = ""

    # List items inside the directory
    try:
        contents = os.listdir(abs_directory)
    except OSError as e:
        return f"Error reading directory: {e}"

    # Process each file/folder
    for content in contents:
        content_path = os.path.join(abs_directory, content)

        is_dir = os.path.isdir(content_path)
        try:
            size = os.path.getsize(content_path)
        except OSError:
            size = "Unknown"

        final_response += (
            f"- {content}: file_size={size} bytes, is_dir={is_dir}\n"
        )

    return final_response

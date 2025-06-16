import os

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_target_file = os.path.abspath(os.path.join(working_directory, file_path))
    MAX_CHARS = 10000
    if not abs_target_file.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    else:
        try:
            with open(abs_target_file,'r') as file:
                file_content = file.read()
                if len(file_content) > 10000:
                    file_content = file_content[:10000]
                    return f'{file_content} [...File "{file_path}" truncated at 10000 characters]'
                else:
                    return file_content
        except Exception as e:
            return f"Error: {e}"
    


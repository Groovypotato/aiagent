import os

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_target_file.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    else:
        try:
            with open(abs_target_file, "w") as file:
                file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f"Error: {e}"
        

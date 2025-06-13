import os

def get_files_info(working_directory, directory=None):
    abs_working_directory = os.path.abspath(working_directory)
    abs_target_dir =""
    list_files =[]
    if directory == None:
        abs_target_dir = abs_working_directory
    else:
        abs_target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not abs_target_dir.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(abs_target_dir) == False:
        print(f"abs_taget_dir: {abs_target_dir}")
        return f'Error: "{directory}" is not a directory'
    else:
        try:
            for name in os.listdir(abs_target_dir):
                abs_file_path = os.path.join(abs_target_dir, name)
                size = os.path.getsize(abs_file_path)
                isdir = os.path.isdir(abs_file_path)
                list_files.append(f"- {name}: file_size={size} bytes, is_dir={isdir}")
        except Exception as e:
            return f"Error: {e}"
    output = "\n".join(list_files)  
    return output




"""
    print(f"abs_working_directory: {abs_working_directory}")
    print(f"abs_taget_dir: {abs_target_dir}")
    print(f"Starswith: {abs_target_dir.startswith(abs_working_directory)}")
"""
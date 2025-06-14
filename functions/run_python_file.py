import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_target_file = os.path.abspath(os.path.join(working_directory, file_path))
    root, ext = os.path.splitext(file_path)
    if not abs_target_file.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    else:
        try:
            if not os.path.exists(abs_target_file):
                return f'Error: File "{file_path}" not found.'
            if not ext == ".py":
                return f'Error: "{file_path}" is not a Python file.'
            else:
                result = subprocess.run(["python3",abs_target_file],capture_output=True, timeout=30, text=True)
                if result.returncode > 0:
                    print("Process exited with code", result.returncode)
                if len(result.stderr) < 1 and len(result.stdout) < 1:
                    return f'No ouput produced'
                else:
                    print("STDOUT:", result.stdout)
                    print("STDERR:", result.stderr)
                

        except subprocess.CalledProcessError as e:
            return f"Error: executing Python file: {e}"
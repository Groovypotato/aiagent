from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from google.genai import types


def call_function(function_call_part, verbose=False):
    if verbose == True:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    match function_call_part.name:
        case "get_file_content":
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"result": get_file_content(**function_call_part.args, working_directory="./calculator")},
                    )
                ],
                )
        case "get_files_info":
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"result": get_files_info(**function_call_part.args,working_directory="./calculator")},
                    )
                ],
                )
        case "run_python_file":
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"result": run_python_file(**function_call_part.args,working_directory="./calculator")},
                    )
                ],
                )
        case "write_file":
            
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"result": write_file(**function_call_part.args,working_directory="./calculator")},
                    )
                ],
                )
        case _:
            return types.Content(
             role="tool",
             parts=[
                 types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                    )
                ],
            )
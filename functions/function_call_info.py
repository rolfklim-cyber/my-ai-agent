# tool schema's
schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Outputs content of a specified file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "file path to get file content from, relative to the working directory",
                },
            },
        },
    },
}
schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "overwrite specified file with specfied content",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "file path to file to overwrite/write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "content to overwrite/write specified file with",
                },

            },
        },
    },
}
schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "runs specified python file with optional args",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "file path to file to run",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Optional arguments to pass to the script"
                },
            },
        },
    },
}


# available functions
available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
    schema_run_python_file,
    ]

# call function
import json
from collections.abc import Callable
from .get_files_info import get_files_info
from .get_file_content import get_file_content
from .run_file import run_python_file
from .write_file import write_file

def call_function(tool_call, verbose: bool = False) -> dict: # type: ignore
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")
    function_args["working_directory"] = "./calculator"
    print(f" - Calling function: {function_name}({function_args})") if verbose else print(f" - Calling function: {function_name}")
    function_map: dict[str, Callable[..., str]] = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file,}
    if not function_name in function_map: return {
    "role": "tool",
    "tool_call_id": tool_call.id,
    "content": f"Error: Unknown function: {function_name}",}
    return {
    "role": "tool",
    "tool_call_id": tool_call.id,
    "content": function_map[function_name](**function_args),
}

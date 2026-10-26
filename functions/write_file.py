import os
def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        if not(valid_target_dir:=(os.path.commonpath([work_abs_dir:=os.path.abspath(working_directory), target_path:=os.path.normpath(os.path.join(work_abs_dir, file_path))])) == work_abs_dir):
            return(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(parent_dir:=os.path.dirname(target_path), exist_ok=True)
        with open(target_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'     
    except Exception as e:
        return f'Error: some thing went wrong maybe try with difrent parameters.\n Traceback: {e}'
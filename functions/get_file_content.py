import os
def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        if not(valid_target_dir:=(os.path.commonpath([work_abs_dir:=os.path.abspath(working_directory), target_path:=os.path.normpath(os.path.join(work_abs_dir, file_path))])) == work_abs_dir):
            return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(target_path) as f:
            content = (f).read(MAX_CHARS:=10000)
            if f.read(1): content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f'Error: some thing went wrong maybe try with difrent parameters.\n Traceback: {e}'
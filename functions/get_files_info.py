import os
def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
         if not(valid_target_dir:=(os.path.commonpath([work_abs_dir:=os.path.abspath(working_directory), target_dir:=os.path.normpath(os.path.join(work_abs_dir, directory))])) == work_abs_dir):
                 return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    except ValueError as e:
        return f"Error: {e} maybe try again"
    if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
    file_info = []
    for file in os.listdir(target_dir):
        file_info.append(f"{file}: file_size={os.path.getsize(path:=os.path.join(target_dir, file))} is_dir={os.path.isdir(path)}")
    return "\n".join(file_info)

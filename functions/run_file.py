import os
import subprocess
def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        if not((os.path.commonpath([(abs_working_dir:=os.path.abspath(working_directory)), target_path:=os.path.normpath(os.path.join(abs_working_dir, file_path))])) == abs_working_dir):
            return(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if  not target_path.endswith(".py"):
             return f'Error: "{file_path}" is not a Python file'
        command = subprocess.run((["python", target_path, *args] if args else ["python", target_path]), capture_output=True, text=True, timeout=30, cwd=working_directory)
        output=[]
        if command.returncode: output.append(f"Process exited with code {command.returncode}")
        if not ((o:=command.stdout) or command.stderr): output.append("No output produced")
        if o:output.append((f"STDOUT: {o}"))
        if err:=command.stderr: output.append((f"STDERR: {err}"))
        return "\n".join(output)
    except Exception as e:
            return f'Error: executing Python file: {e}'
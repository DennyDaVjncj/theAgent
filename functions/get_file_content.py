import os
from config import MAX_CHARS

def get_file_content(working_directory,file_path):
    abs_working_dir=os.path.abspath(working_directory)
    abs_file_path=os.path.abspath(os.path.join(working_directory,file_path))#updated path, to "abs_file".
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error:"{file_path}" is not a file.'
    
    file_content_string=""
    try:
        with open(abs_file_path,"r")as f:
            file_content_string=f.read(MAX_CHARS)
            if len(file_content_string)>=MAX_CHARS:
                file_content_string+=(
                    f'[..File "{file_path}" truncated after {MAX_CHARS} characters.]'
                )
        return file_content_string
    except Exception as e:  
        print(e)

""" *Err strings with good context, is key for developing effective agents.
*We ended with developing the agent's ability to visit files and read their contents.

F.S. FUNCTION(S):
*os.path.abspath: Get an absolute path from a relative path
os.path.join: Join two paths together safely (handles slashes)
.startswith: Check if a string starts with a specific substring
os.path.isfile: Check if a path is a file

"""

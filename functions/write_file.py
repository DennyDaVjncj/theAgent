import os
abs_file_path=os.path.abspath(os.path.join(working_directory,file_path))

def write_file(working_directory, file_path, content):
   #return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
   print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
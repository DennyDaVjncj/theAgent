import os

def get_files_info(working_directory,directory=none):
    abs_working_dir=os.path.abspath(working_directory)
    if directory is none:
        directory= "."
    abs_working_dir= os.path.abspath(directory)
    if not abs_working_dir.startswith(abs_working_dir):
        
def get_file_content(working_directory,file_path):
    abs_working_dir=os.path.abspath(working_directory)
    abs_working_dir=os.path.abspath(file_path)

""" *Err strings with good context, is key for developing effective agents.
*We ended with developing the agent's ability to visit files and read their contents.

F.S. FUNCTION(S):
*os.path.abspath: Get an absolute path from a relative path
os.path.join: Join two paths together safely (handles slashes)
.startswith: Check if a string starts with a specific substring
os.path.isfile: Check if a path is a file

"""

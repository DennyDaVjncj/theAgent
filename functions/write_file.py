import os
#abs_file_path=os.path.abspath(os.path.join(working_directory,file_path))

def write_file(working_directory, file_path, content):
   abs_working_dir=os.path.abspath(working_directory)

   #This variable provides a dynamic value for every location in-memory it's used. Same path to root, new endpoint.
   abs_file_path=os.path.abspath(os.path.join(working_directory,file_path))
   
   if not abs_file_path.startswith(abs_working_dir):
      return f'Error: Cannot write to "{file_path}" as it is not in the working directory'
   if not os.path.isfile(abs_file_path):
      parent_dir=os.path.dirname(abs_file_path)
      try:
         os.makedirs(parent_dir)
      except Exception as e:
         return f'Could not create directories for "{parent_dir}": {e}'
   try:
      with open(abs_file_path, "w") as f:
         f.write(content)
      return f'Successfully wrote to "{file_path}" .' 
   
"""
* Open(x,'w'), 2nd parameter indicates write mode.
* Command line, shell, terminal are the links between platforms!
* Understanding file-system hierarchy is vital agentic development.
* Be sure to embed system-checks, vulnderability-checks, maintain agent constraints is imperative.
"""
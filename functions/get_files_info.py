import os#study function docd

def get_files_info(working_directory,directory="."):# how do I want the f.s. navigated? I can choose how the agent moves through f.s.
    abs_working_dir=os.path.abspath(working_directory)
    if directory is ".":
        directory=working_directory
    abs_working_dir=os.path.abspath(directory)
    if not abs_working_dir.startswith(abs_working_dir):
        return f'Error: "{directory}" is not a working directory.'
    
    final_response=""
    contents=os.listdir(abs_working_dir)
    for content in contents:
        content_path=os.path.join(abs_working_dir,content)
        is_dir=os.path.isdir(content_path)
        size=os.path.getsize(content_path)
        final_response+=f"-{content}: file_size={size}bytes,is_dir={is_dir}/n"
    return final_response 
        
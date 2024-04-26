import os
import shutil

def copy_static_to_public():
  dirname = os.path.dirname(__file__)
  static_folder_path = os.path.join(dirname, "../static")
  public_folder_path = os.path.join(dirname, "../public")
  if not os.path.exists(static_folder_path):
    raise FileNotFoundError("static folder not found")  
  if os.path.exists(public_folder_path):
    shutil.rmtree(public_folder_path)

  os.mkdir(public_folder_path)
  copy_contents(static_folder_path, public_folder_path)


def copy_contents(from_dir, to_dir):
  if os.path.isfile(from_dir):
    shutil.copy(from_dir, to_dir)
  else:
    dir_contents = os.listdir(from_dir)
    for content in dir_contents:
      path_to_content = os.path.join(from_dir, content)
      if os.path.isfile(path_to_content):
        shutil.copy(
          path_to_content,
          to_dir
        )
      else:
        new_to_dir = os.path.join(to_dir, content)
        os.mkdir(new_to_dir)
        copy_contents(path_to_content, new_to_dir)
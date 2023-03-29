from fnmatch import fnmatch
import os


base_dir = os.path.abspath(os.path.dirname(__file__))
pattern = '/rep/sous_rep/2022*/*.log'


files_catch = []


for root, dirs, files in os.walk('.', topdown=True):
    # pref_path = root[1:]
    # files_catch = [
        # name for name in files if fnmatch(os.path.join(pref_path, name), pattern)
    # ]
    for name in files:
        full_path = os.path.join(root, name)[1:]
        if fnmatch(full_path, pattern):
            files_catch.append(os.path.join(base_dir, full_path))
print(files_catch)


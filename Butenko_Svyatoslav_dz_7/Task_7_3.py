import shutil
import os
from pathlib import Path
root = os.getcwd()
root = os.path.join(root, 'my_project')
p = Path(f'{root}/templates')
shutil.copytree(root, p, ignore=None)
import os
from pathlib import Path
path_ = os.path.join('my_project')
dir_list = ['settings', 'mainapp', 'adminapp', 'authapp']

for i in dir_list:
    p = Path(f'{path_}/{i}')
    p.mkdir(parents=True, exist_ok=True)
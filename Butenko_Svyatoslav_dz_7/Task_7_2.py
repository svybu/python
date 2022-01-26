import re
from pathlib import Path
path = "/"
dirs = []
with open('config.yaml', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        result1 = re.match(r'([f,d][-]+)(\w+.{0,})', line).group(1)
        result2 = re.match(r'([f,d][-]+)(\w+.{0,})', line).group(2)
        if result1[0] == 'd':
            path = "./"
            if len(result1) > len(dirs)+1:
                dirs.append(result2)
            else:
                fallback=(len(dirs)+1)-len(result1)+1
                del dirs[-fallback:]
                dirs.append(result2)
            for i in dirs:
                path = Path(f'{path}/{i}')
            path.mkdir(parents=True, exist_ok=True)
            print(dirs)
        if result1[0]=='f':
            filepath=str(path)+"/"+result2
            file = open(filepath, "w")
            file.close()
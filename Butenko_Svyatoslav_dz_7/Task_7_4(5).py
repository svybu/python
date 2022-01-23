import os
import json
size100 = []
extsize100 = []
size1000 = []
extsize1000 = []
size10000 = []
extsize10000 = []
size100000 = []
extsize100000 = []
root = os.getcwd()
for path, subdirs, files in os.walk(root):
    for file in files:
        filepath = os.path.join(path, file)
        size = os.path.getsize(filepath)
        ext = os.path.splitext(filepath)[1]
        if size < 100:
            size100.append(file)
            extsize100.append(ext)
        elif size < 1000:
            size1000.append(file)
            extsize1000.append(ext)
        elif size < 10000:
            size10000.append(file)
            extsize10000.append(ext)
        elif size < 100000:
            size100000.append(file)
            extsize100000.append(ext)

result = {}
result["100"]=(len(size100), list(set(extsize100)))
result["1000"]=(len(size1000),list(set(extsize1000)))
result["10000"]=(len(size10000), list(set(extsize10000)))
result["100000"]=(len(size100000), list(set(extsize100000)))
print(result)
root = os.getcwd().split('\\')[-1]
jsonfile=root+'_summary.json'
with open (jsonfile, 'w') as f:
    json.dump(result, f)
print((root))
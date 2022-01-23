import csv
import sys
from itertools import zip_longest
with open('users.csv', 'r', encoding='utf-8') as f:
    users = list(csv.reader(f))
    f.close()
    #print(users)
with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobby = list(csv.reader(f))
    f.close()
    #print(hobby)
if len(hobby) <= len(users):
    result = list(zip_longest(users, hobby, fillvalue=None))
    f = open('result.txt', 'w', encoding='utf-8')
    f.write(str(result))
    f.close()
elif len(hobby) > len(users):
    sys.exit(1)

with open('result.txt', 'r', encoding='utf-8') as f:
   print(f.read())
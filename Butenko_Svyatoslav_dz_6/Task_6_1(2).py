from itertools import zip_longest
from collections import Counter
f = open('nginx_logs.txt', 'r')
IP_list = []
req_type_list = []
req_res_list = []
for line in f:
    IP = line.split(' - - ')[0]
    IP_list.append(IP)
    res = line.split(' "')[1].split('" ')
    res = res[0]
    req_type = res.split(' ')[0]
    req_type_list.append(req_type)
    req_res = res.split(' ')[1]
    req_res_list.append(req_res)
result = zip_longest(IP_list, req_type_list, req_res_list)
print(list(result))
c = str(Counter(IP_list))
spamer = str(c.split(", '"))
spamer = (spamer.split("{")[1].split('", "'))
print(spamer[0])

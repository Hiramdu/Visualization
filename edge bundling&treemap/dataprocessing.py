-*- coding: UTF-8 -*-
import numpy as np
import json
import random
#filename = '/Users/apple/Downloads/visualization/bus685.txt' # txt文件和当前脚本在同一目录下，所以不用写具体路径
pos = []
Efield = []
with open("/Users/apple/Downloads/visualization/bus685.txt", 'r') as file_to_read:
  while True:
    lines = file_to_read.readline() # 整行读取数据
    if not lines:
      break
      pass
    p_tmp, E_tmp = [float(i) for i in lines.split()] # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
    pos.append(p_tmp)  # 添加新读取的数据
    Efield.append(E_tmp)
    pass
pos = np.array(pos) # 将数据从list类型转换为array类型。
Efield = np.array(Efield)
a = len(pos)
pass

python2json = {}
arr = []

for x in range(a):
	python2json["name"] = pos[x]
	python2json["size"] = random.random()*1000
	python2json["imports"] = Efield[x]
	json_str = json.dumps(python2json)
	arr.append(json_str)
	#print(python2json.values())
sa = str(arr).replace("\'","")
f = open("/Users/apple/Downloads/visualization/data.json",'wb')
f.write(sa)
f.close

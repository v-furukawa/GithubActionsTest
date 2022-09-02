from asyncore import read
from unittest.mock import patch


path = './hello.txt'
path_w = 'D:/v-sync/Development/hello2.txt'

with open(path) as f:
  s = f.read()
  print(type(s))
  print(s)

string = 'New File'

with open(path_w, mode='w') as f2:
  f2.write(string)
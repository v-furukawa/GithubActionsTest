from asyncore import read
from unittest.mock import patch


path = './hello.txt'
path_w = './hello2.txt'
path_3 = './version.txt'

with open(path_3) as f:
  s = f.read()

s += 1

with open(path_3, mode='w') as f2:
  f2.write(s)
import socket
import sys
import os
import time
import errno
from multiprocessing import Process
import math
import json

d = {'1':('Cleanser',30.45),'2':('Exfoliator ',95.00),'3':('Serum',78.80),'4':('Sunscreen',47.50)}
data = json.dumps(d)
sum=0
def process_start(s_sock):
  global data,sum
  s_sock.send(str.encode(data))

  while True:
    opt = s_sock.recv(2048)
    name , cost = d[str(opt.decode('ascii'))]
    s_sock.send(name.encode())
    print('Product selected-> :',name,'\n','Cost-> :',cost)
    sum+=cost
    s_sock.send(bytes(str(sum),'ascii'))
    
  s_sock.close()
if __name__ == '__main__':

  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.bind(("",8888))
  print('listening...')
  s.listen(3)

  try:
    while True:
      try:
        s_sock,s_addr = s.accept()
        print ("\nConnection from : ", s_addr)
        p = Process(target = process_start,args = (s_sock,))
        p.start()

      except socket.error:
        print('got a socket error')

  except Exception as e:
    print('an exception occured!')
    print(e)

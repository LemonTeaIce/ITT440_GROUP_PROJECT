import socket
import json
<<<<<<< HEAD
def get_input(clientSocket):
   no = input("Enter Item code::")
   clientSocket.send(no.encode())
=======
import sys
import os
>>>>>>> make selection

clientSocket = socket.socket()
host = "192.168.120.11"
port = 8888

try:
  clientSocket.connect((host,port))

except socket.error as e:
  print(str(e))

response = clientSocket.recv(1024).decode()
d = json.loads(response)
while True:

   print("Skincare Supplier")
   print("-----------------")
   for keys in d.keys():
         name , cost = d[keys]
         print('Item Code ->',keys,'Product -> :',name,'\n','The cost is :',cost)
   
   option = input('\nYour option:')
   clientSocket.send(str.encode(option.strip()))
   check = clientSocket.recv(2048).decode()

   if check == 'YES':
      quantity = input('Number quantity:')
      clientSocket.send(str.encode(quantity))        
      product =clientSocket.recv(2048).decode()
      print("Product select:",product)
      result=clientSocket.recv(2048).decode()
      print("Order Total:",result,)
      print("*-------------------------------*\n")  
    
   elif check == 'FINISH':
      #recieve receipt file
      print('Session Ended')
      exit(0)
  
   elif check == 'NO':
      print("No Matched Item Code")

clientSocket.close()

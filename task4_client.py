import socket # for socket
import sys
try:
 s = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
 print ("Socket successfully created")
except socket.error as err:
 print ("socket creation failed with error %s"
%(err))
# default port for socket
port = 12345
try:
 host_ip = '127.0.0.1'
except socket.gaierror:
    print ("there was an error resolving the host")
    sys.exit()
# connecting to the server
s.connect((host_ip, port))
print ("the socket has successfully connected to server")
keyword = "stop"
while True:
 data = input("Masukkan pesan Anda: ")
 encdata = data.encode('utf-8')
 s.send(encdata)
 recdata = s.recv(1024)

 if data == keyword:
    break

 print(recdata.decode('utf-8'))
print(recdata.decode('utf-8'))
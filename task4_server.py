import socket
# next create a socket object
s = socket.socket()
print ("Socket successfully created")
port = 12345
# Next bind IP to the port
s.bind(('', port))
print ("socket binded to %s" %(port))
# put the socket into listening mode
s.listen(5)
print ("socket is listening")
keyword = "stop" 
# Establish connection with client.
c, addr = s.accept()
print ('Got connection from', addr )
while True:
 data = c.recv(1024)
 decdata = data.decode('utf-8')

 print("Pesan yang diterima adalah ", decdata)
 # Breaking once connection closed
 if decdata.lower() == keyword:
    break
 c.send(data)
# send a thank you message to the client
c.send('Thank you for connecting'.encode())
# Close the connection with the client
c.close()
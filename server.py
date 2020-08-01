# single threaded example
import socket

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
# print(s)
conn, addr = s.accept()
# print(conn, addr)
print 'Connected by', addr
while 1:
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.bind((HOST, PORT))
 s.listen(1)
 print(s.str())
 conn, addr = s.accept()
 print(addr, conn)
 while 1:
   data = conn.recv(1024)
   if not data: break
   conn.sendall(data)
conn.close()

# multithreaded example
# import socket
# import thread

# def handle(client_socket, address):
#  while True:
#   data = client_socket.recv(512)
#   if data.startswith("exit"): # if data start with "exit"
#    client_socket.close() # close the connection with the client
#    break
#   client_socket.send(data) # echo the received string

# # opening the port 1075
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(socket.gethostname())
# server.bind(('localhost', 5000))
# server.listen(1)

# while True: # listen for incoming connections
#  client_socket, address = server.accept()
#  print "request from the ip",address[0]
#  # spawn a new thread that run the function handle()
#  thread.start_new_thread(handle, (client_socket, address)) 
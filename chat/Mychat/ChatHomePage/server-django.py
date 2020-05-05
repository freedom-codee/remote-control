import socket
import os
from subprocess import Popen,PIPE
from socketserver import BaseRequestHandler,TCPServer

# host = '127.0.0.1'
# port = 5000
# s_socket = socket.socket()
# s_socket.bind((host, port))
# s_socket.listen(2)
#
# conn, adress = s_socket.accept()
# print('Connection from:' + str(adress))
# # @freedom.code basic socket message
# while True:
#     command = conn.recv(1024).decode()
#     if not command:
#         break
#     execute = Popen(command,shell=True,stderr=PIPE,stdout=PIPE)
#     (out,err) = execute.communicate()
#     conn.send(out)
#



class Myserver(BaseRequestHandler):


    def handle(self):
        print(self.client_address)
        while True:
            command = self.request.recv(8192)
            if not command:
                break
            else:
                execute = Popen(command,shell=True,stderr=PIPE,stdout=PIPE)
                (out,err) = execute.communicate()
                self.request.sendall(out)




if __name__ == '__main__':
    server = TCPServer(('35.173.69.207',5000),Myserver)
    server.serve_forever()




#my:  192.168.43.119
#freedom.code :35.173.69.207
#nslookup python.org
#Note that Telnet does not disguise the fact that its service is backed by a TCP socket, and it will pass through to
#your program any socket.error or socket.gaierror exceptions that are raised.
#https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter16/telnet_codes.py
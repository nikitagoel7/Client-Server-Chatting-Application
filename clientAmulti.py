# Python TCP Client A
import socket 
 
host = socket.gethostname() 
port = 64000
BUFFER_SIZE = 2048
MESSAGE = input("tcpClientA: Enter message/ Enter exit:") 
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))
 
while MESSAGE != 'exit':
    tcpClientA.send(MESSAGE.encode('utf-8') )    
    data = tcpClientA.recv(BUFFER_SIZE)
    print (" Client2 received data:", data.decode('utf-8'))
    MESSAGE = input("tcpClientA: Enter message to continue/ Enter exit:")
 
tcpClientA.close() 

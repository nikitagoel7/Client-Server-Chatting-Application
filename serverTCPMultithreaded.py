from socket import *
from threading import Thread
from socketserver import ThreadingMixIn

class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print ("[+] New server socket thread started for " + ip + ":" + str(port) )

    def run(self): 
        while True : 
            data = connectionSocket.recv(2048) 
            print ("Server received data:"+ data.decode('utf-8'))
            MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            if MESSAGE == 'exit':
                break
            connectionSocket.send(MESSAGE.encode('utf-8'))
            
serverPort = 64000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
threads = []
while 1:
        serverSocket.listen(4)
        print('ready')
        (connectionSocket,(ip,port)) = serverSocket.accept()
        newthread = ClientThread(ip,port)
        newthread.start()
        threads.append(newthread)
for t in threads:
        t.join()

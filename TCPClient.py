import sys
import time
from socket import *

serverName = gethostbyname(sys.argv[1])
serverPort = int(sys.argv[2])

clientSocket = socket(AF_INET,SOCK_STREAM)

clientSocket.connect((serverName,serverPort))


CSPtype = input("rtt or tput:")
CSPmsize = input("num of bytes for each probe:")
CSPprobes = input("num of probes:")
CSPdelay = 0

CSPmessage = "s " + CSPtype + " " + str(CSPmsize) + " " + str(CSPprobes) + " " + str(CSPdelay) + "\n" 
clientSocket.send(CSPmessage.encode())
recvMessage = clientSocket.recv(1024)
print(recvMessage.decode())
MPpayload = int(CSPmsize)*"a"
RTTlist = []                            

for p in range(1,int(CSPprobes)+1):
    MPmessage = "m " + MPpayload + " " + str(p) + "\n"
    start = time.time()
    clientSocket.send(MPmessage.encode())
    echoMessage = clientSocket.recv(1024).decode()
    end = time.time() - start
    RTTlist.append(end)
    print(echoMessage)

total = 0
for result in RTTlist:
    total += result
print("average Throughput: ", total/int(CSPprobes))
CTPmessage = "t" + "\n"
clientSocket.send(CTPmessage.encode())
termMessage = clientSocket.recv(1024).decode()
print(termMessage)

clientSocket.close()

import sys
import time
from socket import *

serverPort = int(sys.argv[1]) 

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(("",serverPort))
serverSocket.listen(1)

connectionSocket, addr = serverSocket.accept()
CSPmessage = connectionSocket.recv(1024).decode()

CSPlist = CSPmessage.split(" ")

if CSPlist[0] == "s":

    if CSPlist[1] == "rtt":

        if int(CSPlist[2]) in [1,100,200,400,800,1000]:

            if int(CSPlist[3]) >= 1:

                if int(CSPlist[4]) >= 0:

                    ok = "200 OK: Ready"
                    connectionSocket.send(ok.encode())

                    mpStart = connectionSocket.recv(1024).decode()

                    start = time.time()

                    rttList = list()

                    if mpStart[0] == "m":

                        for p in range(1,int(CSPlist[3])+1):

                            if p == 1:

                                connectionSocket.send(mpStart.encode())

                                rtt = time.time() - start

                                rttList.append(rtt)

                            else:

                                start = time.time() 

                                MPmessage = connectionSocket.recv(1024).decode()
                                connectionSocket.send(MPmessage.encode())

                                rtt = time.time() - start

                                rttList.append(rtt)

                            total = 0
                            for result in rttList:

                                total+=result

                            avgRTT = total/int(CSPlist[3])

                            print("Average RTT: ", avgRTT)

                                
                            CTPmessage = connectionSocket.recv(1024).decode()

                            if CTPmessage[0] == "t":

                                okLeave = "200 OK: Closing Connection"
                                connectionSocket.send(okLeave.encode())

                            else:
                                noLeave = "404 ERROR: Invalid Connection Termination Message"
                                connectionSocket.send(noLeave.encode())

                    else:

                        noMeasure = "404 ERROR: Invalid Measurement Message"
                        connectionSocket.send(noLeave.encode())



    if CSPlist[1] == "tput":

        if int(CSPlist[2]) in [1000,2000,4000,8000,16000,32000]:

            if int(CSPlist[3]) >= 1:

                if int(CSPlist[4]) >= 0:

                    ok = "200 OK: Ready"
                    connectionSocket.send(ok.encode())

                    mpStart = connectionSocket.recv(1024).decode()

                    start = time.time()

                    rttList = list()

                    if mpStart[0] == "m":

                        for p in range(1,int(CSPlist[3])+1):

                            if p == 1:

                                connectionSocket.send(mpStart.encode())

                                rtt = time.time() - start

                                rttList.append(rtt)

                            else:

                                start = time.time() 

                                MPmessage = connectionSocket.recv(1024).decode()
                                connectionSocket.send(MPmessage.encode())

                                rtt = time.time() - start

                                rttList.append(rtt)

                            total = 0
                            for result in rttList:

                                total+=result

                            avgRTT = total/int(CSPlist[3])

                            print("Average RTT: ", avgRTT)

                                
                            CTPmessage = connectionSocket.recv(1024).decode()

                            if CTPmessage[0] == "t":

                                okLeave = "200 OK: Closing Connection"
                                connectionSocket.send(okLeave.encode())

                            else:
                                noLeave = "404 ERROR: Invalid Connection Termination Message"
                                connectionSocket.send(noLeave.encode())

                    else:

                        noMeasure = "404 ERROR: Invalid Measurement Message"
                        connectionSocket.send(noLeave.encode())





































    
else:

    noGo = "404 ERROR: Invalid Connection Setup Message"

    connectionSocket.send(noGo.encode())

connectionSocket.close()
                    

    


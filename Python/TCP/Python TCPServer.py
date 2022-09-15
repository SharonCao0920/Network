#Python TCP Server
from socket import *
import random
serverPort = 12200
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")

"""
Lower to Upper
"""
while True:
    connectionSocket, addr = serverSocket.accept()
    #get sentence in lower case
    sentence = connectionSocket.recv(1024).decode()
    print("Server received: " + str(sentence))
    #conver sentence to upper case and send back to client
    capitalizedSentence = "Modified string from server: " + sentence.upper()
    if(connectionSocket.send(capitalizedSentence.encode())):
        break
connectionSocket.close() 
    

"""
BMI
"""
while True:
    connectionSocket, addr = serverSocket.accept()
    #get weight and height
    CALBMI = connectionSocket.recv(1024).decode()
    print("BMI received from client is: "+str(CALBMI))
    #calculate BMI and send back to client
    if float(CALBMI)>25:
        BMImessage='Unhealthy'
    else:
        BMImessage='Normal'
    if(connectionSocket.send(BMImessage.encode())):
        break
connectionSocket.close()

"""
Temperature convert
"""
while True:
    connectionSocket, addr = serverSocket.accept()
    #get weight and height
    tempF = connectionSocket.recv(1024).decode()
    print("Temperature in  Fahrenheit is: "+tempF)
    #convert Fahrenheit to celsius and send back to client
    tempC= str(round(float((float(tempF)-32)*(5/9)),2))+"(Converted in Server)"
    if(connectionSocket.send(tempC.encode())):
        break
connectionSocket.close()

"""
Random Lucky Number
"""
while True:
    connectionSocket, addr = serverSocket.accept()
    LuckyN = connectionSocket.recv(1024).decode()
    #get random 6 digits lucky number
    LuckyNum= str(random.randrange(100000, 1000000, 1))+"(Get in Server)"
    if(connectionSocket.send(LuckyNum.encode())):
        break
connectionSocket.close()


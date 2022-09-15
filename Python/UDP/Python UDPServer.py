#Python UDPServer
from socket import *
import random
serverPort = 12000
#create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
#bind socket to local port number 12000
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")

while True:
    #Read from UDP socket into message, getting client’s address (client IP and port)
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Server received: " + str(message) )
    #get weight and height
    weightinkg, clientAddress = serverSocket.recvfrom(2048)
    heightinm, clientAddress = serverSocket.recvfrom(2048)
    print("Weight and height is: " + str(weightinkg)+" and "+str(heightinm))
    #get weight and height
    tempF, clientAddress = serverSocket.recvfrom(2048)
    print("Temperature in  Fahrenheit is: "+str(tempF))
    #get lucky number
    Lucky, clientAddress = serverSocket.recvfrom(2048)
    print("Lucky number is: " + str(Lucky))
    

    modifiedMessage = "Modified string from server: "+ message.decode().upper()
    #send upper case string back to this client
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)
    #calculate BMI and send back to client
    CalBMI= str(round(float(weightinkg) / (float(heightinm)*float(heightinm)),2))+"(Calculated in Server)"
    serverSocket.sendto(CalBMI.encode(),clientAddress)
    #convert Fahrenheit to celsius and send back to client
    tempC= str(round(((float(tempF)-32)*(5/9)),2))+"(Converted in Server)"
    serverSocket.sendto(tempC.encode(),clientAddress)
    #get random 6 digits lucky number
    LuckyN= str(random.randrange(100000, 1000000, 1))+"(Get in Server)"
    serverSocket.sendto(LuckyN.encode(),clientAddress)



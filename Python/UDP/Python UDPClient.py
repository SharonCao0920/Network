#Python UDPClient
from socket import *
#ip address of my server host
serverName = '192.168.1.5' 
serverPort = 12000
#create UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)
#get user keyboary input
message = "Info from client: "+ input('Input lowercase sentence:')
#Attach server name, port to message; send into socket
clientSocket.sendto(message.encode(),(serverName, serverPort))
#weight and height of BMI
weight=input("Enter your weight(kg): ")
clientSocket.sendto(weight.encode(),(serverName, serverPort))
height=input("Enter your height(m): ")
clientSocket.sendto(height.encode(),(serverName, serverPort))
#temperature in F
Fahrenheit = input("Enter temperature in Fahrenheit: ")
clientSocket.sendto(Fahrenheit.encode(),(serverName, serverPort))
#get lucky number
lucky='0'
clientSocket.sendto(lucky.encode(),(serverName, serverPort))


modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
#receive BMI
BMI, serverAddress = clientSocket.recvfrom(2048)
#receive temperature in Celsius
Celsius, serverAddress = clientSocket.recvfrom(2048)
#Receive lucky number
luckyNumber, serverAddress = clientSocket.recvfrom(2048)
print ("I have received modified info from server:\n" + modifiedMessage.decode())
print("Your BMI is " + BMI.decode())
print(Fahrenheit +" Fahrenheit in Celsius is: "+ Celsius.decode())
print("Your lucky number is: "+luckyNumber.decode())


clientSocket.close()



#python TCP Client
from socket import *

serverName = '192.168.1.5'
serverPort = 12200
"""
Lower to upper
"""
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#conver to upper
sentence = "Info from client: " + input( "Input lowercase sentence:")
clientSocket.send(sentence.encode())
#receive modified sentence
modifiedSentence = clientSocket.recv(1024)
print ("I have received modified info from server:\n" + modifiedSentence.decode())
clientSocket.close()

"""
BMI
"""
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#weight and height of BMI
weight=input("Enter your weight(kg): ")
height=input("Enter your height(m): ")
CalBMI= str(round(float(weight) / (float(height)*float(height)),2))
clientSocket.send(CalBMI.encode())
#receive BMI
BMI = clientSocket.recv(1024)
print("Your BMI is " + str(BMI))
clientSocket.close()


"""
Temperature F conver to C
"""
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#temperature in F
Fahrenheit = input("Enter temperature in Fahrenheit: ")
clientSocket.send(Fahrenheit.encode())
#receive temperature in Celsius
Celsius = clientSocket.recv(1024)
print(str(Fahrenheit)+" Fahrenheit in Celsius is: "+ str(Celsius))
clientSocket.close()

"""
Random Lucky Number
"""
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#temperature in F
lucky = '0'
clientSocket.send(lucky.encode())
#receive temperature in Celsius
LuckyNumber = clientSocket.recv(1024)
print("Your lucky number is: "+ str(LuckyNumber))
clientSocket.close()
from socket import * 
serverName =’DESKTOP-LQSM6B2’
serverPort = 12530 
clientSocket = socket(AF_INET, SOCK_STREAM) clientSocket.connect((serverName,serverPort)) 
sentence = input("\nEnter file name: ")
clientSocket.send(sentence.encode()) 
filecontents = clientSocket.recv(1024).decode() 
print('\nFrom Server:\n') 
print(filecontents) 
clientSocket.close() 

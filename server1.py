import socket

city_temp={
    "chennai":"40",
    "mumbai":"25",
    "kolkata": "13"
}
 

localIP     = "127.0.0.1"

localPort   = 20001

bufferSize  = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

 


while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = format(message)

    if clientMsg[2:-1] in city_temp :
        msgFromServer= city_temp[clientMsg[2:-1]]
        bytesToSend  = str.encode(msgFromServer)
        UDPServerSocket.sendto(bytesToSend, address)

    else :
        msgFromServer= "city not available"
        bytesToSend  = str.encode(msgFromServer)
        UDPServerSocket.sendto(bytesToSend, address)

      
   
    
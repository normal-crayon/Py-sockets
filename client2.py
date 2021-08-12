import socket
def encrypt(text,s):


    result = ""
   # transverse the plain text
    for i in range(len(text)):

        char = text[i]
        # Encrypt uppercase characters in plain text
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
        return result


serverAddressPort   = ("127.0.0.1", 20001)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket

while(True):
    message=input()
    if(message=="BYE"):
        #socket.shutdown(1)
        socket.close(1)
    else:
        bytesToSend= str.encode(encrypt(message,4))
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)

 

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

 

    msg = "{}".format(msgFromServer[0])

    print("server: "+msg[2:-1])

 

 
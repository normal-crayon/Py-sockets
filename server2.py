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
#check the above function




localIP     = "127.0.0.1"

localPort   = 20001

bufferSize  = 1024
 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]



    clientMsg = "{}".format(message)
    #clientIP  = "Client IP Address:{}".format(address)
    
    print("client: "+ clientMsg[2:-1])
    msg= input()

    if(msg=="BYE"):
        sock.close()
    else:
        bytesToSend= str.encode(msg)
        #encrpt(bytesToSend,4)
        UDPServerSocket.sendto(bytesToSend, address)
    # Sending a reply to client

    
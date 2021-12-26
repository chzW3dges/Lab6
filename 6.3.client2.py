import socket


ClientSocket = socket.socket()
host = '192.168.56.104'
port = 8888

print(' -----Waiting for connection...-----\n')
try:
        ClientSocket.connect((host, port))
except socket.error as e:
        print(str(e))

Response =ClientSocket.recv(1024)
print(Response)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(" \n                 C A L C U L A T O R\n")
print("                 -------CLIENT------             ")
print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")


while True:

        status = 0
        while(status == 0):
                option = input("Enter maths function (L - Log | S - Square Root | E - Exponential):\n           ps: please type L/S/E only!!\n--> ")

                if(option == 'L'):
                        value1 = input("×× Enter the value: ")
                        status = 1
                elif(option == 'S'):
                        value1 = input("×× Enter the value: ")
                        status = 1
                elif(option == 'E'):
                        value1 = input("×× Enter the value: ")
                        status = 1
                else:
                        print("×× Invalid operation!! Please re-enter. ××")
                        status = 0


        Input = option + " " +  value1
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
        print("\n")

ClientSocket.close()


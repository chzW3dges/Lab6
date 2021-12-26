import socket
import sys
import time
import errno
import math
from multiprocessing import Process


print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(" \n        C A L C U L A T O R\n           ")
print(" 	-------SERVER------             ")
print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")


def funcLog(x):
        print("×× Calculating L O G ××")
        x = int(x)
        try:
                answer = math.log(x)
        except:
                answer = "Wrong input! Please try again."

        return answer

def funcSqrt(x):
        print("×× Calculating S Q U A R E R O O T ××")
        x = int(x)
        if(x >= 0):
                try:
                        answer = math.sqrt(x)
                except:
                        answer = "Wrong input! Please try again."
        else:
                answer = "It's a negative value! Server is unable calculate."

        return answer

def funcExp(x):
        print("×× Calculating E X P O N E N T I A L ××")
        x = float(x)
        try:
                answer = math.exp(x)
        except:
                answer = "Wrong input! Please try again."


        return answer


def process_start(s_sock):
        s_sock.send(str.encode('-----Connected to the Server!!----- '))
        while True:
                data = s_sock.recv(2048)
                data = data.decode('utf-8')
                try:
                        option, value1 = data.split(" ", 2)
                except:
                        print("×× Unable to calculate, client disconnected :( ××\n")


                if(option == 'L'):
                        answer = funcLog(value1)
                elif(option == 'S'):
                        answer = funcSqrt(value1)
                elif(option == 'E'):
                        answer = funcExp(value1)

                message = "×× Answer: %s" % str(answer)
                print("×× Completed ××\n------------------------------------\n")
                s_sock.sendall(str.encode(message))

        s_sock.close()

if __name__ == '__main__':
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 8888))
        print("-----   Server is listening...   ------")
        s.listen(3)
        try:
                while True:
                        try:
                                s_sock, s_addr = s.accept()
                                p = Process(target = process_start, args = (s_sock,))
                                p.start()

                        except socket.error:
                                print('×× Got a socket error!!! ××')


        except Exception as e:
                print('×× An exception occured!!! ××')
                print(e)
                sys.exit(1)

        finally:
                s.close()

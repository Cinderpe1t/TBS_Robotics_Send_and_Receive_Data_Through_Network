import socket, time
#from turtle import delay
HOST='192.168.1.121'
PORT=5025

x1=255
x2=255
x3=255
x4=255
StrNum=",".join([str(x1),str(x2),str(x3),str(x4)])
bStr=StrNum.encode('utf-8')
print(StrNum)
cNum=StrNum.split(',')
print(cNum)
aNum=list(map(int,cNum))
print(aNum)
print(aNum[0])
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    s.sendall(bStr)
    print(cNum)
    data=s.recv(1024)
    print('Received', repr(data))
    time.sleep(1)
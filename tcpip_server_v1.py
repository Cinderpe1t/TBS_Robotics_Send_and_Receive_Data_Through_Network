import socket
#print(socket.SOCK_STREAM)
HOST=''
PORT=5025
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, address = s.accept()
print(address[0]+":"+str(address[1]))
while True:
    data = conn.recv(1024)
    conn.sendall(b'Client control data received')
    print('Received', repr(data))
    StrNum=bytes.decode(data)
    print(StrNum)
    cNum=StrNum.split(',')
    print(cNum)
    arrNum=list(map(int,cNum))
    print(arrNum)
conn.close()
s.close()
print('Received', repr(data))
Str=bytes.decode(data)
print(Str)

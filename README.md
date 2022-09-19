# TBS Robotics Send and Receive Data Through Network
TBS Robotics Send and Receive Data Through Network
## Preparation
- Laptops, or laptop and network-capable microcontrollers, such as Raspberry Pi or JETSON Nano
- Wireless access point or router with known SSID and password
- Wired Ethernet is another good option, in case wireless connection is questionable
## Understand the network setup
- Join the TBS_Robotics network with your laptop and microcontrollers
- Find out your IP addresses at laptop or microcontroller
```
(base) Apex-penguin:~ akim$ ifconfig
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000 
	inet6 ::1 prefixlen 128 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=201<PERFORMNUD,DAD>

...

en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6463<RXCSUM,TXCSUM,TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether 3c:22:fb:ab:76:a5 
	inet6 fe80::cc:2243:8473:927%en0 prefixlen 64 secured scopeid 0x7 
	inet 192.168.1.6 netmask 0xffffff00 broadcast 192.168.1.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active

```
- `inet 192.168.1.6` shows the IP address is `192.168.1.6`
- From 2nd computer or microcontroller, `ping` command can check the connection is active and shows response time.
```
(base) Apex-penguin:~ akim$ ping 192.168.1.1
PING 192.168.1.1 (192.168.1.1): 56 data bytes
64 bytes from 192.168.1.1: icmp_seq=0 ttl=64 time=16.012 ms
64 bytes from 192.168.1.1: icmp_seq=1 ttl=64 time=10.818 ms
64 bytes from 192.168.1.1: icmp_seq=2 ttl=64 time=7.073 ms
64 bytes from 192.168.1.1: icmp_seq=3 ttl=64 time=6.030 ms
64 bytes from 192.168.1.1: icmp_seq=4 ttl=64 time=6.509 ms
```
- Firewall in the laptop might block the ping request. It is because the ping can be used as a basic hacking tool to check the existence of a computer in a network. Raspberry Pi or JETSON Nano do not block them by default.
## Setup server and client
- Edit server and client python codes with IP addresses
- Run server python code first
- Run client python code
## IP address and port
- HTTP, HTTPS, FTP, FTPS are type of protocols commonly used for internet. Domain names are translated into IP address by domain name server (DNS). Each protocol has default port to connect.
- Hyper Text Transfer Protocol: port #80
- Hyper Text Transfer Protocol Secured: port #443
- File Transfer Protocol: port #21
- File Transfer Protocol Secured: port #21 or 990
- Ping (Internet Control Message Protocol): no port
- TikTok: port #853
- Discord: port #443
- Apple iMessage: port #5223
- Spotify: port #4070
## TCP/IP vs. UDP
- Transfer Control Protocol / Internet Protocol: Packet delivery is ensured with acknowledgement and quality control. Connection-oriented protocol. Most of the internet communication relies on TCP/IP.
- User Datagram Protocol: Connection-less protocol. Just send the data and delivery is not confirmed.
## Prepare server
- Need socket library. Let's use port #5025 for the test.
- Set up TCP/IP socket and bind with the pre-arranged port number to listen to the incoming request.
```
import socket
HOST=''
PORT=5025
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
```
- Whenever client's data is received, server can serve data to the client
- Received data is in byte format. It needs to be translated into the desired format and data type for further processing
- Notice server is likely to wait all the time for the client data
- Packet size can be smaller than 1024 bytes
```
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
```
## Prepare client
- Need socket library
- Connect to server, then send data to server
- Data needs to be formatted as byte data `utf-8` to be sent in the packet
```
StrNum=",".join([str(x1),str(x2),str(x3),str(x4)])
bStr=StrNum.encode('utf-8')
```
- Wait for server to return data
```
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    s.sendall(bStr)
    print(cNum)
    data=s.recv(1024)
    print('Received', repr(data))
    time.sleep(1)
```
## Run the codes
- Modify port numbers at server and client Python codes
- Set server IP address at client code
```
HOST='192.168.1.121'
PORT=5025
```
- Remember to set up and run server-side first
- Client follows after server set up
- At server, `python3 tcpip_server_v1.py`
- At client, `python3 client_test_v1.py`

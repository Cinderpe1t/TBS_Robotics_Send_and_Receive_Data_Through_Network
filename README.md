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


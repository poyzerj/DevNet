import getpass
import telnetlib

HOST = "192.168.1.125"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"vlan 10\n")
tn.write(b"name Management\n")
tn.write(b"vlan 20\n")
tn.write(b"name Guest\n")
tn.write(b"vlan 30\n")
tn.write(b"name IoT\n")
tn.write(b"int gig0/1\n")
tn.write(b"switchport trunk encapsulation dot1q\n")
tn.write(b"switchport mode trunk\n")
tn.write(b"switchport nonegotiate\n")
tn.write(b"int gig0/0\n")
tn.write(b"switchport trunk encapsulation dot1q\n")
tn.write(b"switchport mode trunk\n")
tn.write(b"switchport nonegotiate\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
# KNOWN ISSUES:
# The only issue is that it works too slow it can take decades
# FIXES of the issues
# To speedup we can do Multi Threading

import socket
import sys
import time

usage = "python 3 portScanner.py TARGET START_PORT END_PORT"

print("-"*70)
print("Port Scanner: Python")
print("-"*70)

if(len(sys.argv) != 4):
	print(usage)
	sys.exit()

try:
	target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
	print("Error: Name Resolution Error")
	sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

for port in range(start_port, end_port+1):
	socketConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socketConnection.settimeout(3)
	connection = socketConnection.connect_ex((target, port))
	if(not connection):
		print(f"Port {port} is OPEN")
	socketConnection.close()

		

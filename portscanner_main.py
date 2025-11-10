
#===========================================================
#      Port Scanner
#    only for Educational Purposes
# writen by Spongebob Squarepants and Tadeus Tentakel
#
#============================================================

#===========================================================
#       IMPORTS

import socket



#===========================================================
#      INPUTS

"""
from_port= input("From Port:")
to_port = input("To Port: ")
target_ip = input("Target IP : (x.x.x.x) : ")
"""

#===========================================
#============for Debugging===================


from_port=1
to_port=100
target_ip = "10.10.251.138"
print( from_port, to_port, target_ip) #for debug

#==========debugging_end====================


#==========================================
#         Functions

def scan_socket(host,port):
	s = socket.socket()
	s.settimeout(0.5)
	res = s.connect_ex((host,port)) # needs 1 Argument (address) so we make it a tuple  by (())
	s.close()
	return res == 0



#============================================
#        Main


for port_to_scan in range(int(from_port), int(to_port)):
	if scan_socket(target_ip,port_to_scan):
		print(port_to_scan, "open")














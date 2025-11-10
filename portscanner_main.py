
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

from_port= input("From Port:")
to_port = input("To Port: ")
target_ip = input("Target IP : (x.x.x.x) : ")



print( from_port + to_port + target_ip) #for debug







for port in range(from_port,to_port):
	scan_socket(target_ip,port)









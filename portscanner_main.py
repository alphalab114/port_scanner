
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

"""
from_port=1
to_port=100
target_ip = "10.10.251.138"
print( from_port, to_port, target_ip) #for debug
"""

#==========debugging_end====================

#==========================================
#         Classes


class Port:
	def __init__(self, number):
		self.number = number
		self.open = False


class port_scanner:
	def __init__(self, host, timeout):
		self.host=host
		self.timeout = timeout
		#self.startport = startport
		#self.endport = endport


	def _scan_one_port(self,port_number):
		p = Port(port_number)
		try:
			with socket.socket() as s:
				s.settimeout(self.timeout)
				res = s.connect_ex((self.host,port_number)) # needs 1 Argument (address) so we make it a tuple  by (())
			if res == 0:
				p.open=True
			else:
				p.open=False
			s.close()
		except:
			print("exception line64")	
			pass
		return p


"""
	def _scan_range_of_ports(self,self.startport,self.endport):
		for port_to_scan in range(self.startport ,self.endport):
			if _scan_one_port(target_ip,port_to_scan):
			
"""	





#============================================
#        Main

if __name__ == "__main__":

	host_input = input("Host eigeben:")
	start_port_input = input("startport eingeben")
	end_port_input = input("Endport eigeben")


scanner = port_scanner(host_input, timeout=0.4)
result = scanner._scan_one_port(80)

print(result.number, result.open)






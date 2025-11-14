
#===========================================================
# Port Scanner
# only for Educational Purposes
# writen by Spongebob Squarepants and Tadeus Tentakel
#
#Function:
#  --  Scanning Ports
#  --  Scanning IPs
#
#============================================================

#===========================================================
#  >>  IMPORTS

import socket
import subprocess
import platform



#==========================================
#  >>  DataClasses
#  >> this is my struct for all Data, and because there is no struct in python I use CLASS


class CLASS_Port_Data:
	def __init__(self, number):
		self.number = number
		self.open = False


class CLASS_Network_Data:
	def __init__ (self, ip_adress, host_name):
		self.ip_adress=ip_adress
		self.host_name = host_name



#==========================================
#  >>  Ip Scanner
#  >> scanning for all available IPs

class CLASS_IP_Scanner:
	def __init__(self, timeout_ping, ping_count):
		self.timeout_ping = timeout_ping
		self.ping_count= str(ping_count)

	def _ping_host(self, host):
		print("DEBUG def _ping_host ") # only for Debugging
		print(self.timeout_ping,  self.ping_count)

		host_system = platform.system().lower()
		print(host_system)
		
		if host_system == "windows":
			ping_command = ["ping", "-n", self.ping_count, host]
		else:
			ping_command = ["ping", "-c", self.ping_count, host]
		
		print(ping_command)
		try:
			result = subprocess.run(ping_command, timeout=self.timeout_ping)
			print(result)  #for debug
			if result:
				return True
			else:
				return False
		except subprocess.TimeoutExpired:
			print(" PING Timeout ")
			return False
		except:
			print("Ein leichter und ganz normaler erwarteter Fehler ist beim ping aufgetreten ")
			return False


		


#==========================================
#  >>  Port Scanner
#  >> scanning for all available Ports, get Ip from IP Scanner


class CLASS_Port_Scanner:
	def __init__(self, host, timeout):
		print("======DEBUG======\nCALL of Function:  __init__  \n=======DEBUG END=======")  # only for Debugging
		self.host=host
		self.timeout = timeout
		self.results = []
		

	# "private" methods --> mangling
	def __scan_one_port(self,port_number):
		print("======DEBUG======\nCALL of Function:  _scan_one_port  \n=======DEBUG END=======")# only for Debugging
		p = CLASS_Port_Data(port_number)
		try:
			with socket.socket() as s:
				s.settimeout(self.timeout)
				res = s.connect_ex((self.host,port_number)) # needs 1 Argument (address) so we make it a tuple  by (())
				print(port_number)
			if res == 0:
				p.open=True
			else:
				p.open=False
			s.close()
		except:
			print("--exception _scan_one_port--")	
			pass
		return p


	# public methods
	def scan_range_of_port(self, startport, endport):
		print("======DEBUG======\nCALL of Function:  scan_range_of_port  \n=======DEBUG END=======")# only for Debugging
		self.results = []
		for port_to_scan in range(startport, endport):
			self.results.append(self.__scan_one_port(port_to_scan))
		return self.results
		

	def print_all_ports(self):
		print("======DEBUG======\nCALL of Function: print_all_ports\n=======DEBUG END=======")# only for Debugging
		if not self.results:  #check if empty or falsy
			print("Daten sind leer oder fehlerhaft, sorry!!!")

		for p in self.results:
			if p.open == True:
				print("Port: " , p.number , " open")
			else:
				print("Port: " , p.number , " NA")

	

	def print_all_open_ports(self):
		print("======DEBUG======\nCALL of Function: print_all_open_ports\n=======DEBUG END=======")# only for Debugging
		if not self.results: #check if empty or falsy
			print("Daten sind leer oder fehlerhaft, sorry!!!")

		for p in self.results:
			if p.open == True:
				print("Port: " , p.number , " open")
			


#============================================
#  >>  Main

if __name__ == "__main__": #script entry point code will only executed when called directly

	input__host = "192.168.178.1"   	#input("Host eigeben:")
	input__start_port = int(0) 		#input("startport eingeben")
	input__end_port = int(15)   	#input("Endport eigeben")
	input__ping_timeout = int(2)
	input__ping_count = int(3)

	ipscanner = CLASS_IP_Scanner(input__ping_timeout, input__ping_count)
	ipscanner._ping_host(input__host)





"""
	scanner = CLASS_Port_Scanner(host_input, timeout=0.4)
	scanner.scan_range_of_port(start_port_input,end_port_input)
	scanner.print_all_ports()
	scanner.print_all_open_ports()
"""






#  --> toDO  namin ändern nach input_...

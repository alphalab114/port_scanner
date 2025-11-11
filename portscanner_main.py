
#===========================================================
# Port Scanner
# only for Educational Purposes
# writen by Spongebob Squarepants and Tadeus Tentakel
#
#============================================================

#===========================================================
#       IMPORTS

import socket



#==========================================
#         Classes


class CLASS_Ports:
	def __init__(self, number):
		self.number = number
		self.open = False


class CLASS_Port_Scanner:
	def __init__(self, host, timeout):
		print("======DEBUG======\nCALL of Function:  __init__  \n=======DEBUG END=======")  # only for Debugging
		self.host=host
		self.timeout = timeout
		self.results = []
		


	def _scan_one_port(self,port_number):
		print("======DEBUG======\nCALL of Function:  _scan_one_port  \n=======DEBUG END=======")# only for Debugging
		p = CLASS_Ports(port_number)
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



	def scan_range_of_port(self, startport, endport):
		print("======DEBUG======\nCALL of Function:  scan_range_of_port  \n=======DEBUG END=======")# only for Debugging
		self.results = []
		for port_to_scan in range(startport, endport):
			self.results.append(self._scan_one_port(port_to_scan))
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
#        Main

if __name__ == "__main__": #script entry point code will only executed when called directly

	host_input = "192.168.178.1"   	#input("Host eigeben:")
	start_port_input = int(0) 		#input("startport eingeben")
	end_port_input = int(15)   	#input("Endport eigeben")
	scanner = CLASS_Port_Scanner(host_input, timeout=0.4)
	scanner.scan_range_of_port(start_port_input,end_port_input)
	scanner.print_all_ports()
	scanner.print_all_open_ports()










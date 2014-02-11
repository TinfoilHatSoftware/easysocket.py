
import socket
import select

class EasySocket:
	def __init__(self, sorc, host, port, bufsize,maxclinum):
		self._sorc = sorc
		self.host = host
		self.port = port
		self.bufsize = bufsize
		self.data2 = ""
		self.ready = False
		self.clinum = maxclinum
		self.rpeer = None
		self.connections = []
		self.addrs = []
		self.errors = []
		self.socklistnum = 0
		self.datafin = ''
		
		
		try:
			self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			if (self._sorc ==True) :
				self.sock.bind((self.host, self.port))
				
				
			else:
				
				self.sock.connect((self.host, self.port))
				self.connections.append(self.sock)
			self.errors= None
			
		except Exception as e:
			self.errors += str(e)

		
			

	

	def receive(self,socklistnum):

		self.ready = select.select([self.connections[socklistnum]], [], [], 0)
		a = self.ready[0]
		if len(a) != 0:
			while True: 
					self.ready = select.select([self.connections[socklistnum]], [], [], 0)
					a = self.ready[0]
					if self.connections[socklistnum] not in a:
						break
					self.data = self.connections[socklistnum].recv(1)
					self.data2 += self.data
			bla = ''
			bla = self.data2
			self.data2 = ''
			return bla
		else:
			retdata = None
			return retdata
		
						
						

	def send(self,data3,socklistnum):
		self.socklistnum = socklistnum
		self.connections[self.socklistnum].send(data3)
	def listen(self):
		self.sock.listen(self.clinum)
		rpeer,addr = self.sock.accept()
		self.connections.append(rpeer)
		self.addrs.append(addr)

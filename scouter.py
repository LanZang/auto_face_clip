#!/usr/bin/python3

##############################
# The main script for vtc face recognition
##############################

import socket

###########
# The default port is 9874
def startServerListen(port=9874):
	addr = ('', port)
	udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	udpSock.bind(addr)
	return udpSock

def closeServer(server):
	#TODO: check server existence.
	if not server:
		server.close()

def restartServerListen(server, port=9874):
	#TODO: check server and close it if it is already open.
	closeServer(server)
	return startServerListen(port)

def readMsg(server):
	if server:
		data, addr = server.recvfrom(1048576)
		if not data:
			print("No data")
		else:
			print("receive ", data, ", from ", addr)
	else:
		print("Bad server")


######################
# The test code:
######################
if __name__ == '__main__':
	# Do the test here.
	server = startServerListen()
	while True:
		readMsg(server)
	closeServer(server)

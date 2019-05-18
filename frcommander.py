#!/usr/bin/python3

##############################
# The commander module used to receiver commander from admin.
# The command sent via udp in JSON format. The default port is 9874
##############################

import socket
import threading
import time

#import handler
import comhandler

class Commander(threading.Thread):
    # define the initializer
    def __init__(self, name, port = 9874):
        threading.Thread.__init__(self)
        self.handler = None
        self.name = name
        self.port = port
        self.servSock = None
        self.startFlag = False

    ###########
    # The default port is 9874
    def startServer(self):
        addr = ('', self.port)
        self.servSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.servSock.settimeout(0.5)
        self.servSock.bind(addr)
        self.startFlag = True
        self.start()
        return self.servSock

    def stopServer(self):
        self.startFlag = False
        #TODO: check server existence.
        if not self.servSock:
            self.servSock.shutdown(socket.SHUT_RDWR)
            self.servSock.close()
            self.servSock = None
        self.join()

    def restart(self, port=None):
        #TODO: check server and close it if it is already open.
        if port:
            self.port = port
        if not self.port or self.port <= 0:
            self.port = 9874
        self.stopServer()
        return self.startServer()
        
    def register(self, handler):
        if self.handler:
            self.handler.unregister('Other-registered')
        self.handler = handler

    def unregister(self):
        if self.handler:
            self.handler.unregister('un-registered')
        self.handler = None

    def run(self):
        print("Start commander receiver")
        while self.startFlag:
            data, addr = self.readMsg()
            if data:
                resp = None
                if self.handler:
                    resp = self.handler.handleMsg(data, addr)
                if not resp:
                    resp = '{"code":404, "reason":"Not Found"}'
                self.sendMsg(addr, resp)

    def readMsg(self, size=1048576):
        if self.servSock:
            try:
                data, addr = self.servSock.recvfrom(size)
                if not data:
                    print("No data")
                else:
                    return(data, addr)
            except socket.timeout as reason:
                pass
            except socket.error as error:
                print("socket error: ", error)
                #TODO: how to reopen the socket.
        else:
            time.sleep(1)
        return(None, None)

    def sendMsg(self, addr, data):
        if data and addr:
            if self.servSock:
                self.servSock.sendto(data.encode(), addr)

######################
# The test code:
######################
if __name__ == '__main__':
	# Do the test here.
	command = Commander('utest')
	handler = comhandler.ComHandler('utest')
	command.register(handler)
	command.startServer()
	i = 0
	while i < 20:
		time.sleep(1)
		#print("sleeping...")
		i = i + 1
	print("Exiting...")
	command.stopServer()

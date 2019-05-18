#!/usr/bin/python3

##############################
# The main script for vtc face recognition
##############################

import socket

# local modules
import frcommander as frc
import comhandler

######################
# The test code:
######################
if __name__ == '__main__':
	# Do the test here.
	server = frc.Commander('vtcai')
	while True:
		readMsg(server)
	closeServer(server)

#!/usr/bin/python3

##############################
# The ai handler module used to correctly handle command from commander.
##############################
import json

import comhandler


class PicHandler(comhandler.ComHandler):
    def __init__(self, name=''):
        comhandler.ComHandler.__init__(self, name)

    #The main handler of the command from commander
    # The return shall also be json command to return to commander
    def handleMsg(self, msg, addr = None):
        print(self.name, " received msg: ", msg, ' from ', (addr == None) and "None" or addr)
        


if __name__ == '__main__':
    print("Not run along")
        
        

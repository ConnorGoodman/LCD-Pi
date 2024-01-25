#! /usr/bin/env python

# Import necessary libraries for communication and display use
import drivers
import os
import uuid
import requests
import time
from time import sleep
from dotenv import load_dotenv

load_dotenv()

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()

def getMessage() :
    # set variable message to any message to be printed on the screen.
    # In this example, the message is pulled from azure blob storage.
    url = os.getenv('AZURE_BLOB_URL')
        
    x = requests.get(url)
    
    message = x.text
    
    # Sentences can only be 16 characters long
    print(message)
    
    # seconds between each http check
    timeInterval = 60

    splitMessage = message.split()
    finalMessage = [""]
    
    index = 0
    count = 0
    
    while (splitMessage) :
        count += (len(splitMessage[0]) + 1)
        
        # word is too long, break it up
        if (len(splitMessage[0]) > 14) :
            splitMessage.insert(1, splitMessage[0][14:len(splitMessage[0])])
            splitMessage[0] = splitMessage[0][0:14]
            
        # add to current list element
        elif (count < 16) :
            if (finalMessage[index] != "") :
                finalMessage[index] += " "
            finalMessage[index] += splitMessage[0]
            del splitMessage[0]
            
        # move onto next list element    
        else :
            index = index + 1
            finalMessage.insert(len(finalMessage), "")
            count = 0
            
    print(finalMessage)
    
    # if there are an odd amount of lines, add one more
    if (len(finalMessage) % 2 != 0) :
        finalMessage.insert(len(finalMessage), "")
    
    return finalMessage

while (True) :
    try:
        finalMessage = getMessage()
            
        print(len(finalMessage))
        count = 0
        start = time.time()
        while True :
            if (time.time() - start >= 200 ) :
                start = time.time()
                print("making http call")
                try :
                    finalMessage = getMessage()
                except ConnectionError:
                    print("Error connecting to storage")
                count = 0
                
                
            elif (count >= len(finalMessage)) :
                count = 0
            display.lcd_display_string(finalMessage[count], 1)  # Write line of text to first line of display
            display.lcd_display_string(finalMessage[count + 1], 2)  # Write line of text to second line of display
            sleep(2)
            display.lcd_clear()# Give time for the message to be read                                          # Give time for the message to be read
            count += 2
    except Exception as e:
        print(e)

  
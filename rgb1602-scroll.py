import RGB1602
import time
import math

lcd=RGB1602.RGB1602(16,2)

while True:
    text = 'test test'          # Show scrolling information
    tmp = text                     # Get the display information
    for i in range(0, 16+len(text)):#len(text)):
        if i < 16:
            tmp = text[:i]
            lcd.setCursor(16-i,1)
        else:
            tmp = text[i-16:i+16]
            lcd.setCursor(0,1)   # Position cursor
        print(str(i)+" tmp:"+str(tmp))
        lcd.printout(tmp)            # Display one by one

        time.sleep(0.1)                 # Delay 800ms
        lcd.clear()                # Clear display

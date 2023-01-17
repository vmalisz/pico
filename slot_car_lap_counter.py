from machine import I2C, Pin, reset
from utime import sleep_ms
from time import sleep, ticks_diff, ticks_ms
from pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

ir_a=Pin(15,Pin.IN)
ir_b=Pin(14,Pin.IN)

button = Pin(0, Pin.IN, Pin.PULL_UP)

clock = bytearray([0x00,0x0e,0x15,0x17,0x11,0x0e,0x00,0x00])
#star = bytearray([0x04,0x15,0x0E,0x1F,0x0E,0x15,0x04,0x00  ])

#lcd.custom_char(2, star)
lcd.custom_char(3, clock)

lane1 = 0
start1 = 0
end1 = 0
laps1 = 0
best1 = 0
tmp1 = 0

lane2 = 0
start2 = 0
end2 = 0
laps2 = 0
best2 = 0
tmp2 = 0

lcd.move_to(0,0)
lcd.putstr('#GO!')

while True:    
    if button.value() == 0:
        reset()

## LANE 1 ###############################################        
    if ir_a.value() == 0:
        tmp1 = ticks_ms()        
        if start1 == 0:
            lcd.move_to(0,0)
            lcd.putstr('LAP1')
            start1 = tmp1
        else:
            lap_time1 = ticks_diff(tmp1,start1)/1000
            if lap_time1 > 2:
                start1 = tmp1
                laps1 += 1
                
                if best1 == 0:
                        best1 = round(lap_time1,2)
                else:
                    if lap_time1 < best1:
                        best1 = round(lap_time1,2)
                        
                lcd.move_to(0,0)
                lcd.putstr(str(lap_time1)[:5])
                lcd.move_to(6,0)
                lcd.putstr(chr(3)+':'+str(best1))
                lcd.move_to(13,0)
                lcd.putstr('L'+str(laps1)[:5])
            
## LANE 2 ###############################################        
    if ir_b.value() == 0:
        tmp2 = ticks_ms()        
        if start2 == 0:
            lcd.move_to(0,1)
            lcd.putstr('LAP1')
            start2 = tmp2
        else:
            lap_time2 = ticks_diff(tmp2,start2)/1000
            if lap_time2 > 2:
                start2 = tmp2
                laps2 += 1
                
                if best2 == 0:
                        best2 = round(lap_time2,2)
                else:
                    if lap_time2 < best2:
                        best2 = round(lap_time2,2)
                        
                lcd.move_to(0,1)
                lcd.putstr(str(lap_time2)[:5])
                lcd.move_to(6,1)
                lcd.putstr(chr(3)+':'+str(best2))
                lcd.move_to(13,1)
                lcd.putstr('L'+str(laps2)[:5])
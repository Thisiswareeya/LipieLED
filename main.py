import max7219
from machine import Pin, SPI
from time import sleep
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)

P1 = 'Rediocheck rediocheck Ollie to earth' 
length = len(P1) 
length = (length*8)
display = max7219.Matrix8x8(spi, ss, 4)
display.brightness(1)   # adjust brightness 1 to 15 #ปรับความสว่าง
display.fill(1)
display.show()
sleep(0.5) 
display.fill(0)
display.show()
sleep(0.2)

while True:      
    for x in range(32, -length, -1):    #ลูปตำแหน่งของแมททริก เริ่มที่เท่าไหร่ถอยไปเท่าไหร่ 
        display.text(P1 ,x,0,1)
        display.show()
        sleep(0.10)
        display.fill(0)
      
    
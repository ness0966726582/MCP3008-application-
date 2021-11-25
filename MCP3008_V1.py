import time
import datetime
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
# Software SPI configuration:
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
MCP3008_Ch=["no-use","S1","S2","S3","S4","S5","S6","S7"]

def CTsensor():
    global MCP3008_Ch
    Number=1
    Sensor=["CT-sensor","10","30"] #NAME , <Value=0 , >Value=1
#Below no need to adjust
    AV = int(("{%s}"%Number).format(*values));#print(AV)
    if (AV<int(Sensor[1]) and AV==1):
        MCP3008_Ch[Number] = 0 ;   #print("OFF")
    if (AV>int(Sensor[2])):        
        MCP3008_Ch[Number] = 1 ;   #print("ON")

def Lightsensor():
    global MCP3008_Ch
    Number=2
    Sensor=["Light-sensor","200","200"] #NAME , <Value=1 , >Value=0
#Below no need to adjust
    AV = int(("{%s}"%Number).format(*values));#print(AV)
    if (AV<int(Sensor[1])):
        MCP3008_Ch[Number] = 1 ;   #print("Bright")
    if (AV>int(Sensor[2])):        
        MCP3008_Ch[Number] = 0 ;   #print("DARK")

def Toutchsensor():
    global MCP3008_Ch
    Number=3
    Sensor=["Toutch-sensor","500","600"] #NAME , <Value=0 , >Value=1
#Below no need to adjust
    AV = int(("{%s}"%Number).format(*values));#print(AV)
    if (AV<int(Sensor[1])):
        MCP3008_Ch[Number] = 0 ;   #print("NO CONTACT")
    if (AV>int(Sensor[2])):        
        MCP3008_Ch[Number] = 1 ;   #print("CONTACT")

def Firesensor():
    global MCP3008_Ch
    Number=4
    Sensor=["Fire-sensor","100","1000"] #NAME , <Value=0 , >Value=1
#Below no need to adjust
    AV = int(("{%s}"%Number).format(*values));#print(AV)
    if (AV<int(Sensor[1])):
        MCP3008_Ch[Number] = 1 ;   #print("Fire")
    if (AV>int(Sensor[2])):        
        MCP3008_Ch[Number] = 0 ;   #print("no Fire")

def Watersensor():
    global MCP3008_Ch
    Number=5
    Sensor=["Water-sensor","10","100"] #NAME , <Value=0 , >Value=1
#Below no need to adjust
    AV = int(("{%s}"%Number).format(*values));#print(AV)
    if (AV<int(Sensor[1])):
        MCP3008_Ch[Number] = 0 ;   #print("leaking")
    if (AV>int(Sensor[2])):        
        MCP3008_Ch[Number] = 1 ;   #print("no leaking")

def GASsensor():
    global MCP3008_Ch  
    Number=6
    Sensor=["GAS-sensor","30","100"] #NAME , <Value=0 , >Value=1  
#Below no need to adjust
    AV = int(("{%s}"%Number).format(*values)); #print(AV)
    if (AV<int(Sensor[1])):
        MCP3008_Ch[Number] = 0 ;   #print("no pollution ")
    if (AV>int(Sensor[2])):        
        MCP3008_Ch[Number] = 1 ;   #print("Air pollution")
        
def Sort_List():
    CTsensor()
    Lightsensor()
    Toutchsensor()
    Firesensor()
    Watersensor()
    GASsensor()
    All_Sensor = [MCP3008_Ch[0],MCP3008_Ch[1],MCP3008_Ch[2],MCP3008_Ch[3],MCP3008_Ch[4],MCP3008_Ch[5],MCP3008_Ch[6],MCP3008_Ch[7]]
    print(All_Sensor)    
####### Main program loop.#######
while True:
    values = [0]*8
    for i in range(8):
        values[i] = mcp.read_adc(i)
    
    Sort_List()
    time.sleep(1) 
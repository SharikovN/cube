import machine, ssd1306, time
oled_i2c = machine.SoftI2C(sda=machine.Pin(16), scl = machine.Pin(17))
oled = ssd1306.SSD1306_I2C(128, 64, oled_i2c)

def normal(lz):
    dist = 36
    side = 'left'
    oled.fill(0)
    for i in range(18):
        oled.pixel(36, 19+i, 1) #Левый, левая грань
        oled.pixel(36+dist, 19+i, 1) #Правй, левая грань
        oled.pixel(55, 19+i, 1) #Левый, правая грань
        oled.pixel(55+dist, 19+i, 1) #Правый, правая грань
    for i in range(2):
        if i == 0:
            dist = 0
        else:
            dist = 36

        for j in range(2):
            oled.pixel(37+dist, 17+j, 1)
            oled.pixel(54+dist, 17+j, 1)
            oled.pixel(37+dist, 37+j, 1)
            oled.pixel(54+dist, 37+j, 1)
            oled.pixel(38+dist+j, 16, 1)
            oled.pixel(52+dist+j, 16, 1)
            oled.pixel(38+dist+j, 39, 1)
            oled.pixel(52+dist+j, 39, 1)

        for j in range(3):
            oled.pixel(40+dist+j, 15, 1)
            oled.pixel(49+dist+j, 15, 1)
            oled.pixel(40+dist+j, 40, 1)
            oled.pixel(49+dist+j, 40, 1)
            oled.pixel(i * (55+j) + (not i) * (127 - (55+j)), 48, 1) # рот

        for j in range(6):
            oled.pixel(43+dist+j, 14, 1)
            oled.pixel(43+dist+j, 41, 1)


        #Зрачки
        for j in range(5):
            oled.pixel(lz+j+dist, 20, 1)
            oled.pixel(lz+j+dist, 35, 1)

        for j in range(8):
            oled.pixel(lz+8+dist, 24+j, 1)

        for j in range(9):
            oled.pixel(lz-2+j+dist, 21, 1)
            oled.pixel(lz-2+j+dist, 34, 1)

        for j in range(11):
            for k in range(12):
                oled.pixel(lz-3+j+dist, 22+k, 1)
    #Рот
    for i in range(8):
        oled.pixel(60+i, 50, 1)
    for i in range(12):
        oled.pixel(58+i, 49, 1)
    oled.show()
    
def ill(lz):
    dist = 36
    side = 'left'
    oled.fill(0)
    for i in range(18):
        oled.pixel(36, 18+i, 1) #Левый, левая грань
        oled.pixel(36+dist, 18+i, 1) #Правй, левая грань
        oled.pixel(55, 18+i, 1) #Левый, правая грань
        oled.pixel(55+dist, 18+i, 1) #Правый, правая грань
    for i in range(2):
        if i == 0:
            dist = 0
        else:
            dist = 36
 
        oled.pixel(37+dist, 18, 1) #1в
        for j in range(2):
            oled.pixel(i * (52+j) + (not i) * (127 - (52+j)), 15, 1) #6в
            oled.pixel(i * 54 + (not i) * (127 - 54), 16+j, 1) #7в
            oled.pixel(i * 37 + (not i) * (127 - 37), 36+j, 1) #1н
            oled.pixel(i * (38+j) + (not i) * (127 - (38+j)), 38, 1) #2н
            oled.pixel(i * (52+j) + (not i) * (127 - (52+j)), 38, 1) #6н
            oled.pixel(i * 54 + (not i) * (127 - 54), 36+j, 1) #7н
 
        for j in range(3):
            oled.pixel(i * (38+j) + (not i) * (127 - (38+j)), 17, 1) #2в
            oled.pixel(i * (41+j) + (not i) * (127 - (41+j)), 16, 1) #3в
            oled.pixel(i * (49+j) + (not i) * (127 - (49+j)), 14, 1) #5в
            oled.pixel(i * (40+j) + (not i) * (127 - (40+j)), 39, 1) #3н
            oled.pixel(i * (49+j) + (not i) * (127 - (49+j)), 39, 1) #5н
 
        for j in range(5):
            oled.pixel(i * (44+j) + (not i) * (127 - (44+j)), 15, 1) #4в
 
        for j in range(6):
            oled.pixel(i * (43+j) + (not i) * (127 - (43+j)), 40, 1) #4н
 
 
        #Зрачки
        for j in range(9):
            oled.pixel(lz+3+j+dist, 39, 1)
        for j in range(6):
            oled.pixel(lz+1+j+dist, 24, 1)
 
        for j in range(9):
            oled.pixel(lz+j+dist, 38, 1)
 
        for j in range(10):
            oled.pixel(lz-1+j+dist, 25, 1)
 
        for j in range(12):
            for k in range(2):
                oled.pixel(lz-2+j+dist, 26+k, 1)
                oled.pixel(lz-2+j+dist, 36+k, 1)
 
        for j in range(14):
            for k in range(8):
                oled.pixel(lz-3+j+dist, 28+k, 1)
 
    #Рот
    dist=14
    for i in range(2):
        oled.pixel(57+i, 46, 1)
        oled.pixel(69+i, 46, 1)
        oled.pixel(54+i, 48, 1)
        oled.pixel(72+i, 48, 1)
    for i in range(3):
        oled.pixel(59+i, 48, 1)
        oled.pixel(66+i, 48, 1)
    for i in range(6):
        oled.pixel(61+i, 46, 1)
    for i in range(18):
        oled.pixel(55+i, 47, 1)
 
 
    oled.show()

def joy(lz):
    dist = 36
    side = 'left'
    oled.fill(0)
    for i in range(18):
        oled.pixel(36, 19+i, 1) #Левый, левая грань
        oled.pixel(36+dist, 19+i, 1) #Правй, левая грань
        oled.pixel(55, 19+i, 1) #Левый, правая грань
        oled.pixel(55+dist, 19+i, 1) #Правый, правая грань
    for i in range(2):
        if i == 0:
            dist = 0
        else:
            dist = 36
 
        for j in range(2):
            oled.pixel(37+dist, 17+j, 1)
            oled.pixel(54+dist, 17+j, 1)
            oled.pixel(37+dist, 37+j, 1)
            oled.pixel(54+dist, 37+j, 1)
            oled.pixel(38+dist+j, 16, 1)
            oled.pixel(52+dist+j, 16, 1)
            oled.pixel(38+dist+j, 39, 1)
            oled.pixel(52+dist+j, 39, 1)
 
            oled.pixel(i * (59+j) + (not i) * (127 - (59+j)), 52, 1)
 
        for j in range(3):
            oled.pixel(40+dist+j, 15, 1)
            oled.pixel(49+dist+j, 15, 1)
            oled.pixel(40+dist+j, 40, 1)
            oled.pixel(49+dist+j, 40, 1)
 
            oled.pixel(i * 58 + (not i) * (127 - 58), 49+j, 1)
 
        for j in range(6):
            oled.pixel(43+dist+j, 14, 1)
            oled.pixel(43+dist+j, 41, 1)
 
 
        #Зрачки
        for j in range(5):
            oled.pixel(lz+j+dist, 20, 1)
            oled.pixel(lz+j+dist, 35, 1)
 
        for j in range(8):
            oled.pixel(lz+8+dist, 24+j, 1)
 
        for j in range(9):
            oled.pixel(lz-2+j+dist, 21, 1)
            oled.pixel(lz-2+j+dist, 34, 1)
 
        for j in range(11):
            for k in range(12):
                oled.pixel(lz-3+j+dist, 22+k, 1)
 
    #Рот
    for i in range(6):
        oled.pixel(61+i, 51, 1)
        oled.pixel(61+i, 53, 1)
    for i in range(12):
        oled.pixel(58+i, 48, 1)
    oled.show()

def sad(lz):
    dist = 36
    side = 'left'
    oled.fill(0)
    for i in range(18):
        oled.pixel(36, 18+i, 1) #Левый, левая грань
        oled.pixel(36+dist, 18+i, 1) #Правй, левая грань
        oled.pixel(55, 18+i, 1) #Левый, правая грань
        oled.pixel(55+dist, 18+i, 1) #Правый, правая грань
    for i in range(2):
        if i == 0:
            dist = 0
        else:
            dist = 36
 
        oled.pixel(37+dist, 18, 1) #1в
        for j in range(2):
            oled.pixel(i * (52+j) + (not i) * (127 - (52+j)), 15, 1) #6в
            oled.pixel(i * 54 + (not i) * (127 - 54), 16+j, 1) #7в
            oled.pixel(i * 37 + (not i) * (127 - 37), 36+j, 1) #1н
            oled.pixel(i * (38+j) + (not i) * (127 - (38+j)), 38, 1) #2н
            oled.pixel(i * (52+j) + (not i) * (127 - (52+j)), 38, 1) #6н
            oled.pixel(i * 54 + (not i) * (127 - 54), 36+j, 1) #7н
 
        for j in range(3):
            oled.pixel(i * (38+j) + (not i) * (127 - (38+j)), 17, 1) #2в
            oled.pixel(i * (41+j) + (not i) * (127 - (41+j)), 16, 1) #3в
            oled.pixel(i * (49+j) + (not i) * (127 - (49+j)), 14, 1) #5в
            oled.pixel(i * (40+j) + (not i) * (127 - (40+j)), 39, 1) #3н
            oled.pixel(i * (49+j) + (not i) * (127 - (49+j)), 39, 1) #5н
 
        for j in range(5):
            oled.pixel(i * (44+j) + (not i) * (127 - (44+j)), 15, 1) #4в
 
        for j in range(6):
            oled.pixel(i * (43+j) + (not i) * (127 - (43+j)), 40, 1) #4н
 
 
        #Зрачки
        for j in range(9):
            oled.pixel(lz+3+j+dist, 39, 1)
        for j in range(6):
            oled.pixel(lz+1+j+dist, 24, 1)
 
        for j in range(9):
            oled.pixel(lz+j+dist, 38, 1)
 
        for j in range(10):
            oled.pixel(lz-1+j+dist, 25, 1)
 
        for j in range(12):
            for k in range(2):
                oled.pixel(lz-2+j+dist, 26+k, 1)
                oled.pixel(lz-2+j+dist, 36+k, 1)
 
        for j in range(14):
            for k in range(8):
                oled.pixel(lz-3+j+dist, 28+k, 1)
 
    #Рот
    for i in range(6):
        oled.pixel(61+i, 46, 1)
    for i in range(8):
        oled.pixel(60+i, 47, 1)
    oled.show()

def eyes_closed():
    for j in range(19):
        oled.line(0,j+10,128,j+10,0)
        oled.line(0,46-j,128,46-j,0)
        oled.show()
        time.sleep(0.1)
    em_sleep()

def em_sleep():
    oled.fill(0)
    oled.text('Z', 1, 1, 1)
    oled.text('z', 11, 6, 1)
    oled.text('z', 21, 11, 1)
    #Рот
    for i in range(8):
        oled.pixel(57+i, 46, 1)
        oled.pixel(57+i, 49, 1)
    for i in range(2):
        oled.pixel(56, 47+i, 1)
        oled.pixel(65, 47+i, 1)
    #Глаз левый
    oled.pixel(36,30,1)
    oled.pixel(37,30,1)
    oled.pixel(37,31,1)
    oled.pixel(38,31,1)
    oled.pixel(39,31,1)
    oled.line(40,32,50,32,1)
    oled.line(51,31,53,31,1)
    #Глаз правый
    oled.pixel(36+28,30,1)
    oled.pixel(37+28,30,1)
    oled.pixel(37+28,31,1)
    oled.pixel(38+28,31,1)
    oled.pixel(39+28,31,1)
    oled.line(40+28,32,50+28,32,1)
    oled.line(51+28,31,53+28,31,1)
    oled.show()

 
def animate(func):
    lz = 40
    for i in range(7):
        oled.fill(0)
        if func == 'normal':
            normal(lz)
        elif func == 'joy':
            joy(lz)
        elif func == 'sad':
            sad(lz)
        elif func == 'ill':
            ill(lz)
        lz += 1
        time.sleep(0.1)
        if lz == 47:
            while lz > 40:
                oled.fill(0)
                if func == 'normal':
                    normal(lz)
                elif func == 'joy':
                    joy(lz)
                elif func == 'sad':
                    sad(lz)
                elif func == 'ill':
                    ill(lz)
                lz -= 1
                time.sleep(0.1)
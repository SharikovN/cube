import machine
import ssd1306
import time
import neopixel

# Инициализация I2C для OLED и настройка Neopixel
oled_i2c = machine.SoftI2C(sda=machine.Pin(16), scl=machine.Pin(17))
oled = ssd1306.SSD1306_I2C(128, 64, oled_i2c)
np = neopixel.NeoPixel(machine.Pin(5), 14)

oled.fill(0)
oled.show()

def color(col):
    if col == 'red':
        col = (255, 0, 0)
    elif col == 'blue':
        col = (0, 0, 255)
    else:
        col = (0, 0, 0)
    for i in range(14):
        np[i] = col
    np.write()

# Анимация загрузки
def loading(duration):
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < duration:
        oled.fill(0)
        oled.text("Loading", 20, 20)
        oled.text(".", 70, 30)
        oled.show()
        time.sleep(0.5)
        color('red')

        oled.fill(0)
        oled.text("Loading", 20, 20)
        oled.text("..", 70, 30)
        oled.show()
        time.sleep(0.5)
        color('blue')

        oled.fill(0)
        oled.text("Loading", 20, 20)
        oled.text("...", 70, 30)
        oled.show()
        time.sleep(0.5)
        color('off')

# Запуск анимации на 4 секунды

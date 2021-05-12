from subprocess import PIPE, Popen
import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

# RPI GPIO setup
lcd_rs = digitalio.DigitalInOut(board.D25)
lcd_en = digitalio.DigitalInOut(board.D24)
lcd_d7 = digitalio.DigitalInOut(board.D22)
lcd_d6 = digitalio.DigitalInOut(board.D18)
lcd_d5 = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D23)

# I think this doesn't work
lcd_backlight = digitalio.DigitalInOut(board.D4)

lcd_columns = 16
lcd_rows = 2

lcd = character_lcd.Character_LCD_Mono(
    lcd_rs,
    lcd_en,
    lcd_d4,
    lcd_d5,
    lcd_d6,
    lcd_d7,
    lcd_columns,
    lcd_rows,
    lcd_backlight
)

def run_command(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

weather_cmd  = r'''curl wttr.in/Wroclaw?format="%l+%T+%C+%t+%h+%w+%P+%s\n"'''
wather_cond_cmd = r'''curl wttr.in/Wroclaw?format="%C\n"'''

counter = 0
while counter < 100:
    lcd.clear()
    weather_out = run_command(weather_cmd)
    lcd.message = weather_out
    for i in range(len(weather_out)):
        time.sleep(0.5)
        lcd.move_left
    counter += 1

lcd.clear()
# Create message to scroll
scroll_msg = "<-- Scroll"
lcd.message = scroll_msg
# Scroll message to the left
for i in range(len(scroll_msg)):
    time.sleep(0.5)
    lcd.move_left()
lcd.clear()
lcd.message = "Going to sleep\nCya later!"
time.sleep(3)
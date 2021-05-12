from subprocess import check_output
import time
from datetime import datetime
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
    return check_output(cmd, shell=True)

def print_and_move(msg):
    n = max([len(i) for i in msg.split("\n")])
    lcd.clear()
    lcd.message = msg
    for i in range(n):
        time.sleep(0.5)
        lcd.move_left()


weather_cmd  = r'''curl wttr.in/Wroclaw?format="%l+%t+%h+%w+%P+%s\n"'''
weather_cond_cmd = r'''curl wttr.in/Wroclaw?format="%C\n"'''
try:
    while True:
        weather_out = run_command(weather_cmd)
        weather_cond_out = run_command(weather_cond_cmd).decode().strip()
        act_time = datetime.now().strftime('%b %d  %H:%M:%S')
        location, temp, hum, wind, pres, sunset = [i.decode() for i in weather_out.split()]
        for i in range(3):
            upper_row = " ".join([location, temp])
            lower_row = " ".join([act_time, weather_cond_out])
            print_and_move(upper_row+"\n"+lower_row)
            print_and_move(f"Humidity: {hum}\nPreassure: {pres}")
            print_and_move(f"Wind: {wind}\nSunset: {sunset}")
finally:
    lcd.clear()

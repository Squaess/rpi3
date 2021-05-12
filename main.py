import board
import time
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd


# lcd_rs = 25
# lcd_en = 24
# lcd_d7 = 22
# lcd_d6 = 18
# lcd_d5 = 17
# lcd_d4 = 23
# lcd_backlight = 2

lcd_rs = digitalio.DigitalInOut(board.D25)
lcd_en = digitalio.DigitalInOut(board.D24)
lcd_d7 = digitalio.DigitalInOut(board.D22)
lcd_d6 = digitalio.DigitalInOut(board.D18)
lcd_d5 = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D23)
lcd_backlight = digitalio.DigitalInOut(board.D2)

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
# lcd = character_lcd.Character_LCD()
print("Clearing lcd")
lcd.clear()
print("Printing Hello ...")
lcd.message = "Hello\nCircuitPython"
print("Sleeping ...")
time.sleep(4)
print("Clearing lcd")
lcd.clear()
print("Printing Dupa")
lcd.message("Dupa")
print("Sleeping")
time.sleep(4)

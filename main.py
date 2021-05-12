import board
import time
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd


lcd_rs = 25
lcd_en = 24
lcd_d7 = 22
lcd_d6 = 18
lcd_d5 = 17
lcd_d4 = 23
lcd_backlight = 2

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
)
# lcd = character_lcd.Character_LCD()

lcd.clear()
lcd.message = "Hello\nCircuitPython"
time.sleep(4)
lcd.clear()
lcd.message("Dupa")
time.sleep(4)

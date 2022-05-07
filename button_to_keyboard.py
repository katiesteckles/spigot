import gpiozero
import keyboard

button = gpiozero.Button(9)
button_state=False

while True:
    if button.is_active and not button_state:
        keyboard.press_and_release('a')
        button_state=True
    if button_state and not button.is_active:
        keyboard.press_and_release('b')
        button_state=False

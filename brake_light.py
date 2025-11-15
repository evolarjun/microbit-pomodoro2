# MicroPython program for BBC micro:bit
#
# Sets all LEDs to 70% brightness.
# When a shake is detected, all LEDs brighten to 100% for 1 second,
# then return to 70%.

# This doesn't work like I intend yet, still needs some more work.

from microbit import *

# Define brightness levels
# The maximum brightness for an LED is 9.
# 70% of 9 is ~6.3, so we'll use 6.
BRIGHTNESS_LOW = 6
BRIGHTNESS_HIGH = 9

def set_all_leds(brightness_level):
    """A helper function to set all 25 LEDs to a given brightness."""
    for x in range(5):
        for y in range(5):
            # display.set_pixel(x, y, value) sets the brightness
            # of the LED at coordinate (x,y)
            display.set_pixel(x, y, brightness_level)

# --- Main Program Starts Here ---

# 1. Set the initial state: all LEDs at 70%
set_all_leds(BRIGHTNESS_LOW)

# 2. Start an infinite loop to keep checking for shakes
while True:
    # Check if the 'shake' gesture has happened
    if accelerometer.was_gesture('shake'):
        
        # If shaken, set all LEDs to 100% brightness
        set_all_leds(BRIGHTNESS_HIGH)
        
        # Pause for 1 second (1000 milliseconds)
        sleep(100)
        
        # Return all LEDs to the low brightness state
        set_all_leds(BRIGHTNESS_LOW)
    
    # Add a small delay in the loop to allow the micro:bit
    # to process other things (like detecting gestures)
    sleep(20)

from microbit import (display, button_a, button_b, Image, running_time, 
    set_volume, sleep, pin_logo, pin0, pin1, pin2)
import micropython
#import audio
#from microbit import *
import music

# set some global variables
currently_shown_t = 0 # keep track of what is shown so we don't update the interface
ms_in_minute = 1000 # ms in a minute for debugging
ms_in_minute = 60000
time_0 = running_time()
timer_length = 25 # in minutes
timer_length_list = [5, 15, 25, 50]
max_brightness = 6 # full brightness is too bright for my desk
running = 0
blank_image = Image(
        "00000:"
        "00000:"
        "00000:"
        "00000:"
        "00000:"
    )
full_image = Image(
        "99999:"
        "99999:"
        "99999:"
        "99999:"
        "99999:"
)
digits = {
    '0': ('99', '99', '99', '99', '99'),
    '1': ('09', '09', '09', '09', '09'),
    '2': ('99', '09', '99', '90', '99'),
    '3': ('99', '09', '99', '09', '99'),
    '4': ('90', '90', '99', '09', '09'),
    '5': ('99', '90', '99', '09', '99'),
    '6': ('90', '90', '99', '99', '99'),
    '7': ('99', '09', '09', '09', '09'),
    '8': ('99', '99', '00', '99', '99'),
    '9': ('99', '99', '99', '09', '09'),
    ' ': ('00', '00', '00', '00', '00'),
}

# setting these sometimes caused flickering in the 4th and 5th rows. Not sure why and it was intermittent.
#pin0.set_touch_mode(pin0.CAPACITIVE)
#pin1.set_touch_mode(pin1.CAPACITIVE)
#pin2.set_touch_mode(pin2.CAPACITIVE)



def showDigits(value, b=9, fill_zero=False):
    value = min(max(value, 0), 99)
    d = ('{:02d}' if fill_zero else '{:2d}').format(value)
    display.show(Image(':'.join(
        ['{}0{}'.format(digits[d[0]][i], digits[d[1]][i]).replace('9', str(b)) 
         for i in range(5)])))
    

def updateTimerDisplay(t):
    global max_brightness
    global currently_shown_t
    t2 = int(t)
    first = max_brightness
    if t2 > 26:
        t2 = t - 25
        first = 0
    #elif t2 == 25:
    #    first = 3
    #print()
    if (int(t2) != currently_shown_t): 
        currently_shown_t = int(t2)
        for row in range(5):
            for col in range(5):
                #print(str(int(t)) + "  " + str(col) + " " + str(row) + " " + str(t2))
                #sleep(100)
                if (t2 >= 0):
                    if (col == 0 and row == 0):
                        display.set_pixel(col, row, first)
                    else:
                        display.set_pixel(col, row, max_brightness)
    
                else:
                    display.set_pixel(col, row, 0)
                t2 += -1


def showTimerLengthSetting():
    global max_brightness
    global timer_length
    display.show(blank_image)
    if timer_length == 50:
        display.show(Image(
        "00000:"
        "00000:"
        "66666:"
        "66666:"
        "00000:"
        ))
    else:
        for col in range(int(timer_length / 5)):
            display.set_pixel(col, 2, max_brightness)


def beep():
    # music.play(music.BEEP)
    music.pitch(1100, 100)
    #audio.play(audio.SoundEffect(
    #    freq_start=2200, 
    #    freq_end=2500, 
    #    duration=100, 
    #    vol_start=220, 
    #    vol_end=220,
    #    waveform=3,
    #    fx=0,
    #    shape=18), wait=False)

def alert():
    display.show(blank_image)
    #display.show(Image.ALL_CLOCKS)
    #display.show(Image.CLOCK12)
    #sleep(1000)
    beep()
    for _ in range(10):
        display.show(full_image)
        sleep(300)
        display.show(blank_image)
        sleep(200)
    #display.show(Image.ALL_CLOCKS)
    #display.show(Image.CLOCK12)
    #sleep(1000)
    
def stop_timer():
    global running
    running = 0
    # reset display
    showTimerLengthSetting()

def start_timer():
    global running
    global time_0
    running = 1
    time_0 = running_time()
    showDigits(timer_length)
    sleep(500)

set_volume(50)
display.show(Image.YES)
sleep(200)
showTimerLengthSetting()

while True:
    if running:
        elapsed = (running_time() - time_0) / ms_in_minute        
        if timer_length - elapsed <= 0:
            running = 0
            currently_shown_t = 0
            alert()
            showTimerLengthSetting()
        else:
            # print(timer_length - elapsed)
            updateTimerDisplay(timer_length - elapsed)

    if button_b.was_pressed():
        if running:
            stop_timer()
        else:
            start_timer()
    if button_a.was_pressed():
        if running:
            running = 0
            updateTimerDisplay(timer_length)
            sleep(500)
            showTimerLengthSetting()
        else:
            # toggle timer
            if timer_length == 50:
                timer_length = 5
                showDigits(timer_length)
                sleep(500)
                showTimerLengthSetting()
            elif timer_length == 5:
                timer_length = 15
                showDigits(timer_length)
                sleep(500)
                showTimerLengthSetting()
            elif timer_length == 15:
                timer_length = 25
                showDigits(timer_length)
                sleep(500)
                showTimerLengthSetting()
            else:
                timer_length = 50
                showDigits(timer_length)
                sleep(500)
                showTimerLengthSetting()
# Use of touch sensors for pins 1, 2, and 3 causes flickering for some reason
    if pin_logo.is_touched():
        beep()
#        showDigits(1)
#        timer_length = 
#    if pin0.is_touched():
#        beep()
#        if running:
#            running = 0
#        timer_length = 5
#        showDigits(timer_length)
#        sleep(500)
#        showTimerLengthSetting()
#    if pin1.is_touched():
#        beep()
#        if running:
#            running = 0
#        timer_length = 25
#        showDigits(timer_length)
#        sleep(500)
#        showTimerLengthSetting()
#    if pin2.is_touched():
#        beep()
#        if running:
#            running = 0
#        timer_length = 50
#        showDigits(timer_length)
#        sleep(500)
#        showTimerLengthSetting()
#    

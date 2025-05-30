from microbit import *
import micropython
import audio

# set some global variables
ms_in_minute = 1000 # ms in a minute for debugging
ms_in_minute = 60000
time_0 = running_time()
timer_length = 25 # in minutes
timer_length_list = [5, 15, 25, 50]
max_brightness = 6
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

def updateTimerDisplay(t):
    global max_brightness
    t2 = int(t)
    first = max_brightness
    if t2 > 26:
        t2 = t - 25
        first = 0
    #elif t2 == 25:
    #    first = 3
    #print()
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
    if timer_length > 25:
        display.show(Image.CLOCK12)
    else:
        for col in range(int(timer_length / 5)):
            display.set_pixel(col, 2, max_brightness)


def beep():
    audio.play(audio.SoundEffect(
        freq_start=2200, 
        freq_end=2500, 
        duration=100, 
        vol_start=220, 
        vol_end=220,
        waveform=3,
        fx=0,
        shape=18), wait=False)

def alert():
    display.show(blank_image)
    #display.show(Image.ALL_CLOCKS)
    #display.show(Image.CLOCK12)
    #sleep(1000)
    beep()
    for _ in range(6):
        display.show(full_image)
        sleep(300)
        display.show(blank_image)
        sleep(200)
    display.show(Image.ALL_CLOCKS)
    display.show(Image.CLOCK12)
    sleep(1000)
    
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
    display.scroll(timer_length)


set_volume(50)
display.show(Image.YES)
sleep(200)
showTimerLengthSetting()

while True:
    if running:
        elapsed = (running_time() - time_0) / ms_in_minute
        if timer_length - elapsed <= 0:
            running = 0
            alert()
            showTimerLengthSetting()
        else:
            updateTimerDisplay(timer_length - elapsed)

    if button_b.was_pressed():
        if running:
            stop_timer()
        else:
            start_timer()
    if button_a.was_pressed():
        if running:
            running = 0
            updateTimerDisplay(25)
            sleep(500)
            showTimerLengthSetting()
        else:
            # toggle timer
            if timer_length == 50:
                timer_length = 5
                display.scroll(timer_length)
                showTimerLengthSetting()
            elif timer_length == 5:
                timer_length = 25
                display.scroll(timer_length)
                showTimerLengthSetting()
            else:
                timer_length = 50
                display.scroll(timer_length)
                showTimerLengthSetting()
    if pin_logo.is_touched():
        beep()
        sleep(500)


from microbit import *
import micropython
import audio

# set some global variables
time_0 = running_time()
timer_length = 25 # in minutes
timer_length_list = [5, 15, 25, 50]
max_brightness = 6
running = 0
ms_in_minute = 1000 # ms in a minute for debugging
ms_in_minute = 60000
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
    t2 = t
    if t2 > 25:
        multiplier = 2
    else:
        multiplier = 1
    for row in range(5):
        for col in range(5):
            if  t2 > 0:
                display.set_pixel(col, row, max_brightness)
                t2 += -multiplier                    
            else:
                display.set_pixel(col, row, 0)

def showTimerLengthSetting():
    global max_brightness
    global timer_length
    display.show(blank_image)
    left = timer_length
    for row in range(2, 4):
        for col in range(5):
            if left > 0:
                #print(row, col)
                display.set_pixel(col, row, max_brightness)
                left -= 5
            else:
                break
#    for col in range(int(timer_length / 5)):
#        display.set_pixel(col, 2, max_brightness)
    

def beep():
    audio.play(audio.SoundEffect(
        freq_start=500, 
        freq_end=2500, 
        duration=500, 
        vol_start=220, 
        vol_end=0,
        waveform=3,
        fx=0,
        shape=18), wait=False)

def alert():
    beep()
    # display.show(blank_image)
    for _ in range(8):
        display.show(full_image)
        sleep(300)
        display.show(blank_image)
        sleep(200)
    display.show(Image.ALL_CLOCKS)
    display.show(Image.CLOCK12)
    sleep(1000)
    


set_volume(50)
display.show(Image.YES)
sleep(100)
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
            running = 0
            # reset display
            showTimerLengthSetting()
        else:
            running = 1
            time_0 = running_time()
            display.scroll(timer_length)

    if button_a.was_pressed():
        if running:
            running = 0
            updateTimerDisplay(25)
            sleep(500)
            showTimerLengthSetting()
        else:
            # toggle timer
            if timer_length == 25:
                timer_length = 5
                display.scroll(timer_length)
                showTimerLengthSetting()
            else:
                timer_length = 25
                display.scroll(timer_length)
                showTimerLengthSetting()
    if pin_logo.is_touched():
        if running:
            running = 0
            updateTimerDisplay(15)
            sleep(600)
            showTimerLengthSetting()
        else:
            for i in range(len(timer_length_list)):
                if timer_length == timer_length_list[i]:
                    if i == len(timer_length_list) - 1:
                        timer_length = timer_length_list[0]
                        break
                    else:
                        timer_length = timer_length_list[i + 1]
                        break
            else:
                timer_length=25
            display.scroll(timer_length)
            showTimerLengthSetting()

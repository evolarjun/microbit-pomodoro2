# microbit-pomodoro2
Second try at a microbit pomodoro timer. This time with micropython which is easer than make:code

My first attempt started with my son and the visual programming tools at make:code (though I switched to python mode at one point) https://github.com/evolarjun/pomodor-timer.

In this version the system is event driven and much more responsive to the button presses. I probably could have done this with the Make:Code version, but I kept running into issues. The micropython version was easier for me to grok and get through. Possibly if I had started with the python at Make:Code I wouldn't have struggled as much there.

Used https://python.microbit.org/v/3/reference to edit and flash the microbit.

Chrome on my Mac has the USB connection feature and can send on one click without requiring the copy to a USB drive.

This has been useful for me.  First I noticed a 25 minute warning was kind of neat when I was running 1/2 hour meetings, but what about my 15 minute meetings, then I thought if I double 25 it's 50 minutes and maybe that'll work for my 50 minute meetings. Then 5 minutes was a good idea.

Note that when not running the fist two rows will be dar. Each light starting in the 3rd (middle) row stands for 5 minutes. Button A changes the timer length and button B is a start / reset button. There isn't a pause function at this point, though I should probably add one using the logo.  I noticed that enabiling touch sensitivity on the bottom pins causes fickering in the 4th row sometimes. I don't understand why, but the only way I was able to get it to stop was to not enable capactitative touch on pins 1 2 and 3.

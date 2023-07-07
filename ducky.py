import keyboard, os, subprocess
from random import choice

# wav format to reduce time processing/delay
a = ['\p1.wav', '\p2.wav', '\p3.wav']
p = os.getcwd()

def duck(e): 
    aa = p + choice(a)
    subprocess.Popen(["ffplay", "-nodisp", "-autoexit", aa])

keyboard.on_press(duck)
keyboard.wait("esc")
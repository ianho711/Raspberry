#! usr/bin/python3
import RPi.GPIO as GPIO
from tkinter import *

class App():
    def __init__(self, main):
        self.ledState = False
        main.title("Led Control")
        main.geometry("300x200")
        main.option_add("*Font",("verdana",18,"bold"))
        main.option_add("*Label.Font",("verdana",18))
        main.option_add("*Button.Background", "light blue")
        mainFrame = Frame(main)
        self.button = Button(mainFrame,text="LED Open",padx=40,pady=40,command=self.userClick)
        self.button.pack(expand=YES)

        mainFrame.pack(expand=YES, fill=BOTH)
        
    def userClick(self):
        print("userClick")
        if self.ledState:
            self.ledState = False
            GPIO.output(25, GPIO.LOW)
            self.button.config(text="LED Open")
        else:
            self.ledState = True
            GPIO.output(25, GPIO.HIGH)
            self.button.config(text="LED Close")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    #GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setup(25, GPIO.OUT)

    window = Tk()
    app = App(window)
    window.mainloop()

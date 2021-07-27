import tkinter as tk
from pyo import *
import numpy as np
import time

#creat a window to place our UI elements

s= Server(duplex=1, buffersize=1024, winhost='asio',nchnls=2)
s.boot()
s.start()

# Drops the gain by 20 dB.
s.amp = 0.1
SND_PATH = 'C:/Users/jonathan/PycharmProjects/pythonProject/'
sndnames = ["carousel1", "cheer1", "elephant1", "kids1", "wheel1"]
channels = []
rotations = []
elevations = []
spans = []
players = []

for name in sndnames:
    path = SND_PATH + name + '.wav'
    channels.append(path)
    rotations.append(Phasor(0.2, mul=360))
#    rotations.append(30)
    elevations.append(Sine(0.1).range(-90, 90))
    spans.append(Sine(0.3).range(0, 1))

for channel in channels:
    players.append(SfPlayer(channel,loop=0))

oscs = np.column_stack((players, rotations, elevations, spans))
oscillators = []
for osc in oscs:
    oscillators.append(Binaural(osc[0], azimuth=osc[1], elevation=osc[2], azispan=osc[3]))

def play_sound(slider):
    signal = sum(oscillators)
    signal.out()
    time.sleep(1)
    slider.destroy()
#    s.gui(locals())

window = tk.Tk()
window.geometry("600x600")

def createNewWindow(str):
    current_value = tk.DoubleVar()
    def get_current_value():
        return '{: .2f}'.format(current_value.get())
    def slider_changed(event):
        value_label.configure(text=get_current_value())

    newWindow = tk.Toplevel(window)
    newWindow.geometry('450x150')
    newWindow.resizable(False, False)
    newWindow.title(str)
    newWindow.columnconfigure(0, weight=1)
    newWindow.columnconfigure(1, weight=3)

    slider_label = tk.Label(newWindow, text='On a scale of 1-10, how much do you feel of this emotion?')
    slider_label.grid(column=0, row=0, sticky='w')

    value_label = tk.Label(newWindow, text=get_current_value())
    value_label.grid(row=2, columnspan=2, sticky='n')

    slider = tk.Scale(newWindow, from_=1, to=10, orient='horizontal', command=slider_changed, variable=current_value)
    slider.grid(column=0, row=1, sticky='we')

    buttonConfirm = tk.Button(newWindow, text = "Confirm", command=lambda: play_sound(newWindow))
    buttonConfirm.grid(columnspan=2, row=3, sticky='w')


# Create an event handler for the buttons

def button_pressed(event):
    createNewWindow(event)

# Place buttons relative to each other
button_01 = tk.Button(text="Anger",
                      highlightbackground = "red",
                      command= lambda :
                      button_pressed("Anger emotion scale"))
button_01.place(height=300, width=300)

button_02 = tk.Button(text="Fear",
                      highlightbackground = "black",
                      command= lambda :
                      button_pressed("Fear emotion scale") )
button_02.place(height=300, width=300,relx=0.5)

button_03 = tk.Button(text="Sadness",
                      highlightbackground = "blue",
                      command= lambda :
                      button_pressed("Sadness emotion scale"))
button_03.place(height=300, width=300,rely=0.5)

button_04 = tk.Button(text="Happiness",
                      highlightbackground="yellow",
                      command= lambda :
                      button_pressed("Happiness emotion scale"))
button_04.place(height=300, width=300,relx=0.5,rely=0.5)

#This event loop listens to event such as the press of a button
window.mainloop()
s.gui(locals())


#ch1Binaural = HRTF(players[0], azimuth=rotations[0], elevation=elevations[0])
#ch2Binaural = HRTF(players[1], azimuth=rotations[1], elevation=elevations[1])
#ch3Binaural = HRTF(players[2], azimuth=rotations[2], elevation=elevations[2])


#mixer = Mixer(outs=2,chnls=2)

#mixer.addInput(0,ch1Binaural)
#mixer.addInput(1,ch2Binaural)
#mixer.addInput(2,ch3Binaural)


#mixer.setAmp(0,0,0.5)
#mixer.setAmp(0,1,0.5)
#mixer.setAmp(1,0,0.5)
#mixer.setAmp(1,1,0.5)
#mixer.setAmp(2,0,0.5)
#mixer.setAmp(2,1,0.5)

#mixer.out()

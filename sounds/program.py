import tkinter as tk
from pyo import *
import numpy as np

s = Server()
s.boot()
s.start()

s.amp = 0.4
SND_PATH = './sounds/'
sndnames = ["ambience1", "stomp"]
channels = []
rotations = []
elevations = []
spans = []
players = []

for name in sndnames:
    path = SND_PATH + name + '.wav'
    channels.append(path)
    rotations.append(Phasor(0.8, mul=360))
    elevations.append(Sine(0.1).range(-90, 90))
    spans.append(Sine(0.3).range(0, 1))

for channel in channels:
    players.append(SfPlayer(channel, loop=0))

oscs = np.column_stack((players, rotations, elevations, spans))
oscillators = []
for osc in oscs:
    if sys.platform == "win32":
        oscillators.append(Binaural(osc[0], azimuth=osc[1], elevation=osc[2], azispan=osc[3]))
    else:
        oscillators.append(HRTF(osc[0], azimuth=osc[1], elevation=osc[2]))

def play_sound(slider):
    signal = sum(oscillators)
    signal.out()
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

    buttonConfirm = tk.Button(newWindow, text="Confirm", command=lambda: play_sound(newWindow))
    buttonConfirm.grid(columnspan=2, row=3, sticky='w')


# Create an event handler for the buttons

def button_pressed(event):
    createNewWindow(event)


# Place buttons relative to each other
button_01 = tk.Button(text="Anger",
                      highlightbackground="red",
                      command=lambda:
                      button_pressed("Anger emotion scale"))
button_01.place(height=300, width=300)

button_02 = tk.Button(text="Fear",
                      highlightbackground="black",
                      command=lambda:
                      button_pressed("Fear emotion scale"))
button_02.place(height=300, width=300, relx=0.5)

button_03 = tk.Button(text="Sadness",
                      highlightbackground="blue",
                      command=lambda:
                      button_pressed("Sadness emotion scale"))
button_03.place(height=300, width=300, rely=0.5)

button_04 = tk.Button(text="Happiness",
                      highlightbackground="yellow",
                      command=lambda:
                      button_pressed("Happiness emotion scale"))
button_04.place(height=300, width=300, relx=0.5, rely=0.5)

# This event loop listens to event such as the press of a button
window.mainloop()
s.gui(locals())

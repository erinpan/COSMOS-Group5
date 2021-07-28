import tkinter as tk
import numpy as np
from pyo import *
import random
import time
import webbrowser


def callback(url):
    webbrowser.open_new(url)


s = Server(duplex=1, buffersize=1024, winhost='asio', nchnls=2)
s.boot()
s.start()
pool = ['a', 'f', 's', 'h']


def play_sound(slider):
    temp = pool[random.randrange(3)]
    if temp == "a":
        SND_PATH = './sounds/'
        sndnames = ["sirens", "honking1", "peets"]
        channels = []
        rotations = []
        elevations = []
        spans = []
        players = []

        for name in sndnames:
            path = SND_PATH + name + '.wav'
            channels.append(path)
            rotations.append(Phasor(0.2, mul=360))
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
        sum(oscillators).out()
    elif temp == "f":
        sound_path = "./sounds/hauntedhouse.wav"
        sound_player = SfPlayer(sound_path, loop=True)
        ele = 30
        azi = Sine(0.1).range(0, 360)

        binaural_renderer = Binaural(sound_player, azimuth=azi, elevation=ele, azispan=0, elespan=0)
        binaural_renderer.out()
    elif temp == "s":
        sound_path = "./sounds/RainforestEnvComp1.wav"
        sound_player = SfPlayer(sound_path, loop=True)
        ele = 30
        azi = Sine(0.1).range(0, 360)

        binaural_renderer = Binaural(sound_player, azimuth=azi, elevation=ele, azispan=0, elespan=0)
        binaural_renderer.out()
    else:
        sound_player = SfPlayer("./sounds/carnival_3.wav", loop=False)
        ele = 45
        azi = Sine(0.1).range(0, 360)

        binaural_renderer = Binaural(sound_player, azimuth=azi, elevation=ele, azispan=0, elespan=0)
        binaural_renderer.out()

    slider.destroy()
    #placeholder
    time.sleep(90)
    quit()

window = tk.Tk()
window.geometry("600x600")
root = tk.Tk()
link1 = tk.Label(root, text="Google Form Hyperlink", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://forms.gle/KfTjk8Abzt2yadmR6"))

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


def button_pressed(event):
    global pool
    pool.remove(event)
    if event == "a":
        createNewWindow("Anger Emotion Scale")
    elif event == "s":
        createNewWindow("Sadness/Calmness Emotion Scale")
    elif event == "f":
        createNewWindow("Fear Emotion Scale")
    else:
        createNewWindow("Happiness Emotion Scale")


# Place buttons relative to each other
button_01 = tk.Button(text="Anger",
                      highlightbackground="red",
                      command=lambda:
                      button_pressed("a"))
button_01.place(height=300, width=300)

button_02 = tk.Button(text="Fear",
                      highlightbackground="black",
                      command=lambda:
                      button_pressed("f"))
button_02.place(height=300, width=300, relx=0.5)

button_03 = tk.Button(text="Sadness/Calmness",
                      highlightbackground="blue",
                      command=lambda:
                      button_pressed("s"))
button_03.place(height=300, width=300, rely=0.5)

button_04 = tk.Button(text="Happiness",
                      highlightbackground="yellow",
                      command=lambda:
                      button_pressed("h"))
button_04.place(height=300, width=300, relx=0.5, rely=0.5)


window.mainloop()
s.gui(locals())

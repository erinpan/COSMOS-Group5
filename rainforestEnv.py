from pyo import *

SNDS_PATH = r"C:\Users\Emmy Chen\Cluster5\myProject\RainforestEnvComp1.wav"

s= Server(duplex=1, buffersize=1024, winhost='asio',nchnls=2)
s.boot()
s.start()



sound_player = SfPlayer(SNDS_PATH, loop=True)
ele = 30
azi = Sine(0.1).range(0,360)

binaural_renderer = Binaural(sound_player, azimuth=azi, elevation=ele, azispan=0, elespan=0)
binaural_renderer.out()

s.gui(locals())

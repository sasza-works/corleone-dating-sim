
# music paths
define audio.chillout = "music/chillout.mp3"
define audio.humansound = [ "sound/ahh1.wav", "sound/ahh2.wav", "sound/ahh3.wav", "sound/ahh4.wav", "sound/hhh.wav", "sound/bime.wav"]
define audio.snekmiss = "sound/uhh.wav"

init python:
    def snekeatersounds(): 
        return renpy.random.choice(audio.humansound)
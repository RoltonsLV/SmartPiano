from play_sound_by_pygame import play_sound
from threading import Thread
from time import sleep


def drum_beat():
    while True:
        play_sound("voxy-SNARE1.wav")
        sleep(0.4)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.4)

def bass():
    sleep(6.4)
    while True:
        play_sound("126_Fm_TheGridArpBass_02_550.wav")
        sleep(7.7)

def cymbals():
    sleep(12.4)
    while True:
        for i in range(25):
            play_sound("11_HiHats_02_34_SP.wav")
            sleep(0.4)
        for j in range(25):
            play_sound("11_HiHats_02_34_SP.wav")
            sleep(0.2)
            play_sound("11_HiHats_02_34_SP.wav")
            sleep(0.2)
            
        sleep(8.8)
        play_sound("BlofeldCowbell_02_550.wav")
        sleep(0.4)
        play_sound("BlofeldCowbell_02_550.wav")
        sleep(0.4)
        play_sound("BlofeldCowbell_02_550.wav")
        sleep(0.4)
        play_sound("BlofeldCowbell_02_550.wav")
        sleep(0.2)
        play_sound("BlofeldCowbell_02_550.wav")
        sleep(0.2)
        for o in range(25):
            play_sound("11_HiHats_02_34_SP.wav")
            sleep(0.2)
            play_sound("11_HiHats_02_34_SP.wav")
            sleep(0.2)


def synths():
    sleep(6.4)
    while True:
        for i in range(4):
            play_sound("Am_PhattyStabSynth_01_550.wav")
            sleep(1.6)
            play_sound("cyborg-05-TTweat.wav")
            sleep(1.6)
            play_sound("F_PhattyStabSynth_02_550.wav")
            sleep(1.6)
            play_sound("cyborg-05-TTweat.wav")
            sleep(1.6)
        play_sound("Am_PhattyStabSynth_01_550.wav") 
        sleep(10.9)

def main():
    threadDrums = Thread(target=drum_beat)
    thread2Bass = Thread(target=bass)
    threadCymbals = Thread(target=cymbals)
    threadSynths = Thread(target=synths)

    threadDrums.start()
    thread2Bass.start()
    threadCymbals.start()
    threadSynths.start()

    threadDrums.join()
    thread2Bass.join()
    threadCymbals.join()
    threadSynths.join()

main()

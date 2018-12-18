#! coding: UTF-8
import pygame.midi
import time

PROGRAM_CHANGE = 0xC0


def handle_events(events):
    """Handle MIDI events"""
    for event in events:
        data = event[0]
        timestamp = event[1]
        cmd = data[0]
        if cmd == PROGRAM_CHANGE:
            progNum = data[1]
            print("Program number {}".format(progNum))
            if progNum == 0:
                print("Regn...")
                pygame.mixer.Sound.play(soundRain)
            if progNum == 1:
                print("Åska!!!")
                pygame.mixer.Sound.play(soundThunder)
            
    
def runRiders():
    """Roders on the storm"""
    pygame.midi.init()
    pygame.mixer.init()
    path = r"/media/daniel/Data/Treo/"
    soundRain = pygame.mixer.Sound(path + r"Regn.wav")
    soundThunder = pygame.mixer.Sound(path + r"Åska.wav")

    print(pygame.midi.get_default_output_id())
    for i in range(pygame.midi.get_count()):
        info = pygame.midi.get_device_info(i)
        if info[2]:
            print("{}: Input: {}".format(i, info))
            if "E-MU" in info[1]:
                emuID = i
    midiIn = pygame.midi.Input(emuID)
#  pygame.mixer.music.load(r"/home/daniel/Music/Treo/Åska.wav")
#  pygame.mixer.music.load(r"/home/daniel/Music/Treo/Treo-Falling_en_inspelning.mp3")
    
    while True:
        events = midiIn.read(10)
        handle_events(events)
        time.sleep(0.1)

if __name__ == "__main__":
    pygame.midi.init()

    print(pygame.midi.get_default_output_id())
    for i in range(pygame.midi.get_count()):
        info = pygame.midi.get_device_info(i)
        if info[2]:
            print("{}: Input: {}".format(i, info))
        if info[3]:
            print("{}: Output: {}".format(i, info))
        else:
            print("{}: Unknown: {}".format(i, info))
    
    
    midiOut = pygame.midi.Output(7)
    note = 64
#     midiOut.note_on(note,60,channel=0)
#     midiOut.note_on(note+4,60,channel=0)
#     midiOut.note_on(note+7,60,channel=0)
#     
    # Pitch bend
    midiOut.write_short(0xE0, 0x00, 0x45)
    print("Wow!")


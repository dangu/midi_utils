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
            print "Program number {}".format(progNum)
            
    
if __name__ == "__main__":
    pygame.midi.init()
    print pygame.midi.get_default_output_id()
    for i in range(pygame.midi.get_count()):
        info = pygame.midi.get_device_info(i)
        if info[2]:
            print "{}: Input: {}".format(i, info)
    midiIn = pygame.midi.Input(5)
    while True:
        events = midiIn.read(10)
        handle_events(events)
        time.sleep(0.1)
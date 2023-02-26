import mido
import mido_test

SYSEX_START = 0xF0
SYSEX_END = 0xF7

def print_messages():
    """Print all incoming messages"""
    print(mido.get_input_names())
    in_name = 'E-MU 0404 | USB:E-MU 0404 | USB MIDI 1 20:0'

    with mido.open_input(in_name) as inport:
        for msg in inport:
            print(msg)

def create_syx_file_from_midi():
    """Get midi data and dump to syx file"""
    folderPath = "/home/daniel/Lokalt/midi_utils/dumps/"

    filenameOutSyx = folderPath + "out3.syx"

    print(mido.get_input_names())
    in_name = 'E-MU 0404 | USB:E-MU 0404 | USB MIDI 1 20:0'

    with mido.open_input(in_name) as inport:
        for msg in inport:
            if msg.type == "sysex":
                
                mido.write_syx_file(filenameOutSyx, [msg])
                print("Sysex dumped to " + filenameOutSyx)
    
def createSyxFile():
    """Create .syx file from dump"""

    folderPath = "/home/daniel/Lokalt/midi_utils/dumps/"
    filenameIn = folderPath + "ACC_pretty_9"

    filenameOutSyx = folderPath + "out1.syx"
    filenameOutSyxTxt = folderPath + "out1.txt"
    
    sysexBytes = [SYSEX_START]
    with open(filenameIn, 'rb') as f1:
        for x in f1:
            for sysexByteStr in x.split():
                sysexByte = int(sysexByteStr, 16)
                sysexBytes.append(sysexByte)

    sysexBytes.append(SYSEX_END)

    messages=[]
    messages.append(mido.parse(sysexBytes))
    print(f"message: {messages[0].type} Length: {len(sysexBytes)}")
    print(f"mido message: {len(messages[0].data)}")

    mido.write_syx_file(filenameOutSyx, messages)
    mido.write_syx_file(filenameOutSyxTxt, messages, plaintext=True)
    #filename = "test.syx"

    #messages = mido.read_syx_file(filename)

def run():
    """Run"""
    #create_syx_file_from_midi()
    print_messages()
    
    
def run2():
    """Run"""
    folderPath = "/home/daniel/Lokalt/midi_utils/dumps/"
    filenameInSyx = folderPath + "out1.syx"
    
    messagesIn = mido.read_syx_file(filenameInSyx)

    if len(messagesIn) != 1:
        print("Can handle only one message")
        raise

    message = messagesIn[0]
    
    fs680Syx=mido_test.FS680_sysex(name="test1")
    fs680Syx.from_message(message)
    header = fs680Syx.parse_header()
    print(header)

    fs680Syx.get_accs()
    
    
if __name__ == '__main__':
    run()

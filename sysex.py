import mido

SYSEX_START = 0xF0
SYSEX_END = 0xF7


def run():
    """Run"""
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

    messagesIn = mido.read_syx_file(filenameOutSyx)

    for idx, syxByte in enumerate(messagesIn[0].data):
        if messages[0].data[idx] != syxByte:
            print(f"{messages[0][idx]:02X} != {syxByte:02X} at index {idx}")
            break
    print(f"Compared {idx+1} bytes")

if __name__ == '__main__':
    run()

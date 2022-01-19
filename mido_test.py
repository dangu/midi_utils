import mido
import logging

logger = logging.getLogger()
#sysex data=(64,0,33,5,3,1,1,0,3,3,8,0,11,0,11,0,11,0,11,0,11,0,10,0,10,0,10,0,8,3,10,3,6,0,7,2,0,0,1,0,3,3,8,0,12,0,12,0,11,0,11,0,11,0,4,1,10,1,9,1,9,3,7,3,2,0,6,3,0,0,1,0,3,3,8,0,14,0,14,0,11,0,11,0,11,0,2,4,4,0,14,1,9,3,14,1,1,0,13,1,0,0,1,0,3,2,8,0,14,0,14,0,11,0,11,0,11,0,3,2,1,2,0,0,9,3,13,0,2,0,6,2,0,0,1,0,3,2,8,0,10,0,10,0,11,0,11,0,11,0,6,5,0,2,2,3,9,3,0,1,1,0,11,0,0,0,1,0,3,3,8,0,14,0,14,0,11,0,11,0,11,0,5,4,13,4,9,1,9,1,8,5,1,0,1,2,0,0,1,0,3,2,8,0,10,0,10,0,11,0,11,0,11,0,8,0,10,0,4,2,8,3,3,4,2,0,0,2,0,0,1,0,3,1,8,0,9,0,9,0,11,0,11,0,11,0,5,2,14,0,0,0,8,3,4,4,2,0,0,2,0,0,5,0,0,0,8,0,14,0,14,0,11,0,11,0,11,0,0,4,0,0,8,1,8,3,11,5,1,0,13,0,0,0,5,0,0,0,8,0,13,0,13,0,11,0,11,0,11,0,12,0,15,1,10,0,8,3,2,3,2,0,13,2,0,0,1,0,3,3,8,0,11,0,11,0,11,0,11,0,11,0,10,0,10,0,10,0,8,3,10,3,6,0,7,2,0,0,1,0,3,3,8,0,12,0,12,0,11,0,11,0,11,0,4,1,10,1,9,1,9,3,7,3,2,0,6,3,0,0,1,0,3,3,8,0,14,0,14,0,11,0,11,0,11,0,2,4,4,0,14,1,9,3,14,1,1,0,13,1,0,0,1,0,3,2,8,0,14,0,14,0,11,0,11,0,11,0,3,2,1,2,0,0,9,3,13,0,2,0,6,2,0,0,1,0,3,2,8,0,10,0,10,0,11,0,11,0,11,0,6,5,0,2,2,3,9,3,0,1,1,0,11,0,0,0,1,0,3,3,8,0,14,0,14,0,11,0,11,0,11,0,5,4,13,4,9,1,9,1,8,5,1,0,1,2,0,0,1,0,3,2,8,0,10,0,10,0,11,0,11,0,11,0,8,0,10,0,4,2,8,3,3,4,2,0,0,2,0,0,1,0,3,1,8,0,9,0,9,0,11,0,11,0,11,0,5,2,14,0,0,0,8,3,4,4,2,0,0,2,0,0,5,0,0,0,8,0,14,0,14,0,11,0,11,0,11,0,0,4,0,0,8,1,8,3,11,5,1,0,13,0,0,0,5,0,0,0,8,0,13,0,13,0,11,0,11,0,11,0,12,0,15,1,10,0,8,3,2,3,2,0,13,2,0,0) time=0
# SYN
# sysex data=(64,0,33,5,3,0,15,5,0,6,1,6,2,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,6,1,0,4,1,4,14,14,14,14,2,4,14,14,1,0,6,1,0,4,1,4,15,14,15,14,2,4,15,14,1,0,6,1,0,5,2,5,14,14,14,14,2,4,14,14,1,0,6,1,0,5,2,5,15,14,15,14,2,4,15,14,1,0,6,1,0,5,2,5,15,14,15,14,2,4,15,14,2,10,6,14,1,0,1,0,4,8,1,0,14,8,8,8,2,10,8,14,1,0,1,0,4,8,1,0,6,8,9,4,2,10,14,13,1,0,1,0,4,8,1,0,7,8,9,4,1,12,4,1,0,6,1,3,9,11,9,11,14,4,9,11,1,12,4,1,0,6,1,3,10,11,10,11,14,4,10,11,1,12,4,1,0,6,2,3,11,11,11,11,14,4,11,11,1,12,4,1,0,6,2,3,12,11,12,11,14,4,12,11,1,12,4,1,0,6,2,3,13,11,13,11,14,4,13,11,9,15,8,13,8,4,1,0,4,8,1,0,4,12,14,8,5,15,2,15,14,0,1,0,4,8,1,0,8,8,10,4,5,15,12,14,4,4,1,0,4,8,1,0,10,8,11,4,1,8,8,0,0,5,1,7,0,2,15,7,15,7,0,2,1,8,8,0,0,5,1,7,0,2,15,7,15,7,0,2,1,8,8,0,0,5,2,7,0,2,15,7,15,7,0,2,1,8,8,0,0,5,2,7,0,2,15,7,15,7,0,2,1,8,8,0,0,5,2,7,0,2,15,7,15,7,0,2,7,14,0,15,1,0,1,0,4,8,1,0,10,8,11,8,3,14,0,15,1,0,1,0,4,8,1,0,10,8,6,4,3,14,12,14,1,0,1,0,4,8,1,0,10,8,7,4,1,8,8,0,0,6,1,6,0,12,15,14,6,6,0,12,1,8,8,0,0,6,1,6,0,12,15,14,6,6,0,12,1,8,8,0,0,6,2,6,0,12,15,14,6,6,0,12,1,8,8,0,0,6,2,6,0,12,15,14,6,6,0,12,1,8,8,0,0,6,2,6,0,12,15,14,6,6,0,12,14,15,14,15,4,12,1,0,4,8,1,0,4,12,11,4,14,15,14,15,4,12,1,0,4,8,1,0,4,12,11,4,14,15,14,15,4,12,1,0,4,8,1,0,4,12,11,4,1,8,8,0,0,3,1,3,0,2,11,10,15,7,0,2,1,8,8,0,0,3,1,3,0,2,11,10,15,7,0,2,1,8,8,0,0,3,2,3,0,2,11,10,15,7,0,2,1,8,8,0,0,3,2,3,0,2,11,10,15,7,0,2,1,8,8,0,0,3,2,3,0,2,11,10,15,7,0,2,14,15,8,15,13,4,1,0,4,8,1,0,12,8,11,4,14,15,8,15,13,4,1,0,4,8,1,0,12,8,11,4,14,15,6,15,13,4,1,0,4,8,1,0,12,8,11,4) time=0
# ACC


class FS680_sysex:
    """Kawai FS680 sysex message
    F0    Sysex start
    40    Manufacturer ID: Kawai
    """
    def __init__(self, name):
        """Init"""
        self.name = name
        self.syx_data = None
        
    def from_message(self, message):
        """Set message"""
        self.syx_data = message.data
        
    def from_hex_file(self, filename):
        """Get data from file with hex data"""
        self.syx_data = []
        with open(filename, "r") as f1:
            for line in f1:
                self.syx_data += [int(x,16) for x in line.split()]
                

        
    def from_file(self, filename):
        """Get data from file"""
        with open(filename, "r") as f1:
            file_data_raw=f1.readlines()
            
        assert(len(file_data_raw)==1)
        self.file_data = [int(x) for x in file_data_raw[0].strip().split(',')]
        
        for idx,data_byte in enumerate([64,0,33,5,3]):
            assert(self.file_data[idx]==data_byte)
            
        self.syx_data = self.file_data  #[1:-1]
        
    def pretty_print(self):
        """Pretty print data
        REG:
        40 00 21 05 03 01 01 00 03 03 08 00 0B 00 0B 00
0B 00 0B 00 0B 00 0A 00 0A 00 0A 00 08 03 0A 03

        40 Manufacturer ID (3 bytes)
        00 
        21 
        05 Device ID
        03 Model ID
        01 Command
        01 Instrument ID ?
        00 Version ID ?
        03 
        03 08 00 0B 00 0B 00


        
        SYN:
        40 00 21 05 03 00 0F 05 00 06 01 06 02 06 03 06
        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        
        40 Manufacturer ID (3 bytes)      
        00                                
        21                                
        05 Device ID                      
        03 Model ID                       
        00 Command                        
        0F Instrument ID ?                
        05 Version ID ?                   
        00 
        06 01 06 02 06 03 06
        
        Kawai K1 data dump:
        Type: All Data Dump (*)
Note: Kawai K1 SysEx dump of sound bank (original name = A101.syx)
Head:F0 40 00 21 00 03 01 00 50 65 61 63 65 20 20 20 20 20 57 05 32 42 32 0C 1E 21 34 2F 33 32
Uploader: andrea1
        
        
        See SINGLE DATA LIST regarding the data.

0   Status         11110000   F0H   System exclusive
1   Kawai ID no.   01000000   40H
2   Channel no.      0000nnnn   0nH
3   Function no.   00100000   20H   One block data dump
4   Group no.      00000000   00H   Synthesizer group
5   Machine ID no.   00000011   03H   K1/K1M ID. no.
6   Sub command 1   0000000x   00H   Internal; 01H   External                           
7   Sub command 2   0xxxxxxx   0 - 63 SINGLE A-1 - d-8
8   Data          0xxxxxxx    Patch data s0
    Data          0xxxxxxx    Patch data s1
                  |
    Data          0xxxxxxx    Patch data s86
95  Data          0xxxxxxx    Patch data s87 
96  EOX            11110111   F7H
        
        """
        col = 0
        max_col = 16
        pretty_string = ""
        for data_byte in self.syx_data:
            pretty_string += f"{data_byte:02X} "
            col += 1
            if col >= max_col:
                pretty_string = pretty_string[:-1] + "\n"
                col = 0
        return pretty_string
    
    def print_reg(self):
        """The registration format"""
        
        
    def create_checksum(self, start_idx):
        """Create checksum"""
        sum=0
        for data_byte in self.syx_data[start_idx:-1]:
            sum = (sum+data_byte)&0x7F
        sum = (~sum)+1
        logger.info(f"Sum with idx {start_idx}: {sum}")
            
        
    def investigate(self):
        """Investigate data"""
        logger.info(f"Name: {self.name} Len: {len(self.syx_data):7} Data: {self.syx_data[:10]}")
        logger.info(f"Data: {self.syx_data[:10]}")
        self.print_reg()
#        self.dump_to_file(filename = self.name + "_pretty")
        # for idx in range(20):
        #     self.create_checksum(start_idx = idx)

    def dump_to_file(self, filename):
        """Dump to file"""
        with open(filename, 'w') as f1:
            f1.write(self.pretty_print())
    

    
def run():
    logging.basicConfig(format='%(asctime)s %(message)s',
                        filename='mido.log', 
                        encoding='utf-8',
                        level=logging.DEBUG)
    
    
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # add formatter to ch
    ch.setFormatter(formatter)
    
    # add ch to logger
    logger.addHandler(ch)

    logger.setLevel("DEBUG")
    input_name = "M Audio Audiophile 24/96:M Audio Audiophile 24/96 MIDI 24:0"
    
    input_port = mido.open_input(input_name)
    sysex_dict = {}
    for key in ["REG"]: #, "SYN", "ACC", "OFA"]:
        logger.info(f"Receive {key}...")
        sysex_dict[key] = FS680_sysex(name = key)
        #sysex_dict[key].from_message(message=input_port.receive())
        sysex_dict[key].from_hex_file(filename=key+"_pretty")
        
    for _,syx in sysex_dict.items():
        syx.investigate()
        
    logger.info("Done")

    
if __name__=="__main__":
    run()


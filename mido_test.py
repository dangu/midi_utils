import mido
import logging
import time

from random import randrange
from pickle import NONE

logger = logging.getLogger()
#sysex data=(64,0,33,5,3,1,1,0,3,3,8,0,11,0,11,0,11,0,11,0,11,0,10,0,10,0,10,0,8,3,10,3,6,0,7,2,0,0,1,0,3,3,8,0,12,0,12,0,11,0,11,0,11,0,4,1,10,1,9,1,9,3,7,3,2,0,6,3,0,0,1,0,3,3,8,0,14,0,14,0,11,0,11,0,11,0,2,4,4,0,14,1,9,3,14,1,1,0,13,1,0,0,1,0,3,2,8,0,14,0,14,0,11,0,11,0,11,0,3,2,1,2,0,0,9,3,13,0,2,0,6,2,0,0,1,0,3,2,8,0,10,0,10,0,11,0,11,0,11,0,6,5,0,2,2,3,9,3,0,1,1,0,11,0,0,0,1,0,3,3,8,0,14,0,14,0,11,0,11,0,11,0,5,4,13,4,9,1,9,1,8,5,1,0,1,2,0,0,1,0,3,2,8,0,10,0,10,0,11,0,11,0,11,0,8,0,10,0,4,2,8,3,3,4,2,0,0,2,0,0,1,0,3,1,8,0,9,0,9,0,11,0,11,0,11,0,5,2,14,0,0,0,8,3,4,4,2,0,0,2,0,0,5,0,0,0,8,0,14,0,14,0,11,0,11,0,11,0,0,4,0,0,8,1,8,3,11,5,1,0,13,0,0,0,5,0,0,0,8,0,13,0,13,0,11,0,11,0,11,0,12,0,15,1,10,0,8,3,2,3,2,0,13,2,0,0,1,0,3,3,8,0,11,0,11,0,11,0,11,0,11,0,10,0,10,0,10,0,8,3,10,3,6,0,7,2,0,0,1,0,3,3,8,0,12,0,12,0,11,0,11,0,11,0,4,1,10,1,9,1,9,3,7,3,2,0,6,3,0,0,1,0,3,3,8,0,14,0,14,0,11,0,11,0,11,0,2,4,4,0,14,1,9,3,14,1,1,0,13,1,0,0,1,0,3,2,8,0,14,0,14,0,11,0,11,0,11,0,3,2,1,2,0,0,9,3,13,0,2,0,6,2,0,0,1,0,3,2,8,0,10,0,10,0,11,0,11,0,11,0,6,5,0,2,2,3,9,3,0,1,1,0,11,0,0,0,1,0,3,3,8,0,14,0,14,0,11,0,11,0,11,0,5,4,13,4,9,1,9,1,8,5,1,0,1,2,0,0,1,0,3,2,8,0,10,0,10,0,11,0,11,0,11,0,8,0,10,0,4,2,8,3,3,4,2,0,0,2,0,0,1,0,3,1,8,0,9,0,9,0,11,0,11,0,11,0,5,2,14,0,0,0,8,3,4,4,2,0,0,2,0,0,5,0,0,0,8,0,14,0,14,0,11,0,11,0,11,0,0,4,0,0,8,1,8,3,11,5,1,0,13,0,0,0,5,0,0,0,8,0,13,0,13,0,11,0,11,0,11,0,12,0,15,1,10,0,8,3,2,3,2,0,13,2,0,0) time=0
# SYN
# sysex data=(64,0,33,5,3,0,15,5,0,6,1,6,2,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,6,1,0,4,1,4,14,14,14,14,2,4,14,14,1,0,6,1,0,4,1,4,15,14,15,14,2,4,15,14,1,0,6,1,0,5,2,5,14,14,14,14,2,4,14,14,1,0,6,1,0,5,2,5,15,14,15,14,2,4,15,14,1,0,6,1,0,5,2,5,15,14,15,14,2,4,15,14,2,10,6,14,1,0,1,0,4,8,1,0,14,8,8,8,2,10,8,14,1,0,1,0,4,8,1,0,6,8,9,4,2,10,14,13,1,0,1,0,4,8,1,0,7,8,9,4,1,12,4,1,0,6,1,3,9,11,9,11,14,4,9,11,1,12,4,1,0,6,1,3,10,11,10,11,14,4,10,11,1,12,4,1,0,6,2,3,11,11,11,11,14,4,11,11,1,12,4,1,0,6,2,3,12,11,12,11,14,4,12,11,1,12,4,1,0,6,2,3,13,11,13,11,14,4,13,11,9,15,8,13,8,4,1,0,4,8,1,0,4,12,14,8,5,15,2,15,14,0,1,0,4,8,1,0,8,8,10,4,5,15,12,14,4,4,1,0,4,8,1,0,10,8,11,4,1,8,8,0,0,5,1,7,0,2,15,7,15,7,0,2,1,8,8,0,0,5,1,7,0,2,15,7,15,7,0,2,1,8,8,0,0,5,2,7,0,2,15,7,15,7,0,2,1,8,8,0,0,5,2,7,0,2,15,7,15,7,0,2,1,8,8,0,0,5,2,7,0,2,15,7,15,7,0,2,7,14,0,15,1,0,1,0,4,8,1,0,10,8,11,8,3,14,0,15,1,0,1,0,4,8,1,0,10,8,6,4,3,14,12,14,1,0,1,0,4,8,1,0,10,8,7,4,1,8,8,0,0,6,1,6,0,12,15,14,6,6,0,12,1,8,8,0,0,6,1,6,0,12,15,14,6,6,0,12,1,8,8,0,0,6,2,6,0,12,15,14,6,6,0,12,1,8,8,0,0,6,2,6,0,12,15,14,6,6,0,12,1,8,8,0,0,6,2,6,0,12,15,14,6,6,0,12,14,15,14,15,4,12,1,0,4,8,1,0,4,12,11,4,14,15,14,15,4,12,1,0,4,8,1,0,4,12,11,4,14,15,14,15,4,12,1,0,4,8,1,0,4,12,11,4,1,8,8,0,0,3,1,3,0,2,11,10,15,7,0,2,1,8,8,0,0,3,1,3,0,2,11,10,15,7,0,2,1,8,8,0,0,3,2,3,0,2,11,10,15,7,0,2,1,8,8,0,0,3,2,3,0,2,11,10,15,7,0,2,1,8,8,0,0,3,2,3,0,2,11,10,15,7,0,2,14,15,8,15,13,4,1,0,4,8,1,0,12,8,11,4,14,15,8,15,13,4,1,0,4,8,1,0,12,8,11,4,14,15,6,15,13,4,1,0,4,8,1,0,12,8,11,4) time=0
# ACC

ACC_START = 0xF1
ACC_F9    = 0xF9
ACC_F8    = 0xF8


class FS680_ACC:
    """Kawai FS680 ACC format
   
    There are five user rhythms which can
    be sent by the sysex command ACC"""
    class Header:
        """ACC header"""
        def __init__(self, raw_bytes):
            """Init"""
            self._raw = raw_bytes

            logger.debug(f"Header: {self.as_hex()}")  
           
        def as_hex(self):
            """Convert to ascii hex"""
            return " ".join(f"{x:02X}" for x in self._raw)
       
    class Sequence:
        """Sequence data"""
        class Note:
            """Note class"""
            def __init__(self, raw_bytes):
                """Init"""
                self._raw = raw_bytes
                try:
                    self.pitch,self.timestamp,self.duration,self.code = raw_bytes
                   
                    self.velocity_idx = (self.code&0xF0) >> 4
                    self.instrument_idx = self.code&0x0F
                   
                    logger.debug(f"Note: {self.to_string()}")
                except:
                    raise
               
            def to_string(self):
                """To string"""
                return f"Instrument: {self.instrument_idx} Pitch {self.pitch} (0x{self.pitch:02X})"
               
               
               
        def __init__(self, raw_bytes):
            """Init"""
            self._raw = raw_bytes
            self._section = []
           
            self._parse()
       
        def _parse_section(self, raw_bytes, section_idx):
            """Parse a section until the next section separator"""
            idx = 0
            section = []
            sections = []
            next_section = False
            section_done = False
            num_of_bytes = len(raw_bytes)
            logger.info(f"Section {section_idx}: Parsing {num_of_bytes} bytes")
            hex_str = " ".join([f"{x:02X}" for x in raw_bytes[:20]])
            logger.debug(f"Next bytes: {hex_str} ...")
            while(True):
                x=raw_bytes[idx]
                if x == ACC_START:
                    # Start of new section
                    idx+=1
                    subcmd = raw_bytes[idx]
                    logger.debug(f"Start at {idx}, subcmd {subcmd:02X}")
                    idx+=1
                    if idx>=num_of_bytes:
                        logger.debug("End of ACC")
                        section_done = True
                        break
                    data1 = raw_bytes[idx]
                    if subcmd == 0x60 and data1 in [0x04]:
                        idx+=1
                        data2 = raw_bytes[idx]
                        logger.debug(f"Special case: F1 60 and {data1:02X} {data2:02X}")
                        idx+=1
                    next_section = True
                    break
                elif x == ACC_F9:
                    idx+=1
                    subcmd = raw_bytes[idx]
                    logger.debug(f"0xF9 at {idx}, subcmd {subcmd:02X}")
                    idx+=1
                elif x == ACC_F8:
                    idx+=1
                    timestamp = raw_bytes[idx]
                    idx+=3
                    # The next two bytes are unknown
                elif section_idx == 10:
                    logger.debug("Section 10")
                    idx+=4*16+6
                    hex_str = " ".join([f"{x:02X}" for x in raw_bytes[idx:idx+20]])
                    logger.debug(f"Next bytes: {hex_str} ...")
                else:
                    note = self.Note(raw_bytes[idx:idx+4])
                    section.append(note)
                    idx += 4
                    hex_str = " ".join([f"{x:02X}" for x in raw_bytes[idx:idx+20]])
                    logger.debug(f"Next bytes: {hex_str} ...")


                if idx >= num_of_bytes:
                    logger.debug(f"End at {idx}")
                    break
            
            if section_done:
                return [section]
                
            if not next_section:
                logger.error("No section separator found")
            else:
                pass

            return [section] + self._parse_section(raw_bytes[idx:], section_idx+1)
              
            
        def _parse(self):
            """Parse sequence data"""
            sections=self._parse_section(raw_bytes=self._raw,
                                         section_idx=0)
            logger.debug("Done with parsing")


    def __init__(self):
        """Init"""
        self._raw = None
        self._header = None
        self._sequence = None
        
    def from_bytes(self, bytes_in):
        """Take the given list of bytes to fill the internal
        structure"""
        self._raw = bytes_in
        
        # Header format:
        # 00 00 02 00
        # 36 00 50 01
        # 1A 39 18 00
        # 00 00 00 00

        self._header = self.Header(self._raw[0:16])
        self._sequence = self.Sequence(self._raw[16:])
        
        
    
class FS680_sysex:
    """Kawai FS680 sysex message
    F0    Sysex start
    40    Manufacturer ID: Kawai
    """
    def __init__(self, name):
        """Init"""
        self.name = name
        self.syx_data = None

    def from_syx_file(self, filename):
        """Read syx file"""
        messages=mido.read_syx_file(filename)
        if len(messages) != 1:
            logger.error("Number of messages in syx file is not 1")
            raise
        self.syx_data=messages[0].data
        
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
        
    def _pretty_print(self, data, max_col=16):
        """Pretty print the given data"""
        col = 0
        pretty_string = ""
        for data_byte in data:
            pretty_string += f"{data_byte:02X} "
            col += 1
            if col >= max_col:
                pretty_string = pretty_string[:-1] + "\n"
                col = 0
        return pretty_string
     
            
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
        pretty_string = self._pretty_print(self.syx_data, max_col=16)
        return pretty_string
    
    def parse_header(self):
        """Parse the header"""
        # Name, Number of bytes
        header_mapping = [["Kawai ID"      ,  1],
                   ["Channel?"      , 1],
                   ["Function no.?"  , 1],
                   ["Device ID?", 1],
                   ["Model ID?", 1],
                   ["Command", 1], ]
        
        header = []
        idx=0
        for name, n_bytes in header_mapping:
            if n_bytes == 2:
                header += [name, self.syx_data[idx+1]*0x10 + self.syx_data[idx]]
            else:
                header += [name, self.syx_data[idx]]
            idx += n_bytes
            
        return header
           
    
    def get_registers(self):
        """The registration format"""
        offset = 6
        
        # Name, number of bytes, offset
        register_mapping = [
                ["Lower mode"    , 2,   0],  # 0: Normal 1: Auto 2: Drum
                ["Position?"     , 2,   1],
                ["U2"            , 2,   1],
                ["Volume Sound 1", 2,   0],
                ["Volume Sound 2", 2,   0],
                ["Volume Chord"  , 2,   0],
                ["Volume Bass"   , 2,   0],
                ["Volume Rhythm" , 2,   0],
                ["Sound 1"       , 2,   1],
                ["Sound 2"       , 2,   1],
                ["U3"            , 2,   1],
                ["U4"            , 2,   1],
                ["Rhythm"        , 2,   1],
                ["Detune"        , 2,   0],
                ["Tempo"         , 2,   1],  # 0x14 (20) => 100, 0x0A (10) => 80
                ["U5"            , 2,   1],

# Tempo
# 3    SyC  (0x7F)
# 4     216 (0x3F)

# Position: 1: 1, 2: 2, 3:1+2

                
                ]
        registers = []
        idx = offset
        for _ in range(20):
            register = []
            for name, n_bytes, offset in register_mapping:
                if n_bytes == 2:
                    register += [[name, self.syx_data[idx+1]*0x10 + self.syx_data[idx], offset]]
                else:
                    register += [[name, self.syx_data[idx], offset]]
                idx += n_bytes
            registers.append(register)
        
        for register_idx, register in enumerate(registers):
            for name, value, offset in register:
                logger.info(f"{register_idx+1:02} {name:7s}: {value+offset:02}  ({value:02}, {value:02X})")

        
        return registers  
    
    def get_accs(self):
        """The acc format
Header with no Chord:
     40 00 21 05 03 03 00 00 00 00 0A 08 00 00 06 0F 01 00 00 01 03 00 09 01 09 03 08 01 00 00 00 00
     
     
Header with only one note,C (0x3C), with sound 26 (ACC_pretty_3)
     40 00 21 05 03 03 00 00 00 00 0A 08 00 00 0A 0D 01 00 04 0F 02 00 09 01 09 03 08 01 00 00 00 00   
                                                ^  ^        ^  ^  ^
        
Header with only one note,C (0x3C) with sound 27 (ACC_pretty_4)
     40 00 21 05 03 03 00 00 00 00 0A 08 00 00 06 0D 01 00 00 0F 02 00 0A 01 09 03 08 01 00 00 00 00
                                                ^           ^           ^ Sound?
                
Header full with only one note,C (0x3C), with sound 27 (ACC_pretty_5)
     40 00 21 05 03 03 00 00 00 00 0A 08 00 00 0E 06 02 00 08 08 03 00 0A 01 09 03 08 01 00 00 00 00
                                                ^  ^  ^     ^  ^  ^ 
                
Header full with only one note,C# (0x3D), velocity 15 (0x7F?), with sound 27 (ACC_pretty_6)
     40 00 21 05 03 03 00 00 00 00 0A 08 00 00 02 08 02 00 0C 09 03 00 0A 01 09 03 08 01 00 00 00 00
                                                ^  ^        ^  
0D 03 09 03 02 00 0A 0F 0A 02 0C 03 02 00 0C 06


Header full with only one note,C# (0x3D), velocity 14 (0x73?), with sound 27 (ACC_pretty_7)
     40 00 21 05 03 03 00 00 00 00 0A 08 00 00 0A 07 02 00 04 09 03 00 0A 01 09 03 08 01 00 00 00 00
                                                |  |        |
        
Three notes plus three notes: C3# C# C#..... C# C# C#.... 
C# (0x3D), velocity 14 (0x73?), with sound 27 (ACC_pretty_8)
0D 03 08 01 0E 00 0A 0F 04 02 08 01 0B 00 0C 0F 06 02 08 01 07 02 04 0D 00 03 08 01 03 00 0C 09 00 03 08 01 06 01 03 0D 0A 02 0E 01 02 00Note
0D 03 09 01 0D 00 0A 0F
0D 03 02 03 09 02 0A 0F 
----- -----
Note  Time1 Time2 Vel

3D 18 0E FA
3D 30 28 FA
3D 01 0D FA     
3D 19 0D FA    
3D 32 29 FA   
3D 60 0D FA

9: Velocity 10
N  T  L  VC        Note, Time, Length, Velocity, Channel
3D 01 0A AA
3D 18 0C AA
3D 30 25 AA
3D 01 0C AA
3D 19 0C AA
3D 31 26 AA

10: Just chord notes

Tags?
F1 60    Start?
F6
F9 60
F9 5A

11: Some drums

F1 60 
25 01 07 FC    Drum
3D 01 0A AA    Chord
3D 18 0C AA    Chord 
26 2F 08 FC    Drum
3D 30 25 AA    Chord 
25 60 07 FC    Drum
F9 60 
3D 01 0C AA    Chord
26 18 06 FC    Drum
3D 19 0C AA    Chord 
26 2F 07 FC 
3D 31 26 AA    Chord
F1 60

12: And one bass note
F1 60 
30 01 0B FB    Bass
25 01 07 FC 
3D 01 0A AA 
3D 18 0C AA 
26 2F 08 FC 
3D 30 25 AA 
25 60 07 FC 
F9 60
3D 01 0C AA
26 18 06 FC
3D 19 0C AA
26 2F 07 FC
3D 31 26 AA
F1 60

13: Intro gone
14: All gone. Added one single note in each section



        """
        offset = 6
        
        # Name, number of bytes, offset
        
        
        
        LENGTH_OF_ONE_ACC = 1264 # [bytes]
        
        all_nibbles = self.syx_data[offset:]
        all_bytes = []
        
        for byte_idx in range(len(all_nibbles)//2):
            nibble_idx = byte_idx*2
            u08 = all_nibbles[nibble_idx+1]*0x10 + all_nibbles[nibble_idx]
            all_bytes.append(u08)
            
        logger.debug(f"Length of all bytes: {len(all_bytes)}")
        
        with open("dumps/sysex_hex2.txt", "wb") as f1:
            f1.write(self._pretty_print(all_bytes, max_col=16).encode("UTF8"))
        
        accs = []
        for acc_idx in range(5):
            from_idx = acc_idx*LENGTH_OF_ONE_ACC
            to_idx = from_idx+LENGTH_OF_ONE_ACC

            logger.info(f"ACC {acc_idx}")
            acc = FS680_ACC()
            acc.from_bytes(all_bytes[from_idx:to_idx])
            accs.append(acc)
  
        
        # for acc_idx, acc in enumerate(accs):
        #     for name, value, offset in acc:
        #         logger.info(f"{acc_idx+1:02} {name:7s}: {value+offset:02}  ({value:02}, {value:02X})")

        # for acc_idx, acc in enumerate(acc4s):
        #     for data in acc:
        #
        #         str_data = " ".join(f"{x:02X}" for x in data['data'])
        #         logger.info(f"{data['name']} {str_data}")
        #    logger.info(f"{acc_idx+1:02} {name:7s}: {value+offset:02}  ({value:02}, {value:02X})")
        
        return accs  
        
    def pretty_print_registers(self):
        """Pretty print registers"""
        registers_str = ""
        for register_idx, register in enumerate(self.get_registers()):
            for name, value, offset in register:
                registers_str += f"{register_idx+1:02} {name:7s}: {value+offset:02}  ({value:02}, {value:02X})\n"
                
        return registers_str
    
    def pretty_print_accs(self):
        """Pretty print acc"""
        accs_str = ""
        # for acc_idx, acc in enumerate(self.get_accs()):
        #     for name, value, offset in acc:
        #         accs_str += f"{acc_idx+1:02} {name:7s}: {value+offset:02}  ({value:02}, {value:02X})\n"
        #

        col = 0
        max_col = 4
        accs = self.get_accs()
        for acc in accs:
            accs_str += f"{element['data']:02X} "
            col += 1
            if col >= max_col:
                accs_str = accs_str[:-1] + "\n"
                col = 0
                
        return accs_str

         
        
    def create_checksum(self, start_idx):
        """Create checksum"""
        sum=0
        for data_byte in self.syx_data[start_idx:-1]:
            sum = (sum+data_byte)&0x7F
        sum = (~sum)+1
        logger.info(f"Sum with idx {start_idx}: {sum}")
            
        
    def investigate(self):
        """Investigate data
        At startup:
        
        
        
        
        
        """
        logger.info(f"Name: {self.name} Len: {len(self.syx_data):7} Data: {self.syx_data[:10]}")
        logger.info(f"Data: {self.syx_data[:10]}")
        logger.info(f"Header: {self.parse_header()}")
        #self.get_registers()
        self.get_accs()
#        self.dump_to_file(filename = self.name + "_pretty")
        # for idx in range(20):
        #     self.create_checksum(start_idx = idx)

    def dump_to_file(self, filename):
        """Dump to file"""
        with open(filename, 'w') as f1:
            f1.write(self.pretty_print())

        # with open(filename+"_2", 'w') as f1:
        #     f1.write(self.pretty_print_registers())
        
        with open(filename+"_u08", 'w') as f1:
            f1.write(self.pretty_print_accs())
    

class SyxTester:
    """Class for testing sysex messages"""
    def __init__(self, input_port, output_port):
        """Init"""
        self.input_port = input_port
        self.output_port = output_port
               
    def generate_random_message(self, max_len):
        """Generate random message"""
        msg_len = randrange(1, max_len)
        msg = []
        for _ in range(msg_len):
            msg.append(randrange(0x7F))
        
#        logger.info(msg)
        return msg
        
    def get_all(self):
        """Get all messages"""
        while True:
            data_in = self.input_port.receive()
            logger.debug(f"Type: {data_in.type} Data: {data_in.hex(' ')}")
                         
    def test(self):
        """Test sysex messages"""

        device_id = 0x00
        old_msg = mido.Message(type="sysex", data = [])
        
        msg_list = []
        while True:
            # Device inquiry
#             F0 7E <device ID> 06 01 F7
# F0 7E <device ID> Universal System Exclusive Non-real time header
# 06 General Information (sub-ID#1)
# 01 Identity Request (sub-ID#2)
# F7 EOX
# Sysex sent from FS680:
# Sound 1:            40 00 10 05 03 00 00
# Sound 2:            40 00 10 05 03 00 01
# Sound 1+2 (dual):   40 00 10 05 03 00 40
# Detune 0:           40 00 10 05 03 00 40
# Detune 7:           40 00 10 05 03 00 47
# Duet on:            40 00 10 05 03 01 7F
# Duet off:           40 00 10 05 03 01 00
# Sustain on:         40 00 10 05 03 02 7F
# Sustain off:        40 00 10 05 03 02 00
# OFA on:             40 00 10 05 03 03 7F
# OFA off:            40 00 10 05 03 03 00
# Lower mode Auto:    40 00 10 05 03 04 01
# Lower mode normal:  40 00 10 05 03 04 00
# Lower mode drum:    40 00 10 05 03 04 02
# Tempo 48:           40 00 10 05 03 05 00
# Tempo 52:           40 00 10 05 03 05 01
# Tempo 216:          40 00 10 05 03 05 3F
# Tempo SyC:          40 00 10 05 03 05 7F
# Stereo Chorus on: CC 93=127
# Stereo Chorus on: CC 93=0
#
# Melody volume: Channel 0,1: CC: 7 Value: 0-127
# Chord volume:  Channel: 2 CC: 7 Value: 0-127
# Bass volume:   Channel: 3 CC: 7 Value: 0-127
# Rhythm volume: Channel: 9 CC: 7 Value: 0-127
#
# Recorder play 1:  40 00 10 05 03 04 01
#                   40 00 10 05 03 03 7F
#                   40 00 10 05 03 00 00
# Recorder play 2:  40 00 10 05 03 04 01
#                   40 00 10 05 03 00 00
#                   
# Recorder play 3:  40 00 10 05 03 04 01
#                   40 00 10 05 03 03 7F
#                   40 00 10 05 03 00 00
#
# At startup:         40 00 10 05 03 00 00    Sound 1
#                     40 00 10 05 03 02 7F    Sustain on

# Crash here:

# 2022-01-21 23:44:28,276 - root - INFO - 40
# 2022-01-21 23:44:28,276 - root - INFO - 56 28 2E 66 44 7C 7C
# 2022-01-21 23:44:28,276 - root - INFO - 2C 2F 5E 45 0C 05 09 43 62

# for msg in msg_list:
#     data_str = " ".join(f"{x:02X}" for x in msg.data)
#     logger.info(data_str)

            data = self.generate_random_message(10)
            msg = mido.Message(type="sysex", data = data)
            self.output_port.send(msg)
            msg_list.append(msg)
            time.sleep(0.1)
            received = self.input_port.receive(block=False)
            if received:
                logger.info(f"Received {received.type} with {msg.data} (old {msg.data})")
                if received.type == "sysex":
                    received_str = " ".join([f"{x:02X}" for x in received.data])
                    logger.info(f"Received sysex: {received_str}")
                elif received.type == "control_change":
                    logger.info(f"Received Channel: {received.channel} CC: {received.control} Value: {received.value}")
                    
            
            device_id +=1
            if device_id >= 0x7F:
                device_id = 0
                
            old_msg = msg

    
    
def run():
    base_path = "dumps"
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
    output_name = "M Audio Audiophile 24/96:M Audio Audiophile 24/96 MIDI 24:0"
    
#    input_port = mido.open_input(input_name)
    
 #   output_port = mido.open_output(output_name)
    
    # syx_tester = SyxTester(input_port=input_port, output_port=output_port)
    # syx_tester.get_all()
    

    sysex_dict = {}
    for key in ["ACC"]: #["REG", "SYN", "ACC", "OFA"]:
        logger.info(f"Receive {key}...")
        sysex_dict[key] = FS680_sysex(name = key)
        #sysex_dict[key].from_message(message=input_port.receive())

        sysex_dict[key].from_syx_file(filename=base_path + "/" + "out3.syx")
  #      sysex_dict[key].from_hex_file(filename=base_path + "/" + key+"_pretty_14")
        
        sysex_dict[key].dump_to_file(filename=base_path + "/" + key + "_pretty")
        
        
        
      #  msg = mido.Message('sysex', data=sysex_dict[key].syx_data)
        
     #   output_port.send(msg)
        
        
    for _,syx in sysex_dict.items():
        syx.investigate()
        
    logger.info("Done")

    
if __name__=="__main__":
    run()


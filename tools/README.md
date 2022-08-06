# Tools

## read_ch8.py
```
Usage: python read_ch8.py [ch8 filename]
```
Dumps contents of ch8 file two bytes per line.
```
$ python read_ch8.py programs/keypress_test.ch8
0x200: 00 E0
0x202: 12 08
0x204: F0 0A
0x206: 12 04
0x208: FF 0A
[...]
0x2e2: 80 F0
0x2e4: 80 80
0x2e6 - end of file -
```

## write_ch8.py
```
Usage: python write_ch8.py [input filename] [-debug]
```
Converts machine code written in text to binary. If given machine code (2 bytes per line in hex format) it will generate its binary counterpart. In addition, it provides the following convenience functionalities to assist in programming.
### Comments
Anything after a semicolon (`;`) is ignored.
```
1200 ; jump to 0x200
```
### Absolute addressing
Any code following a hex address followed by a colon (`0xNNN:`) will start from that address.
```
0x200:
  1200 ; jump to self
0x206:
  00e0 ; clear screen
```
Binary dump of code above (`test1.txt`):
```
$ python write_ch8.py test1.txt
$ python read_ch8.py test1.ch8
0x200: 12 00
0x202: 00 00
0x204: 00 00
0x206: 00 E0
0x208 - end of file -
```
### Labels
Labels start with a dot (`.`) and end with a colon (`:`) and represent the address of the location in which they are located. They can be referred to in code, taking the place of a memory location.
```
0x204: ; absolute address reference (see above)
.loop: ; the loop label represents the memory location 0x204
  00e0
  1.loop ; converted to 1204
```
Binary dump of the code above (`test2.txt`):
```
$ python write_ch8.py test2.txt
$ python read_ch8.py test2.ch8
0x200: 00 00
0x202: 00 00
0x204: 00 E0
0x206: 12 04
0x208 - end of file -
```
### Relative addressing
Referencing `+[hex]` or `-[hex]` values when designating memory addresses will be replaced with dynamically calculated relative addresses.
```
0x200:
  1+4  ; converted to 1204 (0x200 + 0x4)
  00e0
  1-2  ; converted to 1202 (0x200 - 0x2)
```
Binary dump of the code above (`test3.txt`):
```
$ python write_ch8.py test3.txt
$ python read_ch8.py test3.ch8
0x200: 12 04
0x202: 00 E0
0x204: 12 02
0x206 - end of file -
```
### Designate single hex byte per line
Start line with single quote (`'`). May be useful when writing sprite data:
```
0x200:
.hex0:
  'f0
  '90
  '90
  '90
  'f0
```
Binary dump of the code above (`test4.txt`):
```
$ python write_ch8.py test4.txt
$ python read_ch8.py test4.ch8
0x200: F0 90
0x202: 90 90
0x204: F0 --
0x206 - end of file -
```

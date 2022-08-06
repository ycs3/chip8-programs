# CHIP-8 Programs

Writing programs in the CHIP-8 language, and some tools to aid in programming.

## Programs
Each program has a readable machine code (`.txt`) and corresponding binary (`.ch8`) file.

Name  | Description
------------- | -------------
programs/keypress_test | writes character to display corresponding to keypress


## Tools
`.txt` files can be converted to `.ch8` files using the `tools/write_ch8.py` tool.

Name  | Description
------------- | -------------
tools/read_ch8.py | dumps contents of .ch8 file
tools/write_ch8.py | assists with the writing of CHIP-8 language by enabling relative addressing and labels

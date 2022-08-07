# CHIP-8 Programs

Writing programs in the CHIP-8 language, and some tools to aid in programming.

## Programs (in /programs)
Each program has a readable machine code (`.txt`) and corresponding binary (`.ch8`) file.

Name  | Description
------------- | -------------
my_first_program.ch8 | writes example text to screen
move_paddle.ch8 | move paddle up and down using 1 and 4 keys
keypress_test.ch8 | writes character to display corresponding to keypress
solo_pong_v1.ch8 | basic 1-player pong game (use 1/4 key to move paddle)

## Tools (in /tools)
`.txt` files can be converted to `.ch8` files using the `tools/write_ch8.py` tool.

Name  | Description
------------- | -------------
read_ch8.py | dumps contents of .ch8 file
write_ch8.py | assists with the writing of CHIP-8 language by enabling relative addressing and labels

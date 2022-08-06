import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} [ch8 filename]")
        exit()
    filename = sys.argv[1]
    with open(filename, "rb") as fp:
        contents = fp.read()

    for i in range(0, len(contents), 2):
        print(f"0x{0x200+i:03x}: {contents[i]:02X} {contents[i+1]:02X}")
    print(f"0x{0x200+i+2:03x} - end of file -")


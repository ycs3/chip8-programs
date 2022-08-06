import sys
import os

def generate_machine_code(lines, debug=False):
    # first pass: read refs
    addr = 0x200
    refs = {}
    for line in lines:
        if line.endswith(":"): # define address
            if line.startswith("."): # reference with label
                label = line[1:-1]
                refs[label] = addr
                if debug:
                    print(f"* 0x{addr:03x} {label}")
            else: # absolute address
                addr = int(line[:-1], 16)
        elif line.startswith("'"): # 1-byte hex data
            addr += 1
        else: # 2-byte instruction
            addr += 2

    # second pass: write to rom
    addr = 0x200
    mem = [0] * 0x1000
    for line in lines:
        if line.endswith(":"): # define address
            if not line.startswith("."): # absolute address
                addr = int(line[:-1], 16)
        elif line.startswith("'"): # 1-byte hex data
            v = int(line[1:], 16)
            mem[addr] = v
            if debug:
                print(f"  0x{addr:03x} {v:02x}")
            addr += 1
        else: # 2-byte instruction
            if "+" in line: # relative reference
                cmd, rel = line.split("+")
                s = f"{cmd}{addr + int(rel, 16):03x}"
            elif "-" in line: # relative reference
                cmd, rel = line.split("-")
                s = f"{cmd}{addr - int(rel, 16):03x}"
            elif "." in line:
                cmd, label = line.split(".")
                s = f"{cmd}{refs[label]:03x}"
            else:
                s = line
            v0, v1 = int(s[:2], 16), int(s[2:], 16)
            mem[addr], mem[addr+1] = v0, v1
            if debug:
                print(f"  0x{addr:03x} {v0:02x}{v1:02x}")
            addr += 2

    # identify max addr
    for max_addr in range(0xfff, -1, -1):
        if mem[max_addr] != 0:
            break
    if debug:
        print(f"max addr: 0x{max_addr:03x}")

    ret = bytes(mem[0x200:max_addr+1])
    return ret

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} [input filename] [-debug]")
        exit()

    debug = False
    if len(sys.argv) > 2:
        if sys.argv[2] == "-debug":
            debug = True

    input_file = sys.argv[1]
    output_file = os.path.splitext(input_file)[0] + ".ch8"

    print(f"reading {input_file}\nwriting to {output_file}\n[debug={debug}]")
    
    with open(input_file, "r") as fp:
        lines = [
            l for l in
                [k.split(";", 1)[0].strip() for k in fp.readlines()]
                if len(l) > 0
        ]

    ret = generate_machine_code(lines, debug=debug)

    with open(output_file, "wb") as fp:
        fp.write(ret)

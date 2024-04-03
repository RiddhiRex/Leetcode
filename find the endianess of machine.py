import sys

def is_little_endian():
    return sys.byteorder == 'little'

def is_big_endian():
    return sys.byteorder == 'big'

# Example usage:
if is_little_endian():
    print("The machine is little-endian.")
elif is_big_endian():
    print("The machine is big-endian.")
else:
    print("Unable to determine the endianness of the machine.")

from pwn import *

def execute(input_array: bytes, char_count: int) -> bytes:
    import sys
    
    if input_array is None or char_count == 0:
        sys.exit(1)
    
    double_char_count = char_count * 2
    aligned_buffer = bytearray(double_char_count + 1)  # +1 for 0xc3
    
    incremented_non_checked = 0
    
    for i in range(double_char_count):
        # val_high = 0, val_low = i
        # high_bits = 0
        # condition: ((i & 3) > 1)
        if (i & 3) > 1:
            aligned_buffer[i] = 0x90  # NOP
        else:
            if incremented_non_checked < char_count:
                aligned_buffer[i] = input_array[incremented_non_checked]
                incremented_non_checked += 1
            else:
                aligned_buffer[i] = 0x00  # pad with zeros if input exhausted
    
    aligned_buffer[double_char_count] = 0xc3  # RET
    
    return bytes(aligned_buffer)

def main():
    

    # Output final shellcode
    print(f"Length: {len(shellcode)} bytes")
    print(enhex(shellcode))



if __name__ == "__main__":
    main()

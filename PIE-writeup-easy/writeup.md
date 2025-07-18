# PIE TIME - Binary Exploitation Writeup

## Challenge Info
**Category:** Binary Exploitation  
**Difficulty:** Easy  
**Flag:** `picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_a267144a}`

## Analysis

Running the binary, we see it gives us the address of `main()` and asks for input. Looking at the source code (or disassembly), we find the vulnerability:

```c
void (*foo)(void) = (void (*)())val;
foo();
```

This creates a function pointer from our input and calls it!

## Solution

1. **Find the target:** There's a `win()` function in the binary that we need to call
2. **Calculate the address:** Using a disassembler, we find that `win()` is exactly `0x96` bytes before `main()`
3. **Do the math:** `win_address = main_address - 0x96`
4. **Exploit:** Input the calculated address to redirect execution

## Exploitation Steps

```bash
$ ./pie_time
# Binary shows: "main is at 0x[ADDRESS]"
# Calculate: win_address = ADDRESS - 0x96
# Input the win_address when prompted
# Get flag!
```

## Key Concept

This challenge demonstrates basic function pointer manipulation in a PIE binary. Even though addresses are randomized, we can use the given `main()` address as a reference point to calculate where `win()` is located. We basically have to use offsets now to try to find where certain functions we need are!

**Flag:** `picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_a267144a}`
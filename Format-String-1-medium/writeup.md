# Format-String Leak Writeup

**Flag:** `picoCTF{4n1m41_57y13_4x4_f14g_9135fd4e}`

## Summary

The binary reads user input and prints it back using `printf(buf)` without format specifiers, causing a format string vulnerability. We can leak stack contents by using `%p` specifiers to print pointer values from the stack.

## Exploit Strategy

1. Send a payload consisting of repeated `%p:` specifiers to leak as many stack values as needed.
2. The program prints the leaked addresses as hex pointers separated by colons.
3. Parse the leaked hex addresses, convert each from little-endian 64-bit hex into bytes.
4. Concatenate the bytes and decode as UTF-8 to extract readable strings that include secret values and ultimately the flag.

## Key Points

* Format string vulnerability without format specifiers allows leaking stack memory with `%p`.
* Leaked stack values are 64-bit pointers printed as hex.
* Convert hex leaks to bytes respecting little-endian order.
* Decode bytes as UTF-8 to recover hidden strings on the stack, including the flag.
* No overwrites or code execution needed — pure information leak.

## Technical Details

- Use payload: `%p:` repeated ~100 times to leak a large chunk of the stack.
- Read output after prompt, split on `:` to isolate pointers.
- Convert each `0x`-prefixed string to an integer, then to bytes in little-endian.
- Join and decode bytes to extract printable ASCII.

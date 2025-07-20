# PIE-TIME-2 Writeup

**Flag:** *(output from running the exploit)*

## Solution

The binary reads a name and prints it using `printf(buffer)` without format specifiers, giving a format string vulnerability.

I tested different `%p` specifiers and found `%19$p` reliably leaks a return address on the stack inside the binary’s memory space.

The leaked address points inside `main()` right after where `call_functions()` is located. Using GDB, I calculated the offset between this address and the start of the `win()` function as `0xd7` bytes.

The program then prompts for an address to jump to. I sent the calculated `win()` address by subtracting `0xd7` from the leaked return address.

Because the binary prints both prompts together, I sent the jump address immediately after receiving the leak.

Calling the `win()` function prints the flag.

## Key Points

* Used format string `%19$p` to leak PIE base pointer
* Calculated offset `0xd7` from leak to `win()`
* Sent `win()` address to function pointer call to get code execution and flag
* Prompts printed together, so no delay needed between inputs

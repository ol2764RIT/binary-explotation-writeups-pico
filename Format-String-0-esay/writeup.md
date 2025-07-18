# Format String 0 - CTF Writeup

## Challenge Info
**Category:** Binary Exploitation  
**Difficulty:** Easy  
**Flag:** `picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_c8362f05}`

## Analysis

This challenge involves a burger shop program with two customers. Looking at the code, we can identify several key components:

1. **Signal Handler**: A `sigsegv_handler` that prints the flag when a segfault occurs
2. **Buffer Overflow**: `scanf("%s", choice1)` reads into a 32-byte buffer without bounds checking
3. **Menu Check**: `on_menu()` uses `strcmp()` to validate input against menu items
4. **Format String Vulnerability**: `printf(choice1)` directly prints user input

## The Vulnerability Chain

The exploit works through a chain of vulnerabilities:

1. **Buffer Overflow**: Fill the `choice1` buffer completely with A's (no null terminator)
2. **strcmp() Overread**: Without null termination, `strcmp()` keeps reading past the buffer
3. **Menu Check Bypass**: The overread string (A's + flag) doesn't match any menu item
4. **Format String Trigger**: `printf(choice1)` causes a segfault when parsing A's as format specifiers
5. **Flag Retrieval**: Segfault triggers the signal handler which prints the flag

## Solution

Simply input enough A's to fill the 32-byte buffer without a null terminator:

```bash
$ ./vuln
Welcome to our newly-opened burger place Pico 'n Patty!
Can you help the picky customers find their favorite burger?
Here comes the first customer Patrick who wants a giant bite.
Please choose from the following burgers: Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe
Enter your recommendation: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
There is no such burger yet!

picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_c8362f05}
```

## Key Concepts

- **Buffer Overflow**: Writing past buffer boundaries
- **Null Termination**: How C strings are terminated and what happens without it
- **strcmp() Behavior**: How string comparison functions handle unterminated strings
- **Format String Vulnerabilities**: Direct printf() calls with user input
- **Signal Handlers**: Using SIGSEGV handlers as an exploitation technique

**Flag:** `picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_c8362f05}`
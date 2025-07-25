# Buffer-Overflow-1 Writeup

**Flag:** `picoCTF{you_r34lly_jU5t_h4d_t0_5end_it29be77d6}`

## Summary

This is a classic buffer overflow challenge. The goal is to overwrite the return address of the vulnerable function (`vuln()`) with the address of the `win()` function, which prints the flag.

## Vulnerability

In the `vuln()` function:

```c
char buf[BUFSIZE];    // BUFSIZE = 32
gets(buf);            // UNSAFE! No bounds checking
````

You're allowed to overflow the stack buffer and **overwrite the return address**.

The program even hints at where you’ll return to:

```c
printf("... Jumping to 0x%x\n", get_return_address());
```

## Exploitation Strategy

The buffer is 32 bytes, and the return address is typically **4 bytes after** 12 bytes of saved registers / alignment padding on 32-bit systems, for a total of **44 bytes offset** to the return address.

We overwrite that with the address of the `win()` function:

```python
payload = b"X" * 44 + p32(0x80491f6)  # Address of win()
```

## Final Notes

* This is standard **32-bit stack overflow**, with **non-randomized** addresses (no PIE).
* There is no stack canary, NX doesn’t matter because we’re reusing code.
* `gets()` is again the culprit: always unsafe.

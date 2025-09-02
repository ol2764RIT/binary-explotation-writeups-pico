# Flag-Leak-Medium Writeup

**Flag:** `picoCTF{L34k1ng_Fl4g_0ff_St4ck_rand}`

---

## Summary

This challenge leverages a **format string vulnerability** on a stack-stored secret. The binary prints user input unsafely using `printf(story)`, which allows us to leak arbitrary stack contents.

Rather than manually guessing offsets and `%p` values, we can **dynamically iterate over likely stack positions** to reconstruct the flag. The exploit script automates this process.

---

## Vulnerability

Relevant snippet:

```c
void vuln(){
   char flag[BUFSIZE];
   char story[128];

   readflag(flag, FLAGSIZE); // reads flag into stack
   printf("Tell me a story and then I'll tell you one >> ");
   scanf("%127s", story);
   printf("Here's a story - \n");
   printf(story);  // format string vulnerability
   printf("\n");
}
```

Key points:

* `flag` buffer resides on the stack.
* `story` is printed **directly with printf**, letting us control format specifiers.
* `%p` can leak arbitrary stack addresses; `%s` can leak strings stored on the stack.

---

## Exploitation Strategy

1. **Dynamic offset discovery**

   * Instead of manually guessing, the script loops through a range of stack positions:

     ```python
     for num in range(36, 50):
         payload_1 += f"%{num}$p".encode()
     ```
   * Each `%num$p` prints a pointer from the stack.

2. **Extract flag parts**

   * Output is hex-encoded pointers (e.g., `0x...0x...`).
   * Split the string, convert from hex to bytes, then decode as ASCII.
   * Some parts may be reversed due to stack layout; the exploit corrects this with `[::-1]`.

3. **Reconstruct flag**

   * Concatenate all decoded pieces to get the full flag:

     ```
     picoCTF{L34k1ng_Fl4g_0ff_St4ck_rand}
     ```

---

## Exploit Script Overview

* Uses `pwntools` for connection handling.
* Supports both local and remote execution:

  ```bash
  python3 exploit.py local
  python3 exploit.py remote
  ```
* Dynamically leaks stack contents using format string `%p`.
* Parses, reverses, and decodes hex values to reconstruct the flag.

---

## Final Notes

* **Vulnerability:** format string on stack-stored secret.
* **Automated approach:** iterates over possible stack positions rather than guessing manually.
* **Defense:** always use safe printing: `printf("%s", story)`.
* **Takeaway:** even small buffers read into stack memory can leak secrets when format strings are uncontrolled.

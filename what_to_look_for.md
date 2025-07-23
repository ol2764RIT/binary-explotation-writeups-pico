Exploit Cheat Sheet
1. Format String Vulnerability

    What: `printf(user_input)` without format string sanitization.

    Look for: Direct `printf(buf)` or similar calls.

    Impact:

        Leak memory with %x, %p (stack, libc, or binary addresses).

        Write arbitrary memory with %n.

    Tactics:

        Leak GOT or stack addresses to defeat ASLR.

        Overwrite GOT entry or function pointers to redirect flow.

        Use %[offset]$p to find controlled input offset (%1$p to %40$p).

        Identify address types:

            0x55... → PIE (binary code/data)

            0x56... → Heap

            0x7f... → Libc

            0x7fff... → Stack

        Use known marker input (e.g., AAAABBBB) to find where input lands on the stack.


#### 2. Stack-based Buffer Overflow

* **What:** Overwriting stack memory past buffer boundary.
* **Look for:** `gets()`, `strcpy()`, `sprintf()` without bounds checking.
* **Impact:**

  * Overwrite saved return address or frame pointer.
  * Hijack execution to shellcode or ROP chain.
* **Tactics:**

  * Find buffer size.
  * Calculate offset to return address.
  * Inject payload to control RIP.

#### 3. Heap Exploitation

* **What:** Corrupting heap metadata or use-after-free.
* **Look for:** Dynamic memory use with `malloc()`, `free()`.
* **Impact:**

  * Arbitrary write.
  * Control over future malloc results or function pointers.
* **Tactics:**

  * Overflow chunk size or pointers.
  * Use double free or UAF.

#### 4. Use-After-Free (UAF)

* **What:** Accessing freed memory.
* **Look for:** Reuse of pointers after `free()`.
* **Impact:**

  * Information disclosure or code execution.
* **Tactics:**

  * Control what memory replaces freed chunk.

#### 5. Return-Oriented Programming (ROP)

* **What:** Chain short code snippets ("gadgets") ending in `ret`.
* **Look for:** Non-executable stack (NX) defenses.
* **Impact:**

  * Execute complex logic despite NX.
* **Tactics:**

  * Leak libc addresses.
  * Build gadget chains for system calls.

#### 6. Command Injection / System Hijacking

* **What:** Inject shell commands via input.
* **Look for:** Calls to `system()`, `popen()`, or environment variable usage.
* **Impact:**

  * Remote code execution.
* **Tactics:**

  * Control PATH or environment variables.
  * Escape input parameters.

#### 7. Integer Overflow/Underflow

* **What:** Miscalculation causing buffer overflows or invalid memory use.
* **Look for:** Arithmetic on user inputs without checks.
* **Impact:**

  * Enables overflows or memory corruption.
* **Tactics:**

  * Overflow size fields or counters.

#### 8. Race Conditions / TOCTOU

* **What:** Time-of-check-to-time-of-use bugs.
* **Look for:** Repeated check/use on files or resources.
* **Impact:**

  * Privilege escalation or bypass.
* **Tactics:**

  * Exploit timing to swap files or resources.

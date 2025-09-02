# Guessing Game (Medium)

**Flag:** `picoCTF{r0p_y0u_l1k3_4_hurr1c4n3_476d756f24c7952d}`

---

## Summary

A “guess the number” game gates access to a winner path that later takes oversized input. The binary is statically linked with NX enabled, so shellcode is not allowed. This is a ROP playbook. A **static rand() seed** makes entry predictable: brute-forcing a tiny range of guesses reliably trips the winner branch. From there, an overlong name input smashes the stack, enabling a ROP chain that performs `execve("/bin/sh", 0, 0)`.

---

## Binary Signals (quick recon)

* **i386/amd64 static**: rich gadget surface in the binary itself.
* **NX enabled**: code injection blocked → ROP required.
* **Partial RELRO / No PIE**: predictable addresses in the main module.
* **Game flow**: looped “guess → if correct then winner() → read name”.

---

## Vulnerabilities

1. **Predictable “win gate”**
   The “correct answer” comes from `rand()%BUFSIZE` with a **static seed**. Because the seed never varies, the “right” numbers fall into a tiny, repeatable set. Cycling inputs quickly trips the win condition.

2. **Stack overflow on the winner path**
   The winner prompt reads a “name” into a small stack buffer but allows **significantly more bytes** than the buffer size. That overwrites saved control data and sets up RIP control.

---

## Exploitation Strategy (conceptual)

1. **Reach the winner path**

   * Abuse the static PRNG behavior: try the handful of values produced under the fixed seed until the game prints the “you win” banner.

2. **Stack pivot to ROP**

   * Overflow the name buffer to clobber the saved return address.
   * Keep alignment clean; choose the earliest stable gadgets to reduce brittleness.

3. **Stage data in writable memory**

   * Use a writable section (e.g., **.bss**) as scratch space.
   * Write the string `"/bin/sh\0"` there via a simple move/write gadget pattern.

4. **Load syscall registers**

   * Arrange a minimal register setup for **`execve`**:

     * `RAX = 59` (or `__NR_execve`)
     * `RDI = &"/bin/sh"`
     * `RSI = 0`
     * `RDX = 0`
   * End with a **`syscall`** gadget.

5. **Pop shell → read flag**

   * Successful `execve` spawns a shell; read the challenge flag.

---

## Why it Works

* **NX** only blocks injected code, not **ret-to-gadget** chains already in the binary.
* **Static link** provides a **large, dependable gadget farm** without relying on ASLR-shifting libc.
* A **writable .bss** is ideal for planting benign strings and pointers used as arguments.
* The **PRNG gate** is perfunctory: static seed ⇒ deterministic outputs ⇒ trivial to pass.

---

## Key Takeaways

* **ROP is finicky** until you find **clean, early gadgets**; minimizing gadget count and keeping stack alignment correct saves hours.
* **Writable sections** (like **.bss**) are perfect for staging argument strings and arrays.
* The whole goal boiled down to **`execve("/bin/sh", 0, 0)`**—keep the chain focused on that.
* The bug wasn’t only “overflow”: the **user input overread** on the winner path let the payload flow far enough to **be interpreted as control data**, enabling the chain.
* **Static rand seed** meant only a **tiny brute-force** (e.g., a couple of candidate numbers) to hit the winner branch consistently.
* This took time to stabilize, but once clean gadgets were chosen, the path clicked.

---

## Result

After passing the guess gate and landing the ROP chain, the process executes `/bin/sh` and the flag is retrieved:

**`picoCTF{r0p_y0u_l1k3_4_hurr1c4n3_476d756f24c7952d}`**

---

## Defensive Notes

* Seed PRNGs unpredictably (or avoid them for security-relevant gates).
* Enforce strict bounds on all user-supplied lengths, especially on “celebratory” paths like `win()` functions.
* Don't overread user input! We treated the user input as benign which led us to this.
* Combine **full RELRO** + **PIE** + **ASLR** to erode predictability and reduce gadget reliability.

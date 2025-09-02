# BabyGame01-Medium Writeup

**Flag:** `picoCTF{gamer_m0d3_enabled_fff873ca}`

---

## Summary

This challenge is a 32-bit game where moving normally doesn’t trigger the flag. By moving **out of bounds**, the game performs an **overread into the stack**, leaking a canary-like value, and uses that to update an internal “flag” variable. Once the flag is set via this leak, reaching the exit prints the actual flag.

---

## Vulnerability

* Game is a **32-bit executable** with stack canaries and NX enabled.
* Player position is tracked in memory, likely in a struct or array.
* **Out-of-bounds movement** allows reads **above the allocated buffer**, over the stack, revealing a canary value.
* The leaked value is **added to the internal flag variable**, effectively granting the flag.

Observations:

* Walking normally to the “flag location” does nothing.
* Moving slightly out-of-bounds triggers: `"Player has flag"`.
* Excessive moves (e.g., 99 `s`) cause a segfault due to memory overread.

---

## Exploitation Strategy

1. **Walk OOB to leak stack value**

   * Move left/up beyond normal map boundaries.
   * The game internally reads a stack value (canary) and adds it to the player’s flag variable.
   * This effectively sets the flag without any normal gameplay trigger.

2. **Return to exit normally**

   * Navigate back along valid map coordinates.
   * The internal flag variable is now set.

3. **Reach exit to retrieve flag**

   * Game checks the internal flag variable when you reach the exit.
   * Output prints:

     ```
     picoCTF{gamer_m0d3_enabled_fff873ca}
     ```

---

## Notes

* **Vulnerability type:** out-of-bounds read leading to stack value leak → internal state manipulation.
* **Key insight:** the flag isn’t on the map—it’s determined by **stack-leaked values**.
* **Defense:** proper bounds checking, no memory reads outside valid buffers, and validation of internal game state.


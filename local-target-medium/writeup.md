# local-target Writeup

**Flag:** `picoCTF{l0c4l5_1n_5c0p3_ee58441a}`

## Summary

This challenge features a basic stack buffer overflow. The goal is to change the local variable `int num = 64;` to the value `65` in order to pass a condition and print the flag.

## Vulnerability

The program uses the dangerous `gets()` function, which does **not** perform bounds checking. This allows the user to overflow the `input[16]` buffer and overwrite the adjacent local variable `num`.

```c
char input[16];
int num = 64;
gets(input);  // <-- buffer overflow possible
````

Because of the stack layout, `num` is located **immediately after** `input` in memory.

## Exploit Strategy

1. Overflow the `input` buffer with **16 bytes** to fill it completely.
2. Add **padding** to reach `num` — since `num` is likely aligned on a 4- or 8-byte boundary, total offset to `num` ends up being **24 bytes** on 64-bit systems (due to stack alignment).
3. Overwrite the `num` value with `0x41` (ASCII `'A'` == `65` in decimal) to satisfy the `if(num == 65)` condition.

## Exploit Payload

```python
payload = b"X" * 24 + b"A"  # 'A' = 0x41 = 65
```

This causes `num` to be interpreted as `65`, passing the conditional check and printing the flag.

## Final Notes

* The presence of `gets()` makes this trivially exploitable.
* No stack canaries, PIE, or other mitigations are in place.
* This is a classic example of exploiting local stack variable overflows via simple buffer overrun.

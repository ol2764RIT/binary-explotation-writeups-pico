# heap-2-medium
**Flag:** `hidden`

## Summary
The binary allocates two heap buffers: `input_data` (5 bytes) and `x` (5 bytes). There's a buffer overflow in `write_buffer()` using `scanf("%s", input_data)` with no bounds checking. We can overflow from `input_data` into `x` and overwrite the function pointer used in `check_win()` with the address of `win()`.

## Exploit Strategy
### Step 1: Analyze heap layout
From `init()`:
```c
input_data = malloc(5);
x = malloc(5);
````

Since both are small and allocated back to back, `x` is placed directly after `input_data` in the heap.

Using option 1 to print the heap confirms `x` is located 32 bytes after `input_data`.

### Step 2: Understand the vulnerability

`x` is later dereferenced and called as a function:

```c
((void (*)())*(int*)x)();
```

If we control the contents of `x`, we control the function being called.

### Step 3: Calculate overflow distance

To overwrite `x`, we overflow `input_data` with 32 bytes of padding followed by the address of `win()`.

### Step 4: Craft the payload

```python
payload = b"X" * 32 + p64(0x4011a0)  # 0x4011a0 is the address of win()
```

### Step 5: Trigger win condition

1. Choose option 2 (Write to buffer)
2. Send the payload
3. Choose option 4 (Print Flag)
4. `check_win()` executes the address now stored in `x` → jumps to `win()` → prints the flag

## Key Points

* Heap buffers allocated sequentially: `input_data` then `x`
* `scanf("%s")` with no bounds check → heap overflow
* Overflow distance = 32 bytes
* Overwrite function pointer with `win()` address
* Trigger via option 4 → function pointer call

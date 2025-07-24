# Heap1 Writeup
**Flag:** `picoCTF{starting_to_get_the_hang_79ee3270}`
---
## Summary
The binary allocates two heap buffers: `input_data` (5 bytes) and `safe_var` (5 bytes). There's a buffer overflow in `write_buffer()` using `scanf("%s", input_data)` with no bounds checking. We can overflow from `input_data` into `safe_var` to overwrite it with "pico" and trigger the win condition.
---
## Exploit Strategy
### Step 1: Analyze heap layout
Looking at the allocation order in `init()`:
```c
input_data = malloc(INPUT_DATA_SIZE);  // 5 bytes
safe_var = malloc(SAFE_VAR_SIZE);      // 5 bytes
```
The heap allocates sequentially, so `safe_var` comes right after `input_data`.

Using option 1 to print the heap confirms the layout and shows the distance between buffers.
---
### Step 2: Calculate overflow distance
`safe_var` starts 34 bytes away from `input_data`:
* 32 bytes of actual distance
* 2 spacing bytes (likely heap metadata/alignment)

So we need exactly 32 bytes of padding + our target string "pico".
---
### Step 3: Craft the payload
```python
payload = "X" * 32 + "pico"
```
This fills the 32-byte gap and overwrites `safe_var` with "pico".
---
### Step 4: Trigger win condition
1. Choose option 2 (Write to buffer)
2. Send the payload: `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXpico`
3. Choose option 4 (Print Flag)
4. The `check_win()` function compares `safe_var` with "pico" and prints the flag
---
## Key Points
* Heap buffers allocated sequentially: `input_data` then `safe_var`
* `scanf("%s")` has no bounds checking → buffer overflow
* Distance from `input_data` to `safe_var` = 32 bytes + 2 spacing
* Payload: 32 padding bytes + "pico" target string
* Win condition: `strcmp(safe_var, "pico") == 0`

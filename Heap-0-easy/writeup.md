# picoCTF Heap-0 Writeup

**Flag**: `picoCTF{my_first_heap_overflow_749119de}`

## Overview

We’re given a simple heap-based binary where two buffers, `input_data` and `safe_var`, are `malloc`’d back-to-back with sizes 5 bytes each. The goal is to modify `safe_var` so that it no longer equals `"bico"`, triggering the win condition and revealing the flag.

## Exploitation

Looking at the `init()` function:
input_data = malloc(INPUT_DATA_SIZE); // 5 bytes  
strncpy(input_data, "pico", INPUT_DATA_SIZE);  
safe_var = malloc(SAFE_VAR_SIZE); // 5 bytes  
strncpy(safe_var, "bico", SAFE_VAR_SIZE);


We know that `malloc` will likely allocate these two chunks adjacent to each other on the heap. Since both are small and there’s no memory isolation between them, we can overflow `input_data` into `safe_var`.

The `write_buffer()` function does this:
scanf("%s", input_data);


This is vulnerable. `%s` with `scanf` has no length limit. If we input more than 5 bytes, we overflow into whatever follows — which is `safe_var`.

By entering 32 "A" characters:
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


We overwrite `safe_var`, corrupting the original `"bico"` value.

Now when we call the “Print Flag” option:
4
if (strcmp(safe_var, "bico") != 0)


This returns true, and the flag is printed.

## Key Points

- Heap allocations for `input_data` and `safe_var` are adjacent  
- No bounds check on `scanf("%s", input_data)`  
- Overwriting `safe_var` changes the condition in `check_win()`  
- Classic heap overflow caused by writing past a small malloc buffer

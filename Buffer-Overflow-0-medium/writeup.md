# Buffer-Overflow-0 Writeup

**Flag:** `picoCTF{ov3rfl0ws_ar3nt_that_bad_9f2364bc}`

## Summary

This challenge is based on a stack buffer overflow that triggers a `SIGSEGV`, which is caught by a custom signal handler that prints the flag.

## Vulnerability

There are two stack buffers in play:

1. `char buf1[100];` in `main()`
2. `char buf2[16];` in `vuln(char *input)`

The `main()` function reads into `buf1` using the unsafe `gets()`, and passes that to `vuln()`:

```c
gets(buf1);        // no bounds checking
vuln(buf1);        // input is copied again using strcpy
````

Then in `vuln()`:

```c
char buf2[16];
strcpy(buf2, input);  // buffer overflow here
```

Because `buf2` is only 16 bytes, any input longer than that causes a **stack overflow**, which can eventually corrupt the return address and cause a **segmentation fault**.

The program installs a handler for `SIGSEGV`:

```c
signal(SIGSEGV, sigsegv_handler);
```

That handler prints the flag and exits:

```c
void sigsegv_handler(int sig) {
  printf("%s\n", flag);
  fflush(stdout);
  exit(1);
}
```

## Exploit Strategy

* Send enough data to `gets()` to overflow `buf2` in `vuln()` and cause a crash.
* This will invoke the `sigsegv_handler()` and print the flag.

## Payload

The precise offset to crash depends on stack layout, but experimentation showed that `55` bytes was enough.

```python
payload = b"X" * 55
```

## Final Notes

* This challenge demonstrates an unusual pattern: using a `SIGSEGV` to control program flow.
* It’s exploitable despite safe practices like `gets()` feeding a large buffer (`buf1[100]`) — because the overflow occurs in a second copy step into a **much smaller buffer** (`buf2[16]`).

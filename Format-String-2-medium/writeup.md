# Format-String-2 Writeup

**Flag:** *(retrieved from successful `sus` overwrite)*

## Summary

The binary reads input with `scanf("%1024s", buf)` and directly prints it using `printf(buf)`, introducing a classic format string vulnerability. The goal is to overwrite the global `sus` variable with the value `0x67616c66` ("flag" in little endian) to pass a conditional check and print the flag.

## Exploit Strategy

1. The `sus` variable is global and stored in the `.data` section, not on the stack.
2. Used `objdump -t vuln | grep sus` to find its address: `0x404060`.
3. Determined the format string argument offset to be `14` by sending a `%p::` pattern.
4. Crafted a format string payload to overwrite the `sus` address with `0x67616c66` using byte-wise writes.
5. Sent the payload to trigger the condition and leak the flag.

## Key Points

- Vulnerable `printf(buf)` call allows arbitrary format string injection
- Global variable `sus` is writable with `%n` specifier
- `fmtstr_payload(14, {0x404060: 0x67616c66}, write_size='byte')` constructs correct exploit
- No PIE, so hardcoded address is valid across executions

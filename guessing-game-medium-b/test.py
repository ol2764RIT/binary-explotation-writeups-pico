from pwn import *
print(b"s" * 64)
crash_bytes = b'faabgaab'   # first 8 bytes at RIP
offset = cyclic_find(crash_bytes)
print(offset)

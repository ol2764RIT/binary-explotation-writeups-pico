(base) tropic@vulcan:~/projects/RE-writeups/ropfu-hard-u$ checksec ./vuln
[*] '/home/tropic/projects/RE-writeups/ropfu-hard-u/vuln'
    Arch:       i386-32-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX unknown - GNU_STACK missing
    PIE:        No PIE (0x8048000)
    Stack:      Executable
    RWX:        Has RWX segments
    Stripped:   No
(base) tropic@vulcan:~/projects/RE-writeups/ropfu-hard-u$ 

ropgadget --binary ./vuln > gadgets.txt

Padding of 16 bytes to override into rop territory

32 bit binary so look for Exx registers not Rxx


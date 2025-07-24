    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No

%p * a good amount to leak previous stack values

since they get read in we can try to leak the stack values by %p to find the data types
then we can copy that data dump/raw response

we can convert from hex to utf-8 ad we have to reverse since its little endian encoded?

picoCTF{4n1m41_57y13_4x4_f14g_9135fd4e}
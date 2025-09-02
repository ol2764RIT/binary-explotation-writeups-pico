use w a s d to move

walk to flag normally nothing
walk to flag from oob -> stack smashing detected

99 s's seg fault

(base) tropic@vulcan:~/projects/RE-writeups/babygame01-medium-u$ checksec ./game
[*] '/home/tropic/projects/RE-writeups/babygame01-medium-u/game'
    Arch:       i386-32-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x8048000)
    Stripped:   No

game: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=02a3bb43121b1f6fbc2ab9154ab38a9427e19149, for GNU/Linux 3.2.0, not stripped


solution:

walk up 4 and left 8 to set flag to value of stack protection? or something else

p to win

flag
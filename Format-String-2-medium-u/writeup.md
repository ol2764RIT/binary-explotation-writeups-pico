looked at vuln.c

we need to set sus the global int to match that conditional
global ints are not on the stack

objdump -t ./vuln | grep sus 
for the address of sus 

No pie so this is easy, we could also used gdb/ghidra/etc. 

flag!
# GDB Binary Exploitation Cheatsheet

## Starting & Basic Setup
```bash
gdb ./binary                    # Start GDB with binary
gdb -q ./binary                 # Quiet mode (no banner)
set disassembly-flavor intel    # Use Intel syntax
set follow-fork-mode child      # Follow child processes
checksec                        # Check binary protections (if peda/gef installed)
```

## Information Gathering
```bash
info functions                  # List all functions
info variables                  # List global variables
info registers                  # Show register values
info proc mappings              # Show memory mappings
vmmap                          # Memory map (peda/gef)
```

## Disassembly & Code Analysis
```bash
disas main                      # Disassemble main function
disas 0x401000                  # Disassemble at address
x/20i $rip                      # Show 20 instructions from current position
x/20i 0x401000                  # Show 20 instructions from address
```

## Breakpoints
```bash
b main                          # Break at main function
b *0x401234                     # Break at specific address
b *main+42                      # Break at offset from function
info breakpoints                # List all breakpoints
delete 1                        # Delete breakpoint 1
clear                          # Clear all breakpoints
```

## Memory Examination
```bash
x/20x $rsp                      # Show 20 hex values from stack pointer
x/20gx $rsp                     # Show 20 8-byte values (64-bit)
x/20wx $rsp                     # Show 20 4-byte values (32-bit)
x/s 0x401000                    # Show string at address
x/20c $rax                      # Show 20 characters
telescope $rsp                  # Show stack with references (peda/gef)
```

## Register Manipulation
```bash
print $rax                      # Show register value
set $rax = 0x41414141           # Set register value
print/x $rsp                    # Show in hex
print (char*)$rax               # Cast and print as string
```

## Stack & Buffer Analysis
```bash
x/40wx $rsp                     # Examine stack (32-bit)
x/40gx $rsp                     # Examine stack (64-bit)
info frame                      # Show current frame info
bt                             # Backtrace (call stack)
find $rsp, $rsp+200, 0x41414141 # Find pattern in stack
```

## Pattern Generation (for offset finding)
```bash
# Generate pattern (with peda/gef)
pattern create 200              # Create 200-byte pattern
pattern offset 0x41414141       # Find offset of value in pattern

# Manual pattern generation
python -c "print 'A'*20 + 'B'*4 + 'C'*20"
```

## ROP/Gadget Finding
```bash
# With peda/gef
ropsearch "pop rdi"            # Find ROP gadgets
ropsearch "ret"                # Find return gadgets
ropper --file ./binary         # External tool (install separately)
```

## Address & Symbol Resolution
```bash
print system                    # Get address of system function
print &system                  # Alternative syntax
p/x &system                    # Print in hex
info address system             # Get symbol information
```

## Exploitation Helpers
```bash
# GOT/PLT analysis
x/20gx 0x601000                # Examine GOT (adjust address)
info symbol 0x401030           # What symbol is at address

# String/shellcode injection
find 0x400000, 0x500000, "/bin/sh"  # Find strings in binary
searchmem "/bin/sh"            # Search memory for string (peda/gef)
```

## Process Control
```bash
run                            # Start program
run < input.txt                # Run with input file
run arg1 arg2                  # Run with arguments
continue                       # Continue execution
step                           # Step into (source level)
stepi                          # Step one instruction
next                           # Step over (source level)
nexti                          # Step over one instruction
finish                         # Run until function returns
```

## Advanced Memory Operations
```bash
# Memory writing
set {int}0x601040 = 0x41414141      # Write 4 bytes
set {long}0x601040 = 0x4141414141414141  # Write 8 bytes
set {char}0x601040 = 'A'            # Write single byte

# Memory searching
find 0x400000, 0x500000, 0x41, 0x41, 0x41, 0x41  # Find hex pattern
```

## Useful One-Liners
```bash
# Find writable memory
info proc mappings | grep rw

# Check for stack canaries
disas main | grep stack_chk

# Find system calls
catch syscall write

# Auto-examine stack on break
define hook-stop
x/20gx $rsp
end
```

## Common GDB Extensions
```bash
# Install peda (Python Exploit Development Assistant)
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit

# Install gef (GDB Enhanced Features)
wget -O ~/.gdbinit-gef.py https://gef.blah.cat/py
echo "source ~/.gdbinit-gef.py" >> ~/.gdbinit

# Install pwndbg
git clone https://github.com/pwndbg/pwndbg
cd pwndbg && ./setup.sh
```

## Quick Exploit Development Workflow
1. `checksec` - Check protections
2. `disas main` - Understand program flow
3. Find vulnerability (buffer overflow, format string, etc.)
4. `pattern create` - Generate overflow pattern
5. Crash program, find offset with `pattern offset`
6. `info functions` - Find interesting functions
7. `ropsearch` - Find ROP gadgets if needed
8. Build exploit payload
9. Test with `run < payload`

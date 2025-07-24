# Binary Analysis and Exploitation of PicoCTF Challenges

Personal project exploiting PicoCTF binary challenges to develop vulnerability research and reverse engineering skills.

> **Disclaimer**
>
> This repository contains writeups, exploit scripts, and research based solely on **educational Capture The Flag (CTF) challenges**, primarily from **picoCTF**.  
> All binaries involved are intentionally vulnerable and executed in sandboxed environments.  
> No real-world software, services, or systems were targeted.  
> This work is strictly for ethical skill development and legal, academic purposes.  
> I do not condone or engage in any unauthorized or malicious activity.

## Important Note

Each challenge folder is structured to include the relevant binary and its corresponding `exploit.py` script, where applicable.  
If a folder does **not** include an `exploit.py`, it's either:

- A **trivial challenge** not requiring a custom exploit, or  
- A challenge that was **hosted on PicoCTF's remote servers**, where local exploitation wasn’t possible.

## What I'm Learning

**Reverse Engineering**
- Static analysis with Ghidra and IDA
- Dynamic debugging with GDB
- Assembly code analysis (x86/x64)

**Binary Exploitation**
- Buffer overflows and format strings
- ROP chains and memory corruption
- Environment manipulation and path injection
- Shell escapes from restricted environments

**Tools Used**
- Disassemblers: Ghidra, objdump, readelf
- Debuggers: GDB, PEDA
- Scripting: Python, pwntools
- Analysis: checksec, ROPgadget, strings

## Repository Structure

```
├── Hash-Only-1-medium/     # PATH injection challenge
│   ├── writeup.md
│   └── flaghasher
├── Hash-Only-2-medium/     # Sequel with auto-execution
│   ├── writeup.md
│   └── flaghasher
├── Format-String-0-easy/   # Format string vulnerability
│   ├── writeup.md
│   └── binary
├── Heap-0-easy/           # Heap exploitation basics
│   ├── writeup.md
│   └── binary
├── PIE-writeup-easy/      # Position Independent Executable
│   ├── writeup.md
│   └── binary
├── exploit.py             # Pwntools exploit template/learning
└── GEF-cheatsheet.md      # GDB Enhanced Features reference
```

## Challenges Completed

- **Hash-Only Series**: PATH hijacking and binary substitution
- **Format String**: Arbitrary read/write primitives  
- **Heap Exploitation**: Basic heap manipulation
- **PIE Bypass**: Position Independent Executable analysis

## Skills Demonstrated

- Finding and exploiting binary vulnerabilities
- Reverse engineering unknown binaries
- Writing reliable exploit code
- Clear technical documentation

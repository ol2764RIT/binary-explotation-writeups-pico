# Initial Analysis of `baked_password` (from crackmes.one)

**Reported Difficulty:** 2.0

**Binary Type:** ELF (Linux executable)

Upon inspection, the binary appears to be packed. Function `FUN_00102daa` and label `LAB_00102e3d` suggest that the binary is compressed using **UPX version 3.95**. This is a common packing method used to hinder static analysis.

## First step

UPX being packed or the binary stating that is packed with UPX causes us a problem of annoyance.
Firstly to prevent any time wasted, let's use Detect it Easy (DiE) to make sure that this is actually packed with UPX version 3.95.
As we can see from detect it easy, The binary was packed using UPX v3.95 with its highest compression setting, using the NRV algorithm. This doesn't affect functionality but will make static analysis harder until you unpack it.
The binary is a 64-bit dynamically linked PIE executable targeting a Unix-like OS on AMD64, using shared libraries and position-independent code, which means addresses are resolved at runtime and static analysis requires accounting for runtime base addresses.





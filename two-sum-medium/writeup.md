# Two Sum Writeup

**Flag:** `picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_76f333c8}`

## Summary

This challenge features a basic integer overflow. The goal is to satisfy the condition that `n1 > n1 + n2` in order to pass a condition and print the flag.

## Vulnerability

## Exploit Strategy

1. Assign a value of int max to the digit `n1`
2. Assign any abritrary value for `n2` such that the condition of `n1 > n1 + n2` is satisfied

## Exploit Payload

The exploit is fairly rudamentary so it is not needed for a automation.

## Final Notes

* No check of INT_MAX to fufill condition makes it vulnerable to these types of issues.
* Author should implement a check for int_max to never leak flag!

# Two Sum Writeup

**Flag:** `picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_76f333c8}`

## Summary

This challenge features a basic integer overflow. The goal is to satisfy the condition that `n1 > n1 + n2` in order to pass a condition and print the flag.

## Vulnerability

`
static int addIntOvf(int result, int a, int b) {
    result = a + b;
    if(a > 0 && b > 0 && result < 0)
        return -1;
    if(a < 0 && b < 0 && result > 0)
        return -1;
    return 0;
}
`

The vulnerability lies in the function `addIntOvf()` due to how addition is structured, `n1` being INT_MAX and adding a result of any value `n2` such that `n1 > n2 + n1` results in this function returning -1 fufilling flag condition.
This is because INT_MAX `0x7FFFFFFF` plus a example digit of `0x00000001` will return with a overflow that does not fufill the condition of result being greater than 0 since this will overflow into `0x80000000` which represets the two's complement or negative number.

## Exploit Strategy

1. Assign a value of int max to the digit `n1`
2. Assign any abritrary value for `n2` such that the condition of `n1 > n1 + n2` is satisfied

## Exploit Payload

The exploit is fairly rudamentary so it is not needed for a automation.

## Final Notes

* No check of INT_MAX to fufill condition makes it vulnerable to these types of issues.
* Author should implement a check for int_max to never leak flag!

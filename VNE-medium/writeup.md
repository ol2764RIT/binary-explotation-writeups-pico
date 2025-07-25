# VNE Writeup

**Flag:** `picoCTF{Power_t0_man!pul4t3_3nv_1ac0e5a3}`

## Summary

The binary runs as root but requires the `SECRET_DIR` environment variable to be set. It uses `system("ls $SECRET_DIR")`, allowing control over the command run as root if both `SECRET_DIR` and `PATH` are manipulated.

## Exploit Strategy

1. Running `./bin` without setting `SECRET_DIR` returns an error.

2. Setting `SECRET_DIR=~/ls` causes the binary to list the provided path.

3. Setting `SECRET_DIR=/root` reveals that `flag.txt` exists there.

4. Created a fake `ls` script in the home directory that runs `cat /root/flag.txt`.

5. Prepended `PATH` with the home directory to hijack the `ls` call.

6. Ran the binary with `PATH=~/:$PATH SECRET_DIR=/root` to trigger the exploit.

## Key Points

- `SECRET_DIR` is unsanitized and passed directly into `system()`
- `ls` is resolved using the user-controlled `PATH`
- Fake `ls` script executed as root due to `setuid` behavior
- Final script read `/root/flag.txt` and printed the flag

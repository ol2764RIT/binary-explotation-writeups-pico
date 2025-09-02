
rand seed is static

use loop to find list of 10 numbers?
[84,87]

static linking + nx = rop chain

key takeaways:

- rop is super finicky unless you get a clean gadget + the earliest clean gadget you can find
- .bss is writable and good place to stage /bin/sh changes into
- all our goal was to execve('/bin/sh', 0, 0)
- this vuln worked because the buffer overreads user input so we could technically fill the buffer and then start adding data to be treated like instructions
- rand was static seed wise, this meant we just needed to bruteforce one to two numbers
- this took over one week of finicking but it makes so much sense now that we have clean gadgets

flag
picoCTF{r0p_y0u_l1k3_4_hurr1c4n3_476d756f24c7952d}
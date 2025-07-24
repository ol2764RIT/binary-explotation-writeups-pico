
Safe_var starts 34 bytes (32 bytes + 2 spacing bytes) away from write to buffer addr

We need to craft input that fills up exactly 32 bytes

Writing 33 bytes overwrites the start of the secondary variable on the heap so we need to be able to add what we want the variable to be
We will construct a payload that is exactly the max length appended with the goal word being pico!

`
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXpico
`

picoCTF{starting_to_get_the_hang_79ee3270}


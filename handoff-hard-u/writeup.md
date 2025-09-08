checksec shows nx is unknown

lets check if nx exists

```
(base) tropic@vulcan:~/projects/RE-writeups/handoff-hard-u$ ./handoff &
cat /proc/$!/maps | grep stack
kill $!
[1] 603465
What option would you like to do?
1. Add a new recipient
2. Send a message to a recipient
3. Exit the app
7ffc9c6c1000-7ffc9c6e3000 rwxp 00000000 00:00 0                          [stack]

[1]+  Stopped                 ./handoff
```

rwxp means it is executable! no NX!
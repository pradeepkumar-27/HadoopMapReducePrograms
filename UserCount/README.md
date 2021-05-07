# User Count
MapReduce program to count the number of users in a Linux Operating System  other than root.

## Sample file
/etc/passwd

    root:x:0:0:root:/root:/bin/bash
    bin:x:1:1:bin:/bin:/sbin/nologin
    daemon:x:2:2:daemon:/sbin:/sbin/nologin
    adm:x:3:4:adm:/var/adm:/sbin/nologin
    lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
    sync:x:5:0:sync:/sbin:/bin/sync
    shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
    halt:x:7:0:halt:/sbin:/sbin/halt
    mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
    uucp:x:10:14:uucp:/var/spool/uucp:/sbin/nologin
    operator:x:11:0:operator:/root:/sbin/nologin
    games:x:12:100:games:/usr/games:/sbin/nologin
    nobody:x:99:99:Nobody:/:/sbin/nologin
    aaad:x:1001:0:root:/root:/bin/bash
    bbb:x:1002:0:root:/root:/bin/bash
    ccc:x:1003:0:root:/root:/bin/bash
    dddd:x:1004:0:root:/root:/bin/bash
    
The number of users other than root here is 4

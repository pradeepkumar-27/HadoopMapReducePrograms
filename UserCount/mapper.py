import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split(":")
    uid = data[2]
    shell = data[6]
    if int(uid) >= 1000 and shell == "/bin/bash":
        print(line)
import platform
import os

if "Linux" not in platform.platform():
    print("only Linux is supported!!!")
    exit(0)

for x in range(1,10):
    for line in os.popen("cat /proc/sys/kernel/random/uuid"):
        print(line.upper())

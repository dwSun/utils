import os
f = os.popen("deborphan")
strs = ""
for s in f:
    strs+=" "
    strs+=s.rstrip()
print("sudo apt-get purge "+strs) if strs else print("Nothing!!!")
#open("k.txt","w").write(strs)


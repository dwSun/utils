#!/usr/bin/python3

with open("list") as inf:
    with open("list2","w") as ouf:
        for line in inf:
            try:
                ouf.write("aptitute install -y "+line.split()[1]+"\r\n")
            except:
                pass

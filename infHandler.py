import os
with open(r"d:\333.bat","w") as infile:
    for root,dirs,files in os.walk(r"E:\Software\System\Windows\System"):
        for file in files:
            if file.lower().endswith("inf"):
                ff='infdefaultinstall "%s"\n'%(root + "\\" + file)
                infile.write(ff)
                print(ff)

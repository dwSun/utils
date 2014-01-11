#-------------------------------------------------------------------------------
# Name:       MassiveCompress
# Purpose:
#
# Author:      Joe
#
# Created:     11/07/2013
# Copyright:   (c) Joe 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------



def main():
    print("Path to handle:")
    path=input()
    print(path)
    print("Path correct?(Y/N)")
    inp=input()
    if  "y" not in inp.lower():
        return

    print("Extension to handle:")
    fext=input()
    print(fext)
    print("extension correct?(Y/N)")
    inp=input()
    if  "y" not in inp.lower():
        return
    MassiveComp(path,fext)

def main2():
    MassiveComp("/media/d/Data/","epub")


def MassiveComp(path,fext):
    import os
    for top,dirs,files in os.walk(path):
        for f in files:
            if(f.endswith(fext)):
                src=top+"/"+f
                compress(src,delete=False)


def logger(msg,pri=True):
    print(msg)    
    f=open("/tmp/log.log","a")
    f.write(msg+"\n")
    f.close()

    
def compress(src,ext=".tgz",delete=False):
    import os
    import subprocess
    dst=src+ext
    cmd='tar -zcvf "%(dst)s" "%(src)s"'%{"src":src,"dst":dst}
    try:
        logger(src+"\t===>\t"+dst)
        subprocess.call(cmd,shell=True)
        if delete == True:
            os.remove(src)
    except e:
        logger("Failed on:\t"+src)
        logger(e.errno, e.strerror)
        try:
            os.remove(dst)
        except:
            print("Failed to remove:\t"+dst)
        exit()
    pass


if __name__ == '__main__':
    main2()

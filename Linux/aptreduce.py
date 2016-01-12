#remove all previous version at apt cache to reduce size.
# Python 3.4.4


import os
from functools import reduce
print(os.path.abspath("."))

alls = os.walk(os.curdir) 


def genf(root,dirs):  
    def redfun(f1,f2):
        f1a = f1.split(sep="_",maxsplit=2)
        f2a = f2.split(sep="_",maxsplit=2)
        if f1a[0] == f2a[0]:
            ff=os.path.join(root,dirs,f1)
            print("del:\t"+ ff)
            try:
                os.remove(ff)
            except Exception as e:
                print(e)            
        return f2
    return redfun

for roots,dirs,files in alls:
    if not files:
        break
    files.sort()
    reduce(genf(roots,dirs),files)
    

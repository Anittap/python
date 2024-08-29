import os
import posixpath

d = []

for item in os.walk('/etc/'):

    curdir,subdir,subfiles =item

    for subfile in subfiles:

        abspath = posixpath.join(curdir,subfile)
        
        if abspath.endswith('.conf') and posixpath.isfile(abspath):
        
            size = posixpath.getsize(abspath)

            d.append([abspath,size])

def max_size(file):    

    return file[1]

result = sorted(d,key=max_size,reverse=True)

for i in result:

    filename,size = i

    if size >= 10000:

        print(f'{filename:60} - {size}')

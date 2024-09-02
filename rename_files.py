import os
import sys
import posixpath

if len(sys.argv) ==4:
    directory = sys.argv[1]
    fromext = sys.argv[2]
    toext = sys.argv[3]

    if posixpath.isdir(directory):

        for item in os.walk(directory):

            curdir,subdir,subfiles = item

            for subfile in subfiles:

                abspath = posixpath.join(curdir,subfile)

                if abspath.endswith(fromext):

                    file, extension = posixpath.splitext(abspath)

                    destfile = f"{file}.{toext.lstrip('.')}"

                    os.rename(abspath,destfile)
                

    else:

        print(f'The given path {directory} is not a valid directory')

else:
    print('usage : python2 filename fromextension toextension')

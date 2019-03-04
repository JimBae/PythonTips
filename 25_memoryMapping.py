import os
import sys
import mmap

with open("hello.txt", 'wb') as f:
    f.write(b"Hello Python!\n")

with open("hello.txt", 'r+b') as f:
    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(mm.readline())
    print(mm[:5])
    mm[6:] = b" world!\n"
    mm.seek(0)
    print(mm.readline())
    mm.close()

# hdf5 memory mapping
# ref : https://gist.github.com/maartenbreddels/09e1da79577151e5f7fec660c209f06e

#import h5py
#filePath = 'test.hdf5'




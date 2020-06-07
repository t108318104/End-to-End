import os
path = 'test/txt/p225'



for i,fname in enumerate(os.listdir(path)):
    new_fname = 'p225_%04d.txt' % (i+1)
    os.rename(os.path.join(path, fname), os.path.join(path, new_fname))

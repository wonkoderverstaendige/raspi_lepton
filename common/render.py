import sys; import numpy as np

chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))

GCF = 1
img = np.random.random_integers(45, 255, size=(60, 80))
def print_arr(img):
    img = img.astype(np.float)
    img -= img.min()
    img = (1.0 - img/img.max())**GCF*(chars.size-1)
    print( "\n".join( ("".join(r) for r in chars[img.astype(int)]) ) )

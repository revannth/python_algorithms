#lowlevelarrays.py

from array import array

k = array('i',list(xrange(1000)))

b = array('c',"Revannth")

print(k[0:],b[0:])


#These are compact arrays which are a little bit smaller than the actual lists but not as small as ctypes

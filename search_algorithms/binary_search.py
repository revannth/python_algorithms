#binary_search.py

def bny_sch(l,itm):

	found = False
	bottom = 0
	top = len(l) - 1

	while bottom<=top and not found:
		middle = (bottom + top)/2
		if l[middle]==itm:
			found = True
		elif l[middle]<itm:
			bottom = middle + 1
		else :
			top = middle -1
	return found


if __name__ == '__main__':
	l_i_s_t = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

	itm_m = int(input("What Item are you looking for"))

	if bny_sch(l_i_s_t,itm_m):
		print "Element found"
	else:
		print "Element not found"


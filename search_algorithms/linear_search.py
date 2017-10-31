#linear_search.py
import os

def find(itme,l):
	itme = itme.lower()
	l = [it.lower() for it in l]

	position = 0
	found = False

	while position<len(l) and not found:
		if l[position] == itme:
			found = True
		position+=1;

	return found

if __name__=="__main__":

	lste=["Apple","Orange","Mango","Pineapple","Strawberry","Tomato"]
	
	if find("Mango",lste):
		print "Element found"
		exit()
	else:
		print "Element not found"
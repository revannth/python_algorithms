#Reverse_string.py

#Still has to be refined

def revstr(S,low,high):

	if low<high:
		
		return [S[high],revstr(S,low+1,high-1),S[low]]


if __name__ == '__main__':
	Str = "Revannth"

	St = " ".join(map(str,revstr(Str,0,len(Str)-1)))
	print St


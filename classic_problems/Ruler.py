#Ruler.py

#This program recursively creates the lines of a ruler

def draw_line(tick_len,tick_label = ''):
	line = '-'*tick_len
	if tick_label:
		line += ' '+tick_label
	print line

def draw_intervel(center_len):

	if center_len>0:
		draw_intervel(center_len-1)
		draw_line(center_len)
		draw_intervel(center_len-1)

def draw_ruler(num_inch,major_len):
	draw_line(major_len,'0')
	for j in range(1,num_inch+1):
		draw_intervel(major_len-1)
		draw_line(major_len,str(j))

if __name__ =='__main__':
	#print("Printing the scale upto 1 inch")
	draw_ruler(5,1)




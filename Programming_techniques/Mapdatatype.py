#Mapdatatype.py


#Map for word count


freq = {}

for piece in open('/Users/vedalasrinivas/Documents/communicando_website/app/templates/Our_team1.html').read().lower().split():
	word = ''.join(c for c in piece if c.isalpha())
	if word:
		freq[word] = 1 + freq.get(word,0)
max_count = 0
max_word = ''

for (w,c) in freq.items():
	if c>max_count:
		max_count=c
		max_word=w

print(max_word,max_count)



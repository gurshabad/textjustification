words = [z for z in open("file.txt").read().split(' ')] #creating list of words
width = 15 #max column size, we assume this is greater than the length of any given word; could take this as input as well
print words[0],
space = width - len(words[0])
for x in range(1, len(words)):
	l = len(words[x])
	if l <= space:
		space -= l+1
		print " " + words[x],
	else:
		print "\n" + words[x],
		space = width - l
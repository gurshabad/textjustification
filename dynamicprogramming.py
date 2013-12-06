words = [z for z in open("file.txt").read().split(' ')] #creating list of words
width = 6 #max column size, we assume this is greater than the length of any given word; could take this as input as well

INF = 9999

def cost_function(i, j, width):
	if j < i:
		return width ** 3
	w = words[i:j+1]
	spaces = len(w) - 1
	total = spaces
 	for a in w:
		total += len(a)


	if total > width:
		return INF

	if j == len(words) - 1:
		return 0

	return (width - total) ** 3

cost_mat = []
for a in range(0, len(words)):
	cost_mat.append([])
	for b in range(0, len(words)):
		cost_mat[-1].append(0)

a, b = 0, 0

for a in range(0, len(words)):
	for b in range(a, len(words)):
		cost_mat[a][b] = cost_function(a, b, width)

p = [0] * len(words)
p[0] = (width - len(words[0])) ** 3 
i, j = 0, 0
for i in range(1, len(words)):
	possible = [p[i-1] + cost_function(i, i, width)]
	for j in range(0, i):
		possible.append(sum(p[0:j]) + cost_mat[j][i])
	p[i] = min(possible)

print "Final cost of text:", p[-1]
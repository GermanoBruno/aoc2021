import inputUtils

inp = inputUtils.loadInput(5)

inp = [[line.split("->")[0].split(',') , line.split("->")[1].split(',')] for line in inp]
inp = [[[int(i) for i in coordinate] for coordinate in line] for line in inp]
# Previous format:
# "x1, y1 -> x2, y2"
# Current format:
#[[x1, y1],[x2, y2]]

for line in inp:
	if((line[0][0] == line[1][0]) or (line[0][1] == line[1][1])):
		print(line)



# Advent of Code 2015 - day 3

# Read input
with open("input3.txt", "r") as f:
	input1 = f.read()
n = len(input1)

# PART I
x1 = x2 = y1 = y2 = 0
visited_houses = [(0,0)]

for c in input1:
	if c=="<":
		x1-=1
	elif c==">":
		x1+=1
	elif c=="v":
		y1-=1
	elif c=="^":
		y1+=1
	if (x1,y1) not in visited_houses:
		visited_houses.append((x1,y1))
answer1 = len(visited_houses)

# PART II
visited_houses = [(0,0)]
x1 = x2 = y1 = y2 = 0
for i,c in enumerate(input1):
	if i%2==0:
		if c=="<":
			x1-=1
		elif c==">":
			x1+=1
		elif c=="v":
			y1-=1
		elif c=="^":
			y1+=1
		if (x1,y1) not in visited_houses:
			visited_houses.append((x1,y1))
	elif i%2==1:
		if c=="<":
			x2-=1
		elif c==">":
			x2+=1
		elif c=="v":
			y2-=1
		elif c=="^":
			y2+=1
		if (x2,y2) not in visited_houses:
			visited_houses.append((x2,y2))

answer2 = len(visited_houses)

print("Part I: ", answer1)
print("Part II: ", answer2)
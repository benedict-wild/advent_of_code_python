# Advent of Code 2015 - day 1

# Read input
with open("input1.txt", "r") as f:
	input1 = f.read()

floor, answer2 = 0,0

# Loop through input
for i, c in enumerate(input1):
	if c=='(':
		floor+=1
	elif c==')':
		floor-=1
# Check whether basement entered first time
	if answer2==0 and floor==-1:
		answer2=i

print("Part I:", floor)
print("Part II:", answer2)
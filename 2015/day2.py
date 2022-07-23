# Advent of Code 2015 - day 2

# Read input
with open("input2.txt", "r") as f:
	input1 = f.readlines()

answer1, answer2 = 0,0

# Loop through input
for line in input1:
	tmp = sorted(list(map(int,line.split('x'))))
	answer1+=2*(tmp[0]*tmp[1]+tmp[0]*tmp[2]+tmp[1]*tmp[2])+tmp[0]*tmp[1];
	answer2+=2*(tmp[0]+tmp[1])+tmp[0]*tmp[1]*tmp[2];

print("Part I: ", answer1)
print("Part II:", answer2)
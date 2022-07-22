
N = 5

l = list(range(N * -1, N))

f = open("dz24.txt", "r")

positions = []

for line in f.readlines():
    positions.append(int(line.rstrip('\n')))

result = None
for position in positions:
    if result == None:
        result = l[position]
    else:
        result *= l[position]

print(result)
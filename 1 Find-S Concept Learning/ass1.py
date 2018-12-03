# Find-S Concept Learning

from numpy import genfromtxt

data = genfromtxt('data1.csv', delimiter=',')	#data from 'data1.csv' is stored in 'data'

# The final hypothesis will be stored in s

s = [0,0,0,0,0,0,0,0]

# 1st tuple where y==1 (calss label) is stored in s
change = 0
i = 0
while change==0 and i<20:
	if data[i][8] == 1:
		for j in range(8):
			s[j] = data[i][j]
		change = 1
	i = i + 1
	
# Now s is compared with each tuple in data
# Only those tuples are taken where value of (y)/result is 1
# If there is change in only one attribute then it is don't care condition
# The index of don't care is assigned 10
# The process is repeated till there is no change from start to end


repeat = 1
while repeat==1:
	change = 0
	for i in range(20):
		if data[i][8]==1:
			nchange=0
			for j in range(8):
				if s[j]!=data[i][j] and s[j]!=2:
					nchange = nchange + 1
					index = j
			if nchange == 1:
				s[index] = 2
				change = 1
	if change!=1:
		repeat=0
		
print(s)

# n is the number of literals in hypothesis
n=0
for i in range(8):
	if s[i] != 2:
		n = n + 1

print(n)

# don't cares are not printed
for i in range(8):
	if s[i]!=2:
		if s[i] == 1:
			print((i+1), end=" ")
		else:
			print(-(i+1), end=" ")

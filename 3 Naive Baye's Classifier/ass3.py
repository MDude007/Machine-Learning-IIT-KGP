from numpy import genfromtxt


data = genfromtxt('data3.csv', delimiter=',')	#data from 'data3.csv' is stored in 'data'


#prob0 is the probability for class label y = 0
#prob1 is the probability for class label y = 1

count0 = 0		#count for prob0
count1 = 0		#count for prob1

for i in range(20):
	if data[i][8] == 0: count0 = count0 + 1
	else: count1 = count1 + 1

prob0 = float(count0)/float(20)
prob1 = float(count1)/float(20)

prob0res0 = [0,0,0,0,0,0,0,0]	#probability for xi = 0 when class label y = 0
prob1res0 = [0,0,0,0,0,0,0,0]	#probability for xi = 1 when class label y = 0
prob0res1 = [0,0,0,0,0,0,0,0]	#probability for xi = 0 when class label y = 1
prob1res1 = [0,0,0,0,0,0,0,0]	#probability for xi = 1 when class label y = 1

for i in range(8):
	count00 = 1		#Laplacian smoothing with alpha = 1, count for prob0res0
	count10 = 1		#Laplacian smoothing with alpha = 1, count for prob1res0
	count01 = 1		#Laplacian smoothing with alpha = 1, count for prob0res1
	count11 = 1		#Laplacian smoothing with alpha = 1, count for prob1res1
	for j in range(20):
		if data[j][8] == 0:
			if data[j][i] == 0: count00 = count00 + 1
			else: count10 = count10 + 1
		else:
			if data[j][i] == 0: count01 = count01 + 1
			else: count11 = count11 + 1
	prob0res0[i] = float(count00)/float(count0 + 2)		#count0 + 2 since 2 possible values of xi i.e. 0 and 1
	prob1res0[i] = float(count10)/float(count0 + 2)		#count0 + 2 since 2 possible values of xi i.e. 0 and 1
	prob0res1[i] = float(count01)/float(count1 + 2)		#count1 + 2 since 2 possible values of xi i.e. 0 and 1
	prob1res1[i] = float(count11)/float(count1 + 2)		#count1 + 2 since 2 possible values of xi i.e. 0 and 1



test = genfromtxt('test3.csv', delimiter=',')	#data from 'test3.csv' is stored in test

#res0 is the probability that the class label y = 0
#res1 is the probability that the class label y = 1

for i in range(4):
	res0 = prob0
	res1 = prob1
	for j in range(8):
		if test[i][j] == 0: res0 = res0 * prob0res0[j]
		else: res0 = res0 * prob1res0[j]
	for j in range(8):
		if test[i][j] == 0: res1 = res1 * prob0res1[j]
		else: res1 = res1 * prob1res1[j]
	if res0 >= res1: print 0,
	else: print 1,

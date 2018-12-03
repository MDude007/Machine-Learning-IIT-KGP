#Assignment No. 4 - K-NN Classifier


from numpy import genfromtxt
import math

data = genfromtxt('data4.csv', delimiter=',')	#data from 'data4.csv' is stored in 'data'

test = genfromtxt('test4.csv', delimiter=',')	#data from 'test3.csv' is stored in test


#function for calculation Euclidean Distance
def dist(data_i, test_i):
	sum = 0
	for i in range(4):
		temp = (data[data_i][i] - test[test_i][i])*(data[data_i][i] - test[test_i][i])
		sum = sum + temp
	distance = math.sqrt(sum)
	return distance

	
#function to find k nearest neighbours and find the class label
#here k is take 5
def knn(test_i):
	
	#this vector stores the distance of test case from ith sample
	distance = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	
	for i in range(74):
		distance[i] = dist(i, test_i)

	#this vector stores the index of ith nearest sample		
	nearest = [0,0,0,0,0]
	
	#following steps are done to store 5 nearest neighbours into 'nearest'
	n=0
	j=-1
	previous = -1
	least = -1
	while(n<5):
		greatest = 100
		change = 0
		for i in range(74):
			if least==distance[i] and distance[i]<=greatest and previous<i and change==0:
				greatest = distance[i]
				j = i
				change = 1
			elif least<distance[i] and distance[i]<greatest and change==0:
				greatest = distance[i]
				j=i
		
		nearest[n] = j
		previous = j
		n = n + 1
		least = greatest

	n_0 = 0		#count for class label == 0
	n_1 = 0		#count for class label == 0
	
	#storing count n_0 and n_1
	for i in range(5):
		if data[nearest[i]][4] == 0:	n_0 = n_0 + 1
		else:	n_1 = n_1 + 1
	
	#prints output
	if n_0 > n_1: print 0,
	else:	print 1,

#calls function knn for each test case
for i in range(26):
	knn(i)

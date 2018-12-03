#Assignment 7: K-Means Clustering

#Specifications:
#	Works for input file (data7.csv) with same number of rows and cols.

from numpy import genfromtxt
from numpy import savetxt
import random
import math

data = genfromtxt('data7.csv', delimiter=',')	#data from 'data7.csv' is stored in 'data'

m1 = random.randint(0,19)	#initially random centroid taken for cluster 1
m2 = random.randint(0,19)	#initially random centroid taken for cluster 2

x=0
while(x==0):				#to make sure that 2 centroids are not the same
	if m1==m2:
		m2 = random.randint(1,20)
	else:
		x=1

m1x = data[m1]				#co-ordinates of centroid 1
m2x = data[m2]				#co-ordinates of centroid 2

cLabel = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]		#cluster labels for the given data

def distance(i,j):			#Euclidean Distance
	sum=0
	for k in range(8):
		sum = sum + (data[i][k] - data[j][k])*(data[i][k] - data[j][k])
	sum = math.sqrt(sum)
	return(sum)
	
def findNearest(i,data,m1x,m2x):	#assigning point to the cluster whose centroid is nearest
	d1 = 0
	d2 = 0
	for j in range(8):
		d1 = d1 + (data[i][j] - m1x[j])*(data[i][j] - m1x[j])
		d2 = d2 + (data[i][j] - m2x[j])*(data[i][j] - m2x[j])
	d1 = math.sqrt(d1)
	d2 = math.sqrt(d2)
	if d1 > d2: return(2)
	else: return(1)

def findMean(data,cLabel,m1x,m2x):
	for i in range(8):
		x1 = 0
		count1 = 0
		x2 = 0
		count2 = 0
		for j in range(20):
			if cLabel[j]==1:
				x1 = x1 + data[j][i]
				count1 = count1 + 1
			else:
				x2 = x2 + data[j][i]
				count2 = count2 + 1
		m1x[i] = x1/count1
		m2x[i] = x2/count2
	

x=10					#10 iterations
while(x>0):
	for i in range(20):
		cLabel[i] = findNearest(i,data,m1x,m2x)
	print(cLabel)
	findMean(data,cLabel,m1x,m2x)
		
	x = x - 1
	
savetxt('output.out', cLabel, fmt='%d', delimiter=" ") 	#save o/p to '14CS30009_7.out'
	
print(cLabel)

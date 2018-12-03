#Assignment 6 Perceptron Learning

#Specifications:
#	Works for input files (data6.csv and test6.csv) with same number of rows and cols.
#	By trials, accuracy was better for Learning Rate eta = 0.6.
#	So, Learning Rate = 0.6
#	For test case no. 1 the output varies. So there are two sets of answers: 1 0 1 1 ... and ... 0 0 1 1

from numpy import genfromtxt
from numpy import savetxt
import random
import math

data = genfromtxt('data6.csv', delimiter=',')	#data from 'data6.csv' is stored in 'data'
test = genfromtxt('test6.csv', delimiter=',')	#data from 'test6.csv' is stored in 'test'

w = [0,0,0,0,0,0,0,0]	#to store w1, w2, ... , w8

for i in range(8):
	w[i] = random.uniform(0,1)	#initialising wi as a random value between 0 and 1

w0 = random.uniform(0,1)	#initialising w0 as a random value between 0 and 1

#print(w)

def activation(data,w,j,w0):	#z = w0 + w1x1 + w2x2 + ... + w8x8
	sum=w0
	for i in range(8):
		sum = sum + data[j][i]*w[i]
	return(sum)

def sigmoid(z):					#F(z) = 1/(1+ep(-z))
	temp = 1/(1 + math.exp(-z))
	return(temp)

def delta(data,w,i,w0):			#delW = eta*sum((ti - F(z))*F(z)*(1-F(z))*xi
	sum=0
	for j in range(20):
		temp = 0;
		z = activation(data,w,j,w0)
		Fz = sigmoid(z)
		temp = (data[j][8]-Fz)*Fz*(1-Fz)*data[j][i]
		sum = sum + temp
	sum = sum * 0.6
	return(sum)

t=10			#10 epochs
while(t>0):
	deltaW = [0,0,0,0,0,0,0,0]	#stores delWi
	deltaW0 = 0					#stores delW0
	for i in range(20):
		temp = 0;
		z = activation(data,w,i,w0)
		Fz = sigmoid(z)
		temp = (data[i][8]-Fz)*Fz*(1-Fz)
		deltaW0 = deltaW0 + temp
	deltW0 = deltaW0*0.5
	
	for i in range(8):			
		deltaW[i] = delta(data,w,i,w0)
	
	for i in range(8):			#Wi = Wi + delWi
		w[i] = w[i] + deltaW[i]
	
	w0 = w0 + deltaW0			#W0 = W0 + delW0
	
	t = t-1

count=0
for i in range(20):
	z = activation(data,w,i,w0)
	Fz = sigmoid(z)
	#print(z, end=" ")
	#print(Fz, end=	" ")
	if(Fz>0.5): x=1
	else: x=0
	#print(x, end=" ")
	if x == data[i][8]: count = count + 1

#print(count)		#for accuracy

out = [0,0,0,0]		#to store output

for i in range(4):	#if sigmoid(z)>0.5 then o/p = 1 else o/p = 0
	z = activation(test,w,i,w0)
	Fz = sigmoid(z)
	if Fz>0.5: out[i] = 1
	else: out[i] = 0
	print(out[i], end=" ")
	
savetxt('output.out', out, fmt='%d', delimiter=',') 	#save o/p to '14CS30009_6.out'
#print(w)
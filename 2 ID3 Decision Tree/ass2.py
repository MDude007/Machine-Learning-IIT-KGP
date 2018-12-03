# Specificaations : Works for input files (data2.csv and test2.csv) with same number of rows and cols



import csv
import math

filename = "data2.csv"

def readcsv(filename):	
    ifile = open(filename, "rU")
    reader = csv.reader(ifile, delimiter=";")

    rownum = 0	
    a = []

    for row in reader:
        a.append (row)
        rownum += 1
    
    ifile.close()
    return a


temp=readcsv(filename)

data = [[1,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]

i=0
for row in temp:
	j=0
	for col in row:
		while j<17:
			data[i][j/2] = col[j]
			j=j+2
		i=i+1

def log2(a):
	if a>0: return math.log(a,2)
	else: return 0

def entropy1(a,b):
	if a>0 or b>0:
		ma = float(a)/float((a+b))
		mb = float(b)/float((a+b))
		a = log2(ma)
		b = log2(mb)
		pa = -ma
		pb = -mb
		E = (pa*a) + (pb*b)
		return E
	else: return 0


def entropy2(a,b,c,d):
	if a>0 or b>0 or c>0 or d>0:
		total = a + b + c + d
		E1 = float(a+b)/float(total)
		E2 = float(c+d)/float(total)
		E1 *= entropy1(a,b)
		E2 *= entropy1(c,d)
		E = E1 + E2
		return E
	else: return 0

def infogain(a,b):
	return (a-b)


dtroot = -1
dtn = 0
result0 = [-1,-1,-1,-1,-1,-1,-1,-1]
result1 = [-1,-1,-1,-1,-1,-1,-1,-1]
branch0 = [-1,-1,-1,-1,-1,-1,-1,-1]
branch1 = [-1,-1,-1,-1,-1,-1,-1,-1]

a=b=entr=0

for i in range(24):
	if data[i][8] == "1": a=a+1
	else: b=b+1

entr = entropy1(a,b)


gain = [0,0,0,0,0,0,0,0]
	
for j in range(8):
	a=b=c=d=0
	for i in range(24):
		if data[i][j] == '1':
			if data[i][8] == '0': a=a+1
			else: b=b+1
		else:
			if data[i][8] == '0': c=c+1
			else: d=d+1
	E = entropy2(a,b,c,d)
	gain[j] = infogain(entr,E)

maxgain = 0
maxind = -1

for i in range(8):
	if gain[i]>maxgain:
		maxgain = gain[i]
		maxind = i

gain[maxind] = -1

dtroot = maxind

a=b=c=d=e=f=0
for i in range(24):
	if data[i][maxind] == '0':
		if data[i][8] == '0': a=a+1
		else: b=b+1
		e=1
	else:
		if data[i][8] == '0': c=c+1
		else: d=d+1
		f=1

dtn = dtn+1

if a==0 and e!=0: result0[maxind] = 1
elif b==0 and e!=0: result0[maxind] = 0
if c==0 and f!=0: result1[maxind] = 1
elif d==0 and f!=0: result1[maxind] = 0



change = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
changen = 0

left = -1
right = -1

if result0[maxind] != -1 and result1[maxind] == -1:
	for i in range(24):
		if data[i][maxind] == '0':
			change[i] = 1
			changen = changen + 1
			right = maxind
elif result1[maxind] != -1 and result0[maxind] == -1:
	for i in range(24):
		if data[i][maxind] == '1':
			change[i] = 1
			changen = changen + 1
			left = maxind
elif result0[maxind] != -1 and result1[maxind] != -1:
	for i in range(24):
		change[i] = 1
		changen = changen + 1
else:
	left = maxind
	right = maxind






def formtree(changen, change, left, right, data, dtn, branch0, branch1, result0, result1, gain):
	if changen<24:
		if left!=-1 and right!=-1:
			
			a=b=entr=0

			for i in range(24):
				if change[i] == 0 and data[i][left] == "0":
					if data[i][8] == "1": a=a+1
					else: b=b+1
			entr = entropy1(a,b)

			for j in range(8):
				a=b=c=d=0
				for i in range(24):
					if change[i] == 0 and data[i][left] == "0":
						if data[i][j] == '1':
							if data[i][8] == '0': a=a+1
							else: b=b+1
						else:
							if data[i][8] == '0': c=c+1
							else: d=d+1
				E = entropy2(a,b,c,d)
				if gain[j] != -1:
					gain[j] = infogain(entr,E)

			maxgain = 0
			maxind = -1

			for i in range(8):
				if gain[i]>maxgain:
					maxgain = gain[i]
					maxind = i

			gain[maxind] = -1
			a=b=c=d=e=f=0
			for i in range(24):
				if data[i][maxind] == '0'and change[i] == 0 and data[i][left] == '0':
					if data[i][8] == '0': a=a+1
					else: b=b+1
					e=1
				elif data[i][maxind] == '1' and change[i] == 0 and data[i][left] == '0':
					if data[i][8] == '0': c=c+1
					else: d=d+1
					f=1

			dtn = dtn+1

			branch0[left] = maxind

			left1 = right1 = -1

			if a==0 and e!=0: result0[maxind] = 1
			elif b==0 and e!=0: result0[maxind] = 0
			if c==0 and f!=0: result1[maxind] = 1
			elif d==0 and f!=0: result1[maxind] = 0

			changetemp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			changetempn = changen

			for i in range(24):
				changetemp[i] = change[i]

			if result0[maxind] != -1 and result1[maxind] == -1:
				for i in range(24):
					if data[i][maxind] == '0':
						if changetemp[i] == 0:
							changetemp[i] = 1
							changetempn = changetempn + 1
						right1 = maxind
			elif result1[maxind] != -1 and result0[maxind] == -1:
				for i in range(24):
					if data[i][maxind] == '1':
						if changetemp[i] == 0:
							changetemp[i] = 1
							changetempn = changetempn + 1
						left1 = maxind
			elif result0[maxind] != -1 and result1[maxind] != -1:
				for i in range(24):
					changetemp[i] = 1
					changetempn = changetempn + 1
			else:
				left1 = maxind
				right1 = maxind

			
			formtree(changetempn, changetemp, left1, right1, data, dtn, branch0, branch1, result0, result1, gain)


			a=b=entr=0
			for i in range(24):
				if change[i] == 0 and data[i][left] == "1":
					if data[i][8] == "1": a=a+1
					else: b=b+1
			
			entr = entropy1(a,b)


			for j in range(8):
				a=b=c=d=0
				for i in range(24):
					if change[i] == 0 and data[i][left] == "1":
						if data[i][j] == '1':
							if data[i][8] == '0': a=a+1
							else: b=b+1
						else:
							if data[i][8] == '0': c=c+1
							else: d=d+1
			E = entropy2(a,b,c,d)
			if gain[j] != -1:
				gain[j] = infogain(entr,E)

			maxgain = 0
			maxind = -1

			for i in range(8):
				if gain[i]>maxgain:
					maxgain = gain[i]
					maxind = i

			gain[maxind] = -1

			a=b=c=d=e=f=0
			for i in range(24):
				if data[i][maxind] == '0' and change[i] == 0 and data[i][left] == '0':
					if data[i][8] == '0': a=a+1
					else: b=b+1
					e=1
				elif data[i][maxind] == '1' and change[i] == 0 and data[i][left] == '0':
					if data[i][8] == '0': c=c+1
					else: d=d+1
					f=1

			dtn = dtn+1

			branch1[left] = maxind

			left1 = right1 = -1

			if a==0 and e!=0: result0[maxind] = 1
			elif b==0 and e!=0: result0[maxind] = 0
			if c==0 and f!=0: result1[maxind] = 1
			elif d==0 and f!=0: result1[maxind] = 0

			changetemp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			changetempn = changen

			for i in range(24):
				changetemp[i] = change[i]


			if result0[maxind] != -1 and result1[maxind] == -1:
				for i in range(24):
					if data[i][maxind] == '0':
						if changetemp[i] == 0:
							changetemp[i] = 1
							changetempn = changetempn + 1
						right1 = maxind
			elif result1[maxind] != -1 and result0[maxind] == -1:
				for i in range(24):
					if data[i][maxind] == '1':
						if changetemp[i] == 0:
							changetemp[i] = 1
							changetempn = changetempn + 1
						left1 = maxind
			elif result0[maxind] != -1 and result1[maxind] != -1:
				for i in range(24):
					changetemp[i] = 1
					changetempn = changetempn + 1
			else:
				left1 = maxind
				right1 = maxind


			formtree(changetempn, changetemp, left1, right1, data, dtn, branch0, branch1, result0, result1, gain)

			for i in range(24):
				change[i] = changetemp[i]

			changen = changetempn

		elif (left!=-1 and right==-1) or (left==-1 and right!=-1):

			a=b=entr=0

			for i in range(24):
				if change[i] == 0:
					if data[i][8] == "1": a=a+1
					else: b=b+1
			entr = entropy1(a,b)

			for j in range(8):
				a=b=c=d=0
				for i in range(24):
					if change[i] == 0:
						if data[i][j] == '1':
							if data[i][8] == '0': a=a+1
							else: b=b+1
						else:
							if data[i][8] == '0': c=c+1
							else: d=d+1
				E = entropy2(a,b,c,d)
				if gain[j] != -1:
					gain[j] = infogain(entr,E)


			maxgain = 0
			maxind = -1

			for i in range(8):
				if gain[i]>maxgain:
					maxgain = gain[i]
					maxind = i

			gain[maxind] = -1


			a=b=c=d=e=f=0
			for i in range(24):
				if data[i][maxind] == '0' and change[i] == 0:
					if data[i][8] == '0': a=a+1
					else: b=b+1
					e=1
				elif data[i][maxind] == '1' and change[i] == 0:
					if data[i][8] == '0': c=c+1
					else: d=d+1
					f=1

			dtn = dtn+1

			if left != -1 and right == -1: branch0[left] = maxind
			elif left == -1 and right != -1: branch1[right] = maxind

			left = right = -1


			if a==0 and e!=0: result0[maxind] = 1
			elif b==0 and e!=0: result0[maxind] = 0
			if c==0 and f!=0: result1[maxind] = 1
			elif d==0 and f!=0: result1[maxind] = 0



			if result0[maxind] != -1 and result1[maxind] == -1:
				for i in range(24):
					if data[i][maxind] == '0':
						if change[i] == 0:
							change[i] = 1
							changen = changen + 1
						right = maxind
			elif result1[maxind] != -1 and result0[maxind] == -1:
				for i in range(24):
					if data[i][maxind] == '1':
						if change[i] == 0:
							change[i] = 1
							changen = changen + 1
						left = maxind
			elif result0[maxind] != -1 and result1[maxind] != -1:
				for i in range(24):
					change[i] = 1
					changen = changen + 1
			else:
				left = maxind
				right = maxind


			formtree(changen, change, left, right, data, dtn, branch0, branch1, result0, result1, gain)


formtree(changen, change, left, right, data, dtn, branch0, branch1, result0, result1, gain)



#print branch0
#print branch1

#print result0
#print result1


#print dtroot
	
filename = "test2.csv"
temp=readcsv(filename)

test = [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]

i=0
for row in temp:
	j=0
	for col in row:
		while j<15:
			test[i][j/2] = col[j]
			j=j+2
		i=i+1


for i in range(4):
	flag = 0
	current = dtroot
	while flag == 0:
		if test[i][current] == '0':
			if result0[current] != -1:
				print result0[current],
				flag = 1
			else: current = branch0[current]
		elif test[i][current] == '1':
			if result1[current] != -1:
				print result1[current],
				flag = 1
			else: current = branch1[current]



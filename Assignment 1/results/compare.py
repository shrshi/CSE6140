f1 = open("/home/shruti/Documents/Academics_GT/CSE6140/Assignment 1/results/rmat0709.out", "r")
f2 = open("/home/shruti/Documents/Academics_GT/CSE6140/Assignment 1/results/rmat0709_output.txt", "r")
f1lst = list()
f2lst = list()
for line in f1:
	lst = line.split()
	f1lst.append(float(lst[0]))
for line in f2:
	lst = line.split()
	f2lst.append(float(lst[0]))

if len(f1lst)!=len(f2lst):
	print 'length not matching'
else:
	for i in range(len(f1lst)):
		if f1lst[i]!=f2lst[i]:
			print i, f1lst[i], f2lst[i]
			break

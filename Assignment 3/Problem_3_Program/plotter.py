import matplotlib.pyplot as plt

y_dc = []
y_dp = []
x = []
for op in range(10):
	f = open("output/sshivakumar9_output_dc_" + str((op+1)*1000) + ".txt", "r")
	x.append((op+1)*1000)
	s=0.0
	num=0
	for line in f:
		lst = line.split(",")
		s = s + float(lst[3])
		num = num + 1
	y_dc.append(s/num)
	f.close()

for op in range(10):
	f = open("output/sshivakumar9_output_dp_" + str((op+1)*1000) + ".txt", "r")
	# x.append((op+1)*1000)
	s=0.0
	num=0
	for line in f:
		lst = line.split(",")
		s = s + float(lst[3])
		num = num + 1
	y_dp.append(s/num)
	f.close()

plt.plot(x, y_dc, 'b--')
plt.plot(x, y_dp, 'r--')
plt.xlabel('Array length')
plt.ylabel('Time taken')	
plt.legend(['Divide and Conquer', 'Dynamic Programming'], loc='upper left')
# plt.title('Plot of time taken to compute maximum sum subarray using both approaches')
plt.show()
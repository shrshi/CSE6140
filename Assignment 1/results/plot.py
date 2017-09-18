import matplotlib.pyplot as plt
import subprocess, os

x = [], y_static = [], y_dynamic = []
output = subprocess.check_output("./plot_helper.sh")

lines = output.splitlines()
for num, line in enumerate(lines):
	if num<13:
		x.append(line)
		del lines[num]

for f in range(len(13)):
	s = 0.0
	for num, line in enumerate(lines):
		if num==0:
			y_static.append(lines[num])
		elif num!=0 and num<1001:
			s = s + line
	y_dynamic.append(s)
	del lines[0:1000]

plt.plot(x, y_static, 'b', label='Static computation', x, y_dynamic, 'g', label='Dynamic computation')
plt.xlabel('Number of edges')
plt.ylabel('Time taken')		

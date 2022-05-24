import matplotlib.pyplot as plt
import numpy as np


file = open("textile.txt", "r")
lines = file.readlines()
t = 0

sensor1 = []
sensor2 = []

for line in lines:
    
    if(line[0] != 't'):
        s1, s2 = line.split(',')
        sensor1.append(s1)
        sensor2.append(s2)
    else:
        t = int(float(line[6:-1]))
file.close()

T = np.arange(0, t, t/len(sensor1))

sensor1 = [int(s1) for s1 in sensor1]
sensor2 = [int(s2) for s2 in sensor2]

line1, = plt.plot(T, sensor1, label="Sensor1")
line2, = plt.plot(T[:], sensor2, label="Sensor2")
plt.legend(handles=[line1, line2])
plt.ylabel("Angle(degree)")
plt.xlabel("time(s)")
plt.title("Angle variations based on time")
plt.grid()
plt.savefig("perfect2.png")



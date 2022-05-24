import matplotlib.pyplot as plt
import numpy as np


file1 = open("neck.txt", "r")
lines = file1.readlines()
neck_yaw = []

for line in lines:
    
    if(line[0] != 't'):
        neck_yaw.append(float(line))
file1.close()

file2 = open("back.txt", "r")
lines = file2.readlines()
back_yaw = []
t = 0

for line in lines:
    
    if(line[0] != 't'):
        back_yaw.append(float(line))
    else:
        t = int(float(line[6:-1]))

file2.close()

x1 = len(neck_yaw)
x2 = len(back_yaw)

x = min(x1, x2)

X = np.arange(x)
T = np.arange(0, t, t/x)


line1, = plt.plot(T[:], neck_yaw[:x], label="Sensor1")
line2, = plt.plot(T[:], back_yaw[:x], label="Sensor2")
plt.legend(handles=[line1, line2])
plt.ylabel("Angle(degree)")
plt.xlabel("time(s)")
plt.title("Angle variations based on time")
plt.grid()
plt.savefig("perfect.png")


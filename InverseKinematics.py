import pdb
from math import radians, sin, cos, degrees, atan2, sqrt, pi

#x, y, z, O, A ,T
inputs = []
#Used to store radian value of OAT angle
OAT = []
xyz = []
c = []
s = []

theta1 = []
theta2 = []
theta3 = []
theta4 = []
theta5 = []
theta6 = []

for i in range(:3):
	xyz.append((inputs[i]))
for i in range(3:6):
	OAT.append(radiands(inputs[i]))
for i in OAT:
	c.append(cos(i))
	s.append(sin(i))

a = [0, 0, 650, 0, 0, 0]
d = [0, 0, 191, 600, 0, 0]

r11 = -1 * (c[0]*s[2] - s[0]*s[1]*c[2])
r12 = -1 * (c[0]*c[2] + s[0]*s[1]*s[3])
r13 = s[0]*c[1]
r21 = -1 * (s[0]*s[2] + c[0]*s[1]*c[2])
r22 = -1 * (s[0]*c[2] - c[0]*s[1]*s[3])
r23 = -1 * c[0]*c[1]
r31 = -1 * c[1]*c[2] 
r32 = -1 * c[1]*s[2]
r33 = -1 * s[1]
px = -125 * r13 + xyz[0]
py = -125 * r23 + xyz[1]
pz = -125 * r33 + xyz[2]

theta1.append(atan2(py, px) - atan2(d[2], sqrt(px*px + py*py - d[2]*d[2])))
theta1.append(atan2(py, px) - atan2(d[2], -1 * sqrt(px*px + py*py - d[2]*d[2])))

K = (px*px + py*py + pz*pz - a[2]*a[2] - a[3]*a[3] - d[2]*d[2]-d[3]*d[3])/(2*a[2])

theta3.append(atan2(a[3], d[3]) - atan2(K, sqrt(a[3]*a[3] + d[3]*d[3]-K*K)))
theta3.append(atan2(a[3], d[3]) - atan2(K, -1 * sqrt(a[3]*a[3] + d[3]*d[3]-K*K)))

s23 =  ((-1 * a[3] - (a[2]*c[2]))*pz + (c[0]*px + s[0]*py)*(a[2]*s[2] - d[3]))/(pz*pz + (c[0]*px + s[0]*py)*(c[0]*px + s[0]*py))
c23 = ((a[2]*s[2] - d[3])*pz + (a[3]+a[2]*c[2])*(c[0]*px + s[0]*py))/(pz*pz + (c[0]*px + s[0]*py)*(c[0]*px + s[0]*py))

theta23 = atan2((-1*a[3] - a[2]*c[2])*pz - (c[0]*px + s[0]*py)*(d[3] - a[2]*s[2]), (a[2]*s[2] - d[3])*pz + (a[3]+a[2]*c[2])*(c[0]*px+s[0]*py))

theta2.append(theta23 - theta3[0])
theta2.append(theta23 - theta3[1])










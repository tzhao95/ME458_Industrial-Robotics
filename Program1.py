import pdb
from math import radians, sin, cos, degrees, atan2, sqrt
import numpy

t = [23.384, -120.843, 55.109, 38.498, -35.697, 33.023]
radinputs = []
c = []
s = []

a = [0, 0, 650, 0, 0, 0]
d = [0, 0, 191, 600, 0, 0]

for i in range(6):
	#t.append(float(input("Enter theta %d: " %(i+1) )))
	radinputs.append(radians(t[i]))
	c.append(cos(radinputs[i]))
	s.append(sin(radinputs[i]))

c23 = c[1]*c[2] - s[1]*s[2]
s23 = c[1]*s[2] + s[1]*c[2]

r11 = c[0]*(c23*(c[3]*c[4]*c[5] - s[3]*s[5]) - s23*s[4]*c[5]) + s[0]*(s[3]*c[4]*c[5] + c[3]*s[5])
r21 = s[0]*(c23*(c[3]*c[4]*c[5] - s[3]*s[5]) - s23*s[4]*c[5]) - c[0]*(s[3]*c[4]*c[5] + c[3]*s[5])
r31 = -1*s23*(c[3]*c[4]*c[5] - s[3]*s[5]) - c23*s[4]*c[5]

r12 = c[0]*(c23*(-1*c[3]*c[4]*s[5] - s[3]*c[5]) + s23*s[4]*s[5]) + s[0]*(c[3]*c[5] - s[3]*c[4]*s[5])
r22 = s[0]*(c23*(-1*c[3]*c[4]*s[5] - s[3]*c[5]) - s23*s[4]*s[5]) - c[0]*(c[3]*c[5] - s[3]*c[4]*s[5])
r32 = -1*s23*(-1*c[3]*c[4]*s[5] - s[3]*c[5]) + c23*s[4]*s[5]

r13 = -1*c[0]*(c23*c[3]*s[4] + s23*c[4]) - s[0]*s[3]*s[4]
r23 = -1*s[0]*(c23*c[3]*s[4] + s23*c[4]) + c[0]*s[3]*s[4]
r33 = s23*c[3]*s[4] - c23*c[4]

A = atan2(-r33, sqrt(r31*r31 + r32*r32))
T = atan2(r32/cos(A), -r31/cos(A))
O = atan2(r13/cos(A), -r23/cos(A))

px = c[0]*(a[1]*c[1] + a[2]*c23 - d[3]*s23) - d[2]*s[0]
py = s[0]*(a[1]*c[1] + a[2]*c23 - d[3]*s23) + d[2]*c[0]
pz = -1*a[2]*s23 - a[1]*s[1] - d[3]*c23

print(px)
print(py)
print(pz)
print(degrees(O))
print(degrees(A))
print(degrees(T))
#rx = [degrees(r11), degrees(r21), degrees(r31)]
#ry = [degrees(r12), degrees(r22), degrees(r32)]
#rz = [degrees(r13), degrees(r23), degrees(r33)]

#print(rx)
#print(ry)
#print(rz)

#RESULTS
# x 		y			z		O		A 		T
#-972.196, -261.754, 794.344, -45.242, 4.735, -112.266

#c23 = cos(radinputs[1])*cos(radinputs[2]) - sin(radinputs[1])*sin(radinputs[2])
#s23 = cos(radinputs[1])*sin(radinputs[2]) + sin(radinputs[1])*sin(radinputs[2])

#r11 = cos(radinputs[0]*(cos(c23)*(cos(radinputs[3])*cos(radinputs[4])*cos(radinputs[5]) - sin(radinputs[3])*sin(radinputs[5])) - s23*sin(radinputs[4])*sin(radinputs[5])) + sin(radinputs[0])*(sin(radinputs[3])*cos(radinputs[4])*sin(radinputs[5]) + cos(radinputs[3])*sin(radinputs[5]))


'''
t1 = float(input("Enter theta1: "))
t2 = float(input("Enter theta2: "))
t3 = float(input("Enter theta3: "))
t4 = float(input("Enter theta4: "))
t5 = float(input("Enter theta5: "))
t6 = float(input("Enter theta6: "))
'''


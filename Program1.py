import pdb
from math import radians, sin, cos, degrees, atan2, sqrt, pi
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

t[2] = t[2]
radinputs[2] = radians(t[2]) - pi
c[2] = cos(radinputs[2])
s[2] = sin(radinputs[2])

c23 = c[1]*c[2] - s[1]*s[2]
s23 = c[1]*s[2] + s[1]*c[2]

r11 = c[0]*(c23*(c[3]*c[4]*c[5] - s[3]*s[5]) - s23*s[4]*c[5]) + s[0]*(s[3]*c[4]*c[5] + c[3]*s[5])
r21 = s[0]*(c23*(c[3]*c[4]*c[5] - s[3]*s[5]) - s23*s[4]*c[5]) - c[0]*(s[3]*c[4]*c[5] + c[3]*s[5])
r31 = -1*s23*(c[3]*c[4]*c[5] - s[3]*s[5]) - c23*s[4]*c[5]

r12 = c[0]*(c23*(-1*c[3]*c[4]*s[5] - s[3]*c[5]) + s23*s[4]*s[5]) + s[0]*(c[3]*c[5] - s[3]*c[4]*s[5])
r22 = s[0]*(c23*(-1*c[3]*c[4]*s[5] - s[3]*c[5]) + s23*s[4]*s[5]) - c[0]*(c[3]*c[5] - s[3]*c[4]*s[5])
r32 = -1*s23*(-1*c[3]*c[4]*s[5] - s[3]*c[5]) + c23*s[4]*s[5]

r13 = -1*c[0]*(c23*c[3]*s[4] + s23*c[4]) - s[0]*s[3]*s[4]
r23 = -1*s[0]*(c23*c[3]*s[4] + s23*c[4]) + c[0]*s[3]*s[4]
r33 = s23*c[3]*s[4] - c23*c[4]



px = c[0]*(a[2]*c[1] + a[3]*c23 - d[3]*s23) - d[2]*s[0]
py = s[0]*(a[2]*c[1] + a[3]*c23 - d[3]*s23) + d[2]*c[0]
pz = -1*a[3]*s23 - a[2]*s[1] - d[3]*c23
'''
px = c[0]*(650*c[1] + 0*c23 - 600*s23) - 191*s[0]
py = s[0]*(650*c[1] + 0*c23 - 600*s23) + 191*c[0]
pz = -1*0*s23 - 650*s[1] - 600*c23
'''
WT = [[-r11, -r12, r13, 125*r13+px],
		[-r21, -r22, r23, 125*r23+py],
		[-r31, -r32, r33, 125*r33+pz],
		[0, 0, 0, 1]]
#WT = [[1, 2, 3],
#		[4, 5, 6]]

A = atan2(-WT[2][2], sqrt(WT[2][0]*WT[2][0] + WT[2][1]*WT[2][1]))


if A == 90: 
	T = 0
	O = atan2(-WT[0][0], WT[0][1])
elif A == -90:
	T = 0
	O = atan2(WT[0][0], WT[0][1])
else:
	T = atan2(WT[2][1]/cos(A), -WT[2][0]/cos(A))
	O = atan2(WT[0][2]/cos(A), -WT[1][2]/cos(A))



print('x =', WT[0][3])
print('y =', WT[1][3])
print('z =', WT[2][3])
print('O =', degrees(O))
print('A =', degrees(A))
print('T =', degrees(T))


#RESULTS
# x 		y			z		O		A 		T
#-972.196, -261.754, 794.344, -45.242, 4.735, -112.266

#c23 = cos(radinputs[1])*cos(radinputs[2]) - sin(radinputs[1])*sin(radinputs[2])
#s23 = cos(radinputs[1])*sin(radinputs[2]) + sin(radinputs[1])*sin(radinputs[2])

#r11 = cos(radinputs[0]*(cos(c23)*(cos(radinputs[3])*cos(radinputs[4])*cos(radinputs[5]) - sin(radinputs[3])*sin(radinputs[5])) - s23*sin(radinputs[4])*sin(radinputs[5])) + sin(radinputs[0])*(sin(radinputs[3])*cos(radinputs[4])*sin(radinputs[5]) + cos(radinputs[3])*sin(radinputs[5]))




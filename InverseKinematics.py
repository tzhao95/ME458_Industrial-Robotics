import pdb
from math import radians, sin, cos, degrees, atan2, sqrt, pi

#x, y, z, O, A ,T
#inputs = [-972.2000, -261.760, 794.338, -45.241, 4.735, -112.266]
inputs = [648.175, 362.614, 1111.597, 112.232, -17.655, 46.079]
#Used to store radian value of OAT angle
OAT = []
xyz = []
cOAT = []
sOAT = []
c = []
s = []

theta1 = []
theta2 = []
theta3 = []
theta4 = []
theta5 = []
theta6 = []

for i in range(3):
	xyz.append((inputs[i]))
for i in range(3,6):
	OAT.append(radians(inputs[i]))
for i in OAT:
	cOAT.append(cos(i))
	sOAT.append(sin(i))

a = [0, 0, 650, 0, 0, 0]
d = [0, 0, 191, 600, 0, 0]

r11 = -1 * (cOAT[0]*sOAT[2] - sOAT[0]*sOAT[1]*cOAT[2])
r12 = -1 * (cOAT[0]*cOAT[2] + sOAT[0]*sOAT[1]*sOAT[2])
r13 = sOAT[0]*cOAT[1]
r21 = -1 * (sOAT[0]*sOAT[2] + cOAT[0]*sOAT[1]*cOAT[2])
r22 = -1 * (sOAT[0]*cOAT[2] - cOAT[0]*sOAT[1]*sOAT[2])
r23 = -1 * cOAT[0]*cOAT[1]
r31 = -1 * cOAT[1]*cOAT[2] 
r32 = -1 * cOAT[1]*sOAT[2]
r33 = -1 * sOAT[1]
px = -125 * r13 + xyz[0]
py = -125 * r23 + xyz[1]
pz = -125 * r33 + xyz[2]

def s23(t1, t3):
	return ((((-a[3] - (a[2]*cos(radians(t3))))*pz + (cos(radians(t1))*px + sin(radians(t1))*py)*(a[2]*sin(radians(t3)) - d[3]))/(pz*pz + (cos(radians(t1))*px + sin(radians(t1))*py)**2)))

def c23(t1, t3):
	return ((a[2]*sin(radians(t3)) - d[3])*pz + (a[3]+a[2]*cos(radians(t3)))*(cos(radians(t1))*px + sin(radians(t1))*py))/(pz*pz + (cos(radians(t1))*px + sin(radians(t1))*py)**2)

def t23(t1, t3):
	return degrees(atan2((-1*a[3] - a[2]*cos(radians(t3))*pz - (cos(radians(t1))*px + sin(radians(t1))*py)*(d[3] - a[2]*sin(radians(t3)))), (a[2]*sin(radians(t3)) - d[3])*pz + (a[3]+a[2]*cos(radians(t3)))*(cos(radians(t1))*px+sin(radians(t1))*py)))

def t4(t1, t3):
	return degrees(atan2(-r13*sin(radians(t1)) + r23*cos(radians(t1)), -r13*cos(radians(t1))*c23(t1,t3) - r23*sin(radians(t1))*c23(t1,t3) + r33*s23(t1,t3)))

def t5(t1, t3, t4):
	s5 = -1 * r13*(cos(radians(t1)) * c23(t1,t3) * cos(radians(t4)) + sin(radians(t1))*sin(radians(t4))) + r23*(sin(radians(t1))*c23(t1, t3) * cos(radians(t4)) - cos(radians(t1))*sin(radians(t4))) - r33*(s23(t1, t3) * cos(radians(t4)))
	c5 = r13*(-cos(radians(t1))*s23(t1, t3)) + r23*(-sin(radians(t1))*s23(t1, t3)) + r33*(-c23(t1,t3))
	return degrees(atan2(s5, c5))

def t6(t1, t3, t4, t5):
	s6 = -r11*(cos(radians(t1))*c23(t1, t3)*sin(radians(t4)) - sin(radians(t1))*cos(radians(t4))) - r21*(sin(radians(t1))*c23(t1, t3)*sin(radians(t4)) + cos(radians(t1))*cos(radians(t4))) + r31*(s23(t1, t3)*sin(radians(t4)))
	c6 = r11*((cos(radians(t1))*c23(t1, t3)*sin(radians(t4)) + sin(radians(t1))*sin(radians(t4)))*cos(radians(t5)) - cos(radians(t1))*s23(t1, t3)*sin(radians(t5))) + r21*((sin(radians(t1))*c23(t1,t3)*cos(radians(t4)) - cos(radians(t1))*sin(radians(t4)))*cos(radians(t5)) - sin(radians(t1))*s23(t1, t3)*sin(radians(t5))) - r31(s23(t1,t3)*cos(radians(t4))*cos(radians(t5)) + c23(t1, t3)*sin(radians(t5)))
'''
print('r11 = ', r11)
print('r12 = ', r12)
print('r13 = ', r13)
print('r21 = ', r21)
print('r22 = ', r22)
print('r23 = ', r23)
print('r31 = ', r31)
print('r32 = ', r32)
print('r33 = ', r33)
print('px = ', px)
print('py = ', py)
print('pz = ', pz)
'''

#t1 = degrees(atan2(317.5468, 537.917) - atan2(191, sqrt(317.5468*317.5468 + 537.917*537.917 - 191*191)))
theta1.append(degrees(atan2(py, px) - atan2(d[2], sqrt(px*px + py*py - d[2]*d[2]))))
theta1.append(degrees(atan2(py, px) - atan2(d[2], -1 * sqrt(px*px + py*py - d[2]*d[2]))))
#print('t1 = ', t1)
print(theta1)

c1 = cos(radians(theta1[0]))
s1 = sin(radians(theta1[0]))

K = (px*px + py*py + pz*pz - a[2]*a[2] - a[3]*a[3] - d[2]*d[2]-d[3]*d[3])/(2*a[2])
print(K)

theta3.append(degrees(atan2(a[3], d[3]) - atan2(K, sqrt(a[3]*a[3] + d[3]*d[3]-K*K))))
theta3.append(degrees(atan2(a[3], d[3]) - atan2(K, -1 * sqrt(a[3]*a[3] + d[3]*d[3]-K*K))))

print(theta3)
'''
c3 = cos(radians(-theta3[1]))
s3 = sin(radians(-theta3[1]))
'''
theta2.append(t23(theta1[0], theta3[0]) - theta3[0])
theta2.append(t23(theta1[1], theta3[0]) - theta3[0])
theta2.append(t23(theta1[0], theta3[1]) - theta3[1])
theta2.append(t23(theta1[1], theta3[1]) - theta3[1])

print(theta2)

theta4.append(t4(theta1[0], theta3[0]))
theta4.append(t4(theta1[1], theta3[0]))
theta4.append(t4(theta1[0], theta3[1]))
theta4.append(t4(theta1[1], theta3[1]))

print(theta4)

theta5.append(t5(theta1[0], theta3[0], theta4[0]))
theta5.append(t5(theta1[1], theta3[0], theta4[1]))
theta5.append(t5(theta1[0], theta3[1], theta4[2]))
theta5.append(t5(theta1[1], theta3[1], theta4[3]))
theta5.append(t5(theta1[0], theta3[0], theta4[0]))
theta5.append(t5(theta1[0], theta3[0], theta4[0]))
theta5.append(t5(theta1[0], theta3[0], theta4[0]))
theta5.append(t5(theta1[0], theta3[0], theta4[0]))
print(theta5)

'''
s23 =  ((-a[3] - (a[2]*c3))*pz + (c1*px + s1*py)*(a[2]*s3 - d[3]))/(pz*pz + (c1*px + s1*py)*(c1*px + s1*py))
c23 = ((a[2]*s3 - d[3])*pz + (a[3]+a[2]*c3)*(c1*px + s1*py))/(pz*pz + (c1*px + s1*py)*(c1*px + s1*py))
'''
'''
theta23 = degrees(atan2((-1*a[3] - a[2]*c3)*pz - (c1*px + s1*py)*(d[3] - a[2]*s3), (a[2]*s3 - d[3])*pz + (a[3]+a[2]*c3)*(c1*px+s1*py)))

theta2.append(theta23 - theta3[0])
theta2.append(theta23 - theta3[1])

print(theta2)

'''
'''
theta4.append(degrees(atan2(-r12*s1 + r23*c1, -r12*c1*c23 - r23*s1*c23 + r33*s23)))

print(theta4)


'''

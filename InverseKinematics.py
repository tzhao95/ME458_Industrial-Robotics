import pdb
from math import radians, sin, cos, degrees, atan2, sqrt, pi

#x, y, z, O, A ,T
#inputs = [-972.2000, -261.760, 794.338, -45.241, 4.735, -112.266] This data is bad
#inputs = [648.175, 362.614, 1111.597, 112.232, -17.655, 46.079] #2
#inputs = [879.737, 414.591, 908.843, 101.208, -5.418, -65.169] #3
#inputs = [295.607, -66.719, 1079.214, 38.285, -4.447, 14.899] #4


#results 2 = [12.749, -71.495, 111.84, 16.799, 32.899, 34.755]
#results 3 = 14.311, -58.746, 114.069, -6.303, 29.399, -59.966
#results 4 = -51.872, -113.440, 151.385, 4.832, 47.600, 14.767
#Used to store radian value of OAT angle

inputs = []
inputs.append(float(input("Enter X: ")))
inputs.append(float(input("Enter Y: ")))
inputs.append(float(input("Enter Z: ")))
inputs.append(float(input("Enter O: ")))
inputs.append(float(input("Enter A: ")))
inputs.append(float(input("Enter T: ")))

OAT = []
xyz = []
cOAT = []
sOAT = []
c = []
s = []
#s6temp = []
#c6temp = []
#s23temp = []
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
r31 =  cOAT[1]*cOAT[2] 
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
	s5 = -1 * (r13*(cos(radians(t1)) * c23(t1,t3) * cos(radians(t4)) + sin(radians(t1))*sin(radians(t4))) + r23*(sin(radians(t1))*c23(t1, t3) * cos(radians(t4)) - cos(radians(t1))*sin(radians(t4))) - r33*(s23(t1, t3) * cos(radians(t4))))
	c5 = r13*(-cos(radians(t1))*s23(t1, t3)) + r23*(-sin(radians(t1))*s23(t1, t3)) + r33*(-c23(t1,t3))
	return degrees(atan2(s5, c5))

def t6(t1, t3, t4, t5):
	s6 = -r11*(cos(radians(t1))*c23(t1, t3)*sin(radians(t4)) - sin(radians(t1))*cos(radians(t4))) - r21*(sin(radians(t1))*c23(t1, t3)*sin(radians(t4)) + cos(radians(t1))*cos(radians(t4))) + r31*(s23(t1, t3)*sin(radians(t4)))
	c6 = r11*((cos(radians(t1))*c23(t1, t3)*cos(radians(t4)) + sin(radians(t1))*sin(radians(t4)))*cos(radians(t5)) - cos(radians(t1))*s23(t1, t3)*sin(radians(t5))) + r21*((sin(radians(t1))*c23(t1,t3)*cos(radians(t4)) - cos(radians(t1))*sin(radians(t4)))*cos(radians(t5)) - sin(radians(t1))*s23(t1, t3)*sin(radians(t5))) - r31*(s23(t1,t3)*cos(radians(t4))*cos(radians(t5)) + c23(t1, t3)*sin(radians(t5)))
	#s23temp.append(s23(t1,t3))
	#s6temp.append(s6)
	#c6temp.append(c6)
	return degrees(atan2(s6, c6))
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
#print("theta1:")
#print(theta1)

c1 = cos(radians(theta1[0]))
s1 = sin(radians(theta1[0]))

K = (px*px + py*py + pz*pz - a[2]*a[2] - a[3]*a[3] - d[2]*d[2]-d[3]*d[3])/(2*a[2])
print(K)

theta3.append(degrees(atan2(a[3], d[3]) - atan2(K, sqrt(a[3]*a[3] + d[3]*d[3]-K*K))))
theta3.append(degrees(atan2(a[3], d[3]) - atan2(K, -1 * sqrt(a[3]*a[3] + d[3]*d[3]-K*K))))
#print("theta3:")
#print(theta3 )

theta3output = [theta3[0] + 180, theta3[1] + 180]
#print('theta3:')
#print(theta3output)

theta2.append(t23(theta1[0], theta3[0]) - theta3[0])
theta2.append(t23(theta1[1], theta3[0]) - theta3[0])
theta2.append(t23(theta1[0], theta3[1]) - theta3[1])
theta2.append(t23(theta1[1], theta3[1]) - theta3[1])
#print("theta2:")
#print(theta2)

theta4.append(t4(theta1[0], theta3[0]))
theta4.append(t4(theta1[1], theta3[0]))
theta4.append(t4(theta1[0], theta3[1]))
theta4.append(t4(theta1[1], theta3[1]))
theta4.append(theta4[0] + 180)
theta4.append(theta4[1] + 180)
theta4.append(theta4[2] + 180)
theta4.append(theta4[3] + 180)
#print("theta4:")
#print(theta4)

theta5.append(t5(theta1[0], theta3[0], theta4[0]))
theta5.append(t5(theta1[1], theta3[0], theta4[1]))
theta5.append(t5(theta1[0], theta3[1], theta4[2]))
theta5.append(t5(theta1[1], theta3[1], theta4[3]))
theta5.append(-theta5[0])
theta5.append(-theta5[1])
theta5.append(-theta5[2])
theta5.append(-theta5[3])
#print("theta5:")
#print(theta5)

theta6.append(t6(theta1[0], theta3[0], theta4[0], theta5[0]))
theta6.append(t6(theta1[1], theta3[0], theta4[1], theta5[1]))
theta6.append(t6(theta1[0], theta3[1], theta4[2], theta5[2]))
theta6.append(t6(theta1[1], theta3[1], theta4[3], theta5[3]))
theta6.append(theta6[0] + 180)
theta6.append(theta6[1] + 180)
theta6.append(theta6[2] + 180)
theta6.append(theta6[3] + 180)
#print("theta6:")
#print(theta6)


print(theta1[0], theta2[0], theta3output[0], theta4[0], theta5[0], theta6[0])
print(theta1[1], theta2[1], theta3output[0], theta4[1], theta5[1], theta6[1])
print(theta1[0], theta2[2], theta3output[1], theta4[2], theta5[2], theta6[2])
print(theta1[1], theta2[3], theta3output[1], theta4[3], theta5[3], theta6[3])
print(theta1[0], theta2[0], theta3output[0], theta4[4], theta5[4], theta6[4])
print(theta1[1], theta2[1], theta3output[0], theta4[5], theta5[5], theta6[5])
print(theta1[0], theta2[2], theta3output[1], theta4[6], theta5[6], theta6[6])
print(theta1[1], theta2[3], theta3output[1], theta4[7], theta5[7], theta6[7])
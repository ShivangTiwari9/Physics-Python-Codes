from math import *
G,M=6.6738E-11,1.9891E30
L1=float(input("Enter the value of distance"))
V1=float(input("Enter the value of velocity"))
A=1
B=-(2*G*M)/(V1*L1)
C=-V1**2+(2*G*M)/L1
V2=(-B+sqrt((B**2)-(4*A*C)))/(2*A)
print(f"Aphelion Velocity: {V2}")
L2=L1*V1/V2
a=(L1+L2)/2
b=sqrt(L1*L2)
T=(2*pi*a*b)/(L1*L2)
e=(L2-L1)/(L2+L1)
print(f"Semi-Major Axis: {a} \nSemi-Minor Axis: {b}\nOrbital Period: {T}\nOrbital Eccentricity: {e}\n")
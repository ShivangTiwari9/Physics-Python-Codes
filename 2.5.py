from math import *
h,m=(6.6*10e-34)/(2*pi),9.1*10e-31
E=float(input("Enter the initial Kinetic Energy"))
V=float(input("Enter the Barrier Potential"))
K1=sqrt(2*m*E)/h
K2=sqrt(2*m*(E-V))/h
T=(4*K1*K2)/(K1+K2)**2
R=((K1-K2)/(K1+K2))**2
print(f"Transmission and Reflection probabilities are {T}% and {R}%")
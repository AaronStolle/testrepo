#hawkingradiation.py

from math import *
import numpy as np
from numpy import*
import matplotlib
import matplotlib.pyplot as plt

c = 3.0e8
G = 6.67e-11
k = 1.38e-23
h = 6.626e-34
h_bar = h/(2*pi)
tmax = 0
t = 0
dt = input ("enter time step in seconds: ")

m = []  #[] and the append create arrays for the graphs
R = []
s_g = []
ht = []
p = []
s = []
t_plot = []

#Calculations
M = input ("enter value for M in kg.: ")
m.append(M)
t_plot.append(0)
r_s = 2*G*M/(c*c)
R.append(r_s)
g = G*M/(r_s*r_s)
s_g.append(g)
T_H = h_bar*c*c*c/(8*pi*G*M*k)
ht.append(T_H)
P = h_bar*c*c*c*c*c*c/(15360*pi*G*G*M*M)
p.append(P)
S = 4*pi*k*G*M*M/h_bar
s.append(S)

while (M>0):
    M_mid= M - (h_bar*c*c*c*c/(3*5120*pi*G*G*M*M))*dt/2
   
    #dM = h_bar*c*c*c*c/(3*5120*pi*G*G*M*M)
    t_mid= t+dt/2
    M -= (h_bar*c*c*c*c/(3*5120*pi*G*G*M_mid*M_mid))*dt

    if fabs(M)*M <= 0.0:  #this formulation stops the calculations from going beyond M=0
        break
   
    m.append(M)
    t += dt
    t_plot.append(t)
    #M = M - dM
   
    r_s = 2*G*M/(c*c)
    R.append(r_s)
    g = G*M/(r_s*r_s)
    s_g.append(g)
    T_H = h_bar*c*c*c/(8*pi*G*M*k)
    ht.append(T_H)
    P = h_bar*c*c*c*c*c*c/(15360*pi*G*G*M*M)
    p.append(P)
    S = 4*pi*k*G*M*M/h_bar
    s.append(S)

print ("time (s)", t, "Mass (kg)", M, "radius (m)", r_s, "surface gravity (m/s^2)", g,
        "hawking temperature (K)", T_H, "power (W)", P, "entropy (J/K)", S)

plt.figure(1)
plt.suptitle('Mass versus Time')
plt.xlabel('Time (sec)')
plt.ylabel('Mass (kg)')
plt.plot(t_plot,m, 'b-')
plt.show(1)


plt.figure(2)
plt.suptitle('Schwarzschild Radius versus Time')
plt.xlabel('Time (sec)')
plt.ylabel('Radius (m)')
plt.plot(t_plot, R, 'r-')
plt.show(2)

plt.figure(3)
plt.suptitle('Surface Gravity versus Time')
plt.xlabel('Time (sec)')
plt.ylabel('Gravity (m/s^2)')
plt.plot(t_plot, s_g, 'y-')
plt.show(3)

plt.figure(4)
plt.suptitle('Hawking Temperature versus Time')
plt.xlabel('Time (sec)')
plt.ylabel('Temperature (K)')
plt.plot(t_plot, ht, 'g-')
plt.show(4)

plt.figure(5)
plt.suptitle('Power versus Time')
plt.xlabel('Time (sec)')
plt.ylabel('Power (W)')
plt.plot(t_plot, p, 'm-')
plt.show(5)

plt.figure(6)
plt.suptitle('Entropy versus Time')
plt.xlabel('Time (sec)')
plt.ylabel('Entropy (J/K)')
plt.plot(t_plot, s, 'b-')
plt.show(6)

if t < tmax:
    t = tmax
    print (tmax)

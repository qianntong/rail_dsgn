import numpy as np
import sympy

# problem 4a
L_total = (160-100)*100 # length from 100+00 to 160+00
pvi_sta = sympy.symbols('pvi_sta')
pvi_sta = sympy.solve(722-pvi_sta*0.01-719.8+0.007*(L_total-pvi_sta))[0] # station o PVI
Z_pvi_4a = 722 - pvi_sta * 0.01 # elevation of PVI
print("PVI elevation is %s'" %Z_pvi_4a)
print("PVI station is 26+00")

# problem 4b
Z_track = 703 # lowest elevatio of track
Z_bridge = 707 # lowest elevation of bridge
L_4b, R_4b, x_4b, Z_pvc_4b = sympy.symbols('L_4b R_4b x_4b Z_pvc_4b')
f1 = x_4b - L_4b/2 # x is a half of L
f2 = L_4b - 1.7/R_4b*100 # L=(G2-G1)/R*100
f3 = Z_pvc_4b + (-1)*x_4b/100 + R_4b*x_4b**2/20000 - Z_track # case of track elevation
f4 = Z_pvc_4b + (-1)*(x_4b-1000)/100 + R_4b*(x_4b-1000)**2/20000 - Z_bridge # case of bridge
sol_4b = sympy.solve([f1, f2, f3, f4], [L_4b, R_4b, x_4b, Z_pvc_4b])[0]
print("R is %s, less than 0.06(sag in main track), check!" %sol_4b[1])

#problem 4c
Z_pvt_4c = sol_4b[3] - 1*sol_4b[0]/100 + sol_4b[1]*sol_4b[0]**2/20000
print("PVC station is 109+00")
print("PVC elevation is %s'" %sol_4b[3])
print("PVT station is 143+00")
print("PVT elevation is %s'" %Z_pvt_4c)

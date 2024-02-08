import numpy as np

Ls = 100
I = np.deg2rad(86.18)
L1 = 2000

diversity_angle = np.deg2rad(3.82) # No.15 Frog's diversity angle
L_PI2LST = 167.34 # No.15 Frog's turnout length

T = (2000 - Ls/2 - np.sin(diversity_angle*Ls/2))/(1 + np.sin(diversity_angle)) # T of the curve
D_rad = np.arcsin(50 * np.tan(I/2) / T) * 2 # calculate the minimum of D

D = np.rad2deg(D_rad)
print("Problem 2a:")
print("D_min = %s\N{DEGREE SIGN}" %D)
D_round_up = 3.00 # round a quarter
print("Round a quarter up to %s\N{DEGREE SIGN}" %D_round_up)


# problem 2b
T_updated = 50 * np.tan(I/2) / np.sin(np.deg2rad(D_round_up)/2) # calculate T while D is 3.0 degree
PS_STA = np.cos(diversity_angle) * (Ls/2+T_updated+L_PI2LST) # PS to the north tangent line's projection point
print("Problem 2b:")
print("Length from STA10+60 to PS is %s feet, so PS_STA is 29+75.75" %PS_STA)

#problem 2c

degree_of_curve = 3 # No.15 Frog's diversity angle
Eu = 1 # assume 1" unbanlance for freight
v = 30 # diverging speed /mph
Ea = 0.0007*v**2*degree_of_curve - Eu # actual superelevation
print("Problem 2c:")
print("The superelevation is %s inch, round to the nearest quarter-inch is 1.00 inch" %Ea)

runoff_rate = 44 # runoff rate = 44 if v = 30 mph
Ls_check = 1 * runoff_rate # calculate the length of Ls by Ls = Ea * runoff rate
print("The calculated length is %s inches. Round it up to 50 inches. So it meets the assumption of 100 inches" %Ls_check)


#problem 2d
turnout_20 = 120 # minimum same handed trunouts of No.20 frog
diverging_angle_20 = np.deg2rad(2 + 51/60 + 51/3600) # diverging angle of No.20 frog
L_PS2PI = 61.06 #PS-PI length of No.20 frog
S = 25 # 25' track centers

L_PI2PI = S / np.tan(diverging_angle_20) #PI-PI distance
L_PS2PS = np.cos(diverging_angle_20) * L_PI2PI + 2 * L_PS2PI #PS-PS projection point distance
PS_STA_20 = 2975 + L_PS2PS
print("Problem 2d:")
print("Round the lengh %s feet, so PS_STA is 36+00.00" %PS_STA_20)


#problem 2e
L_20to10 = 900 # length between No.20 frog's turnout and existing No.11 frog's PS STA is 45+00 - 36+00
print("Problem 2e:")
print("900'(length between No.20 frog's turnout and existing No.11 frog's PS STA) > 120'(minimum same handed trunouts of No.20 frog) > 60'(minimum same handed trunouts of No.11 frog). So this distance is adequate")
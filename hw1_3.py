#problem 3a
G1 = 0.8 # %
G2 = -1 # %
R1 = -0.1 # UP stqandard R for v>40 mph of crest
L1 = (G2-G1) / R1 * 100 # length of curve
X = L1 / 2
Z_pvc = 760 - G1*X/100 - R1*X**2/20000 # general curve equation
Z_pvt = Z_pvc + G1*L1/100 + R1*L1**2/20000
Z_pvi = Z_pvc + X*G1/100
print("PVC elevation of crest: %s'" %Z_pvc)
print("PVC station of crest: 2041+00")
print("PVI elevation of crest: %s'" %Z_pvi)
print("PVI station of crest: 2050+00")
print("PVT elevation of crest: %s'" %Z_pvt)
print("PVT station of crest: 2059+00")

# problem 3b
R_NorthSag = 0.06
G2_NorthSag = 0.8 # 0.8%
G1_NorthSag = -0.2 # -0.2%
x_NorthSag = (G2_NorthSag-G1_NorthSag)/R_NorthSag*100
L_NorthSag = (Z_pvc - 730) / (G1-(-0.2))*100

#print(L_NorthSag)
Z_pvi_NorthSag = Z_pvc - L_NorthSag*G2_NorthSag*0.01
Z_pvt_NorthSag = Z_pvi_NorthSag + x_NorthSag/2*0.008
Z_pvc_NorthSag = Z_pvi_NorthSag + x_NorthSag/2*0.002
print("PVC elevation of north sag: %s'" %Z_pvc_NorthSag)
print("PVC station of north sag: 2014+82")
print("PVI elevation of north sag: %s'" %Z_pvi_NorthSag)
print("PVI station of north sag: 2023+00")
print("PVT elevation of north sag: %s'" %Z_pvt_NorthSag)
print("PVT station of north sag: 2031+00")

# problem 3c
R_SouthSag = 0.06
G1_SouthSag = 1
L_SourhSag = (G1_NorthSag-G1_SouthSag) / R_SouthSag * -100
x_3c = (Z_pvt - 730) / (G1_NorthSag+1) * 100
Z_pvi_SouthSag = Z_pvt -  x_3c*0.01
Z_pvc_SouthSag = Z_pvi_SouthSag + L_SourhSag/2*0.01
Z_pvt_SouthSag = Z_pvi_SouthSag - L_SourhSag*0.002

print("PVC elevation of south sag: %s'" %Z_pvc_SouthSag)
print("PVC station of north sag: 2074+65")
print("PVI elevation of south sag: %s'" %Z_pvi_SouthSag)
print("PVI station of north sag: 2081+31")
print("PVT elevation of north sag: %s'" %Z_pvt_SouthSag)
print("PVT station of north sag: 2087+98")

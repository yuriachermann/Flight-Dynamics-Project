import numpy as np


def rho_si(height):
    h = height * 3.2808
    return (((1 - 6.875E-6 * h) ** 5.2561) / (1 - 6.875E-6 * h)) * 1.225


def pot_req(vel, h):
    cl = 2 * W / (rho_si(h) * S * pow(vel, 2))
    cdi = pow(cl, 2) * K
    cd = Cdo + cdi
    d = cd * rho_si(h) * pow(vel, 2) * S / 2
    return d * vel * 0.00134


m = 304.0429  # Mass [Kg]
H = 2300  # Altitude [m]
g = 9.81  # Gravity Acceleration [m/s²]
e = 0.9  # Oswald Efficiency Number
AR = 18  # Aspect Ratio
W = m * g  # Weight [N]
print(W)
S = 8  # Wing Area [m²]
WS = W / S  # Wing Loading [N/m²]
v = 36  # Velocity [m/s]
d_fuel = 690  # Fuel Density [Kg/m³]
K = 1 / (np.pi * AR * e)  # K Coefficient
Cl = 2 * W / (rho_si(H) * S * pow(v, 2))  # Lifting Coefficient
print("Cl =", Cl)
Cl_max = 2.3 * 0.8  # Max Lifting Coefficient
Cdi = pow(Cl, 2) * K  # Lift-induced Drag Coefficient
print(Cdi)
Cdo = 0.01934  # Parasite Drag Coefficient
Cd = Cdo + Cdi  # Drag Coefficient
print(Cd)
D = Cd * rho_si(H) * pow(v, 2) * S / 2  # Drag [N]
print("D =", D)
L = Cl * rho_si(H) * pow(v, 2) * S / 2  # Lift [N]
print(L/D)
print(W/S)
print(WS)
print(rho_si(H))

print("\nArrasto =\t\t\t\t\t", round(D, 4), "N")
print("Sustentação =\t\t\t\t", round(L, 4), "N\n")

########################################################################################################################

V_stall = np.sqrt((2 * WS) / (rho_si(H) * Cl_max))  # Stall Velocity [m/s]
V_endurance = np.sqrt((2 * WS / rho_si(H)) * np.sqrt(K / (3 * Cdo)))  # Endurance Velocity [m/s]
V_range = np.sqrt((2 * WS / rho_si(H)) * np.sqrt(K / Cdo))  # Range Velocity [m/s]

print("Velocidade de stall =\t\t\t", round(V_stall, 4), "m/s")
print("Velocidade de endurance =\t\t", round(V_endurance, 4), "m/s")
print("Velocidade de range =\t\t\t", round(V_range, 4), "m/s")

print("\nEndurance - Stall =\t\t\t\t", round(V_endurance-V_stall, 4), "m/s\n")

Cl_endurance = 2 * W / (rho_si(H) * S * pow(V_endurance, 2))  # Lifting Coefficient Endurance
Cdi_endurance = pow(Cl_endurance, 2) * K
Cd_endurance = Cdo + Cdi_endurance
L_endurance = Cl_endurance * rho_si(H) * pow(V_endurance, 2) * S / 2  # Lift [N]
D_endurance = Cd_endurance * rho_si(H) * pow(V_endurance, 2) * S / 2  # Drag [N]
print("L/D endurance =", L_endurance/D_endurance)

Cl_range = 2 * W / (rho_si(H) * S * pow(V_range, 2))
Cdi_range = pow(Cl_range, 2) * K
Cd_range = Cdo + Cdi_range
L_range = Cl_range * rho_si(H) * pow(V_range, 2) * S / 2  # Lift [N]
D_range = Cd_range * rho_si(H) * pow(V_range, 2) * S / 2  # Drag [N]
print("L/D range =", L_range/D_range)

n_endurance = 0.58  # Endurance Efficience
n_range = 0.68  # Range Efficience

P_eixo_endurance = (D_endurance * V_endurance) / (n_endurance * 745.7)  # Endurance Shaft Power [hp]
P_eixo_range = (D_range * V_range) / (n_range * 745.7)  # Range Shaft Power [hp]

print("\nPotencia de eixo de endurance =\t\t", round(P_eixo_endurance, 4), "hp")
print("Potencia de eixo de range =\t\t\t", round(P_eixo_range, 4), "hp\n")

C = 7  # Consumption [l/h]

########################################################################################################################

c_power_endurance = (d_fuel * (C * 1e-3 / 3.6e3)) / (P_eixo_endurance * 745.7)  # C Power Endurance [mg/W*s]
c_bhp_endurance = C * d_fuel * 1e-6 * 2.2046 / P_eixo_endurance
c_spec_endurance = (c_bhp_endurance * V_endurance) / (550 * n_endurance)  # C specific Endurance
# c_spec_endurance = (c_power_endurance * V_endurance) / n_endurance  # C specific Endurance
print("c power endurance =\t", "{:.2e}".format(c_power_endurance))
print("c spec endurance =\t", "{:.2e}".format(c_spec_endurance))

# print("C power e", c_power_endurance)
# print("SFC e", c_spec_endurance)
# print("cl e", Cl)
# print("cd e", Cd)
# print("rho e", rho_si(H))
# print("w cheio", W)
# print("w vazio", W-50*g)

E = (Cl_endurance/(Cd_endurance * c_spec_endurance))*np.log(W/(W-50*g))  # Raymer
# E = (n_endurance/c_spec_endurance)*(Cl_endurance**1.5/Cd_endurance)*((2*rho_si(H)*S)**0.5)*(((W-50*g)**-0.5)-(W**-0.5))
print("\nEndurance = \t", round(E/3600, 4), "h\n")

########################################################################################################################

c_power_range = (d_fuel * (C * 1e-3 / 3.6e3)) / (P_eixo_range * 745.7)  # C Power Range [mg/W*s]
c_bhp_range = C * d_fuel * 1e-6 * 2.2046 / P_eixo_range
c_spec_range = (c_bhp_range * V_range) / (550 * n_range)  # C specific Range
# c_spec_range = (c_power_range * V_range) / n_range  # C specific Range
print("c power range =\t\t", "{:.2e}".format(c_power_range))
print("c spec range =\t\t", "{:.2e}".format(c_spec_range))

# print("\nCpower r", c_power_range)
# print("ce r", c_spec_range)
# print("cl r", Cl_range)
# print("cd r", Cd_range)
# print("etar r", n_range)

R = ((Cl_range * V_range)/(Cd_range * c_spec_range))*np.log(W/(W-50*g))  # Raymer
# R = (n_range/c_spec_range)*(Cl_range/Cd_range)*(np.log(W/(W-50*g)))
print("\nRange =\t\t\t", round(R/1000, 4), "km")

########################################################################################################################

Cl_sealevel = 0.5 * 0.8  # Lifting Coefficient at Sea Level
Cdi_sealevel = pow(Cl_sealevel, 2) * K  # Lift-induced Drag Coefficient at Sea Level
Cdo_sealevel = 0.01841  # Parasite Drag Coefficient at Sea Level
Cd_sealevel = Cdo_sealevel + Cdi_sealevel  # Drag Coefficient at Sea Level
V_liftoff = 1.1 * V_stall  # Lift-off Velocity [m/s]
V_wind = 0  # Wind Velocity [m/s]
V_avg = 0.707 * V_liftoff  # Average Velocity [m/s]
T_avg = 640  # Average Trust [N]
mi_r = 0.025  # Friction Coefficient
Cl_opt = 0.5 * mi_r / K  # Optimized
D_avg = 0.5 * Cd_sealevel * rho_si(0) * S * (V_avg ** 2)
L_avg = 0.5 * Cl_opt * rho_si(0) * S * (V_avg ** 2)
phi = 0
A_avg = (g / W) * (T_avg - D_avg - (W * phi) - (mi_r * (W - L_avg)))
SG = ((V_liftoff + V_wind) ** 2) / (2 * A_avg)

print("\nCorrida de Decolagem =\t", round(SG, 4), "m\n")


# Range = 1093 km
# Endurance = 11 horas

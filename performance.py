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


m = 297.5318  # Mass [Kg]
H = 2300  # Altitude [m]
g = 9.81  # Gravity Acceleration [m/s²]
e = 0.9  # Oswald Efficiency Number
AR = 11.1111  # Aspect Ratio
W = m * g  # Weight [N]
S = 9  # Wing Area [m²]
WS = W / S  # Wing Loading [N/m²]
v = 36  # Velocity [m/s]
d_fuel = 690  # Fuel Density [Kg/m³]
K = 1 / (np.pi * AR * e)  # K Coefficient
Cl = 2 * W / (rho_si(H) * S * pow(v, 2))  # Lifting Coefficient
print(Cl)
Cl_max = 1.7 * 0.8  # Max Lifting Coefficient
Cdi = pow(Cl, 2) * K  # Lift-induced Drag Coefficient
print(Cdi)
Cdo = 0.01673  # Parasite Drag Coefficient
Cd = Cdo + Cdi  # Drag Coefficient
print(Cd)
D = Cd * rho_si(H) * pow(v, 2) * S / 2  # Drag [N]
print(D)
L = Cl * rho_si(H) * pow(v, 2) * S / 2  # Lift [N]
print(L)

print("\nArrasto =\t\t\t\t\t", round(D, 4), "N")
print("Sustentação =\t\t\t\t", round(L, 4), "N\n")

########################################################################################################################

V_endurance = np.sqrt((2 * WS / rho_si(3000)) * np.sqrt(K / (3 * Cdo)))  # Endurance Velocity [m/s]
V_range = np.sqrt((2 * WS / rho_si(3000)) * np.sqrt(K / Cdo))  # Range Velocity [m/s]
V_stall = np.sqrt((2 * WS) / (rho_si(3000) * Cl_max))  # Stall Velocity [m/s]

print("Velocidade de endurance =\t\t", round(V_endurance, 4), "m/s")
print("Velocidade de range =\t\t\t", round(V_range, 4), "m/s")
print("Velocidade de stall =\t\t\t", round(V_stall, 4), "m/s")

n_endurance = 0.61  # Endurance Efficience
n_range = 0.70  # Range Efficience

P_eixo_endurance = 17.5 / n_endurance  # Endurance Shaft Power [hp]
P_eixo_range = 20.5 / n_range  # Range Shaft Power [hp]

print("\nPotencia de eixo de endurance =\t\t", round(P_eixo_endurance, 4), "hp")
print("Potencia de eixo de range =\t\t\t", round(P_eixo_range, 4), "hp")

C = 7  # Consumption [l/h]

########################################################################################################################

Cl_endurance = 2 * W / (rho_si(H) * S * pow(V_endurance, 2))  # Lifting Coefficient Endurance
Cd_endurance = Cd = Cdo + pow(Cl_endurance, 2) * K  # Drag Coefficient Endurance

c_power_endurance = (d_fuel * (C * 1e-3 / 3.6e3)) / (P_eixo_endurance * 745.7)  # C Power Endurance [Kg/W s]
c_spec_endurance = (c_power_endurance * V_endurance) / n_endurance  # C specific Range

# print("C power e", c_power_endurance)
# print("SFC e", c_spec_endurance)
# print("cl e", Cl)
# print("cd e", Cd)
# print("rho e", rho_si(H))
# print("w e", W-50*g)

# E = (Cl * np.log(W / (W - 50 * g))) / (Cd * c_spec_endurance)  # Raymer
E = (n_endurance/c_spec_endurance)*(Cl_endurance**1.5/Cd_endurance)*((2*rho_si(H)*S)**0.5)*(((W-50*g)**-0.5)-((W)**-0.5))
print("\nEndurance = \t\t\t", E/3600, "h")

########################################################################################################################

Cl_range = 2 * W / (rho_si(H) * S * pow(V_range, 2))  # Lifting Coefficient Range
Cd_range = Cd = Cdo + pow(Cl_range, 2) * K  # Drag Coefficient Range

c_power_range = (d_fuel * (C * 1e-3 / 3.6e3)) / (P_eixo_range * 745.7)  # C Power Range [Kg/W s]
c_spec_range = (c_power_range * V_range) / n_range  # C specific Range

# print("\nCpower r", c_power_range)
# print("ce r", c_spec_range)
# print("cl r", Cl_range)
# print("cd r", Cd_range)
# print("etar r", n_range)

# R = L * V_range * np.log(W / (W - 50 * g)) / (D * c_spec_range)  # Raymer
R = (n_range/c_spec_range)*(Cl_range/Cd_range)*(np.log(W/(W-50*g)))
print("\nRange =\t", R/1000, "km")

########################################################################################################################

Cl_sl = 0.5 * 0.8  # Lifting Coefficient at Sea Level
Cdi_sl = pow(Cl_sl, 2) * K  # Lift-induced Drag Coefficient at Sea Level
Cdo_sl = 0.01841  # Parasite Drag Coefficient at Sea Level
Cd_sl = Cdo_sl + Cdi_sl  # Drag Coefficient at Sea Level
V_lof = 1.1 * V_stall  # Lift-off Velocity [m/s]
V_wind = 0  # Wind Velocity [m/s]
V_avg = 0.707 * V_lof  # Average Velocity [m/s]
T_avg = 640  # Average Trust [N]
mi_r = 0.025  # Friction Coefficient
Cl_opt = 0.5 * mi_r / K  # Optimized
D_avg = 0.5 * Cd_sl * rho_si(0) * S * (V_avg ** 2)
L_avg = 0.5 * Cl_opt * rho_si(0) * S * (V_avg ** 2)
phi = 0
A_avg = (g / W) * (T_avg - D_avg - (W * phi) - (mi_r * (W - L_avg)))
SG = ((V_lof + V_wind) ** 2) / (2 * A_avg)

print("\nCorrida de Decolagem =\t", round(SG, 4), "m")

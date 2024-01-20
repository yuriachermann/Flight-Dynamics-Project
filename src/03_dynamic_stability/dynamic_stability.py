import numpy as np
from performance import rho_si

# VANT parameters

H = 2300  # Altitude
g = 9.81  # Gravity aceleration [m/s²]
S = 16  # Wing projected area [m²]
U_o = 67  # Velocity [m/s]
cc = 0.66667  # Chord [m]
m = 306.8002  # Aircraft mass [kg]
q = 0.5 * rho_si(H) * U_o**2  # Dynamic pressure [Pa]
b = 12

# Inertial mass moments

Ixx = 5.854  # [kgm²]
Iyy = 645.549  # [kgm²]
Izz = 649.139  # [kgm²]

# Parameters

MACH_o = 0.105000
ALPHA_o = 0.000000
BETA_o = 0.000000
U_o = 67.000000

CLo = 0.909890
CDo = 0.046867
CYo = 0.000005
Clo = 0.000013
Cmo = 0.117089
Cno = -0.000002

CL_alpha = 6.769781
CL_beta = -0.045112
CL_mach = 0.120045
CL_p = 0.002191
CL_q = 25.449264
CL_r = 0.019158
CL_u = 0.012605
CL_alpha_2 = 0.000000
CL_alpha_dot = 0.000000
CD_alpha = 0.165440
CD_beta = 0.002264
CD_mach = 0.004520
CD_p = 0.024567
CD_q = 0.462813
CD_r = 0.002591
CD_u = 0.000475
CD_alpha_2 = 0.000000
CD_alpha_dot = 0.000000
CY_alpha = 0.000366
CY_beta = -0.218839
CY_mach = -0.000001
CY_p = -0.105500
CY_q = -0.000284
CY_r = 0.203788
CY_u = -0.000000
CY_alpha_2 = 0.000000
CY_alpha_dot = 0.000000
Cl_alpha = 0.000388
Cl_beta = -0.067622
Cl_mach = -0.000005
Cl_p = -0.743161
Cl_q = -0.001632
Cl_r = 0.274140
Cl_u = -0.000001
Cl_alpha_2 = 0.000000
Cl_alpha_dot = 0.000000
Cm_alpha = -5.966556
Cm_beta = 0.141143
Cm_mach = 0.032096
Cm_p = 0.094807
Cm_q = -65.412240
Cm_r = 0.001132
Cm_u = 0.003370
Cm_alpha_2 = 0.000000
Cm_alpha_dot = 0.000000
Cn_alpha = 0.000035
Cn_beta = 0.002930
Cn_mach = -0.000000
Cn_p = -0.113059
Cn_q = 0.000381
Cn_r = -0.040370
Cn_u = -0.000000
Cn_alpha_2 = 0.000000
Cn_alpha_dot = 0.000000


# Dynamic stability derivatives

# Longitudinal

Xu = (-(CD_u + 2 * CDo) * q * S) / (m * U_o)
Zu = (-(CL_u + 2*CLo) * q * S) / (m * U_o)
Zw = (-(CL_alpha + CDo) * q * S) / (m * U_o)
Mw = (Cm_alpha * q * S * cc) / (U_o * Iyy)
Mw_dot = (Cm_alpha_dot * q * S * cc**2 / (2 * U_o**2 * Iyy))
Mq = (Cm_q * cc**2 * q * S) / (2 * U_o * Iyy)
M_alpha = U_o * Mw
Z_alpha = U_o * Zw
M_alpha_dot = U_o * Mw_dot

# Phugoid mode

freq_phug = np.sqrt((-Zu * g) / U_o)
damping_phug = -Xu / (2 * freq_phug)
print("\nPhugoid frequency =", round(freq_phug, 4))
print("Phugoid ratio =", round(damping_phug, 4))

# Short period mode

freq_short = np.sqrt(((Z_alpha * Mq) / U_o) - M_alpha)
damping_short = -(Mq + M_alpha_dot + (Z_alpha/U_o)) / (2 * freq_short)
print("\nShort Period frequency =", round(freq_short, 4))
print("Short Period ratio =", round(damping_short, 4))

# Latero-Direcional

Y_beta = (q * S * CY_beta) / m
N_beta = (q * S * b * Cn_beta) / Izz
L_beta = (q * S * b * Cl_beta) / Ixx
Yp = (q * S * b * CY_p) / (2 * m * U_o)
Np = (q * S * b**2 * Cn_p) / (2 * Izz * U_o)
Lp = (q * S * b**2 * Cl_p) / (2 * Ixx * U_o)
Yr = (q * S * b * CY_r) / (2 * m * U_o)
Nr = (q * S * b**2 * Cn_r) / (2 * Izz * U_o)
Lr = (q * S * b**2 * Cl_r) / (2 * Ixx * U_o)

# Espiral

espiral_criteria = L_beta * Nr - Lr * N_beta
espiral_time = L_beta / (L_beta * Nr - Lr * N_beta)
print("\nEspiral criteria =", round(espiral_criteria, 4))
print("Espiral time =", round(espiral_time, 4))

# Roll

roll_time = -1 / Lp
print("\nRoll time =", "{:.2e}".format(roll_time))

# Dutch Roll

freq_dr = np.sqrt(((Y_beta * Nr) - (N_beta * Yr) + (U_o * N_beta)) / U_o)
damping_dr = -(Y_beta + U_o * Nr) / (2 * freq_dr * U_o)
print("\nDutch Roll natural frequency =", round(freq_dr, 4))
print("Dutch Roll damping ratio =", round(damping_dr, 4))
print("damping * freq dr =", round(damping_dr*freq_dr, 4))

# Gregson=
#
# Phugoid natural frequency = 0.51
# Phugoid damping ratio = 0.0518
# Short Period natural frequency = 2.937
# Short Period damping ratio = 0.532
# Espiral criteria = 0.084
# Roll time = 0.0455
# Dutch Roll natural frequency = 0.104
# Dutch Roll damping ratio = 0.902

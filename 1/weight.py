import numpy as np


def rho_imp(h):
    return (((1 - 6.875E-6 * h) ** 5.2561) / (1 - 6.875E-6 * h)) * 0.0765


# Aircraft weight estimation

H = 2300 * 3.2808  # Altitude (ft)
v = 36 * 3.2808  # Velocity (ft/s)

V = 3.054 * 35.3147  # Volume (ft³)
d = 6.055  # Density (lb/ft³)
Sw = 8 * 10.7639  # Wing area (ft²)
Wfw = 110.2311  # Wing fuel weight (lbf)
ARw = 18  # Wing aspect ratio
Vc4 = 0  # Wing sweep angle at 1/4
q = rho_imp(H) * v**2 * 0.5  # Dynamic pressure (lb/ft s²)
lbd = 0.8  # Wing tap ratio
tc = 0.14098  # Wing thickness and chord ratio
nz = 3.8  # Ultimate load factor
Wo = d * V  # Gross weight (lbf)

Ft = 0  # Tail factor (0=conventional tail, 1=T-tail)

Sht = 1.8 * 10.7639  # Horizontal tail area (ft²)
Vc4ht = 0  # Horizontal tail sweep angle at 1/4
ARht = 8.88888  # Horizontal tail aspect ratio
lbdHT = 0.5  # Horizontal tail tap ratio
lht = 3.1 * 3.2808  # Horizontal tail arm (ft)

Svt = 0.42 * 10.7639  # Vertical tail area (ft²)
Vc4vt = 0  # Vertical tail sweep angle at 1/4
ARvt = 3.42857  # Vertical tail aspect ratio

Sfs = 14.082 * 10.7639  # Fuselage wetted area (ft²)
lFS = 6 * 3.2808  # Fuselage length (ft)
dFS = 0.75 * 3.2808  # Fuselage average depth (ft)
Vp = 2.563 * 35.3147 * 0.1  # Pressurized cabin volume (ft³)
DeltaP = 1  # Differential pressure cabin (psi)


# Wing weight:
Ww = 0.036 * pow(Sw, 0.758) * pow(Wfw, 0.0035) * pow(ARw / pow(np.cos(Vc4), 2), 0.6) * pow(
    q, 0.006) * pow(lbd, 0.04) * pow(100 * tc / np.cos(Vc4), -0.3) * pow(nz * Wo, 0.49)

# Horizontal tail weight:
Wht = 0.016 * pow(nz * Wo, 0.414) * pow(q, 0.168) * pow(Sht, 0.896) * pow(100 * tc / np.cos(
    Vc4ht), -0.12) * pow(ARht / pow(np.cos(Vc4ht), 2), 0.043) * pow(lbdHT, -0.02)

# Vertical tail weight:
Wvt = 0.073 * (1 + 0.2 * Ft) * pow(nz * Wo, 0.376) * pow(q, 0.122) * pow(Svt, 0.873) * pow(
    100 * tc / np.cos(Vc4vt), -0.49) * pow(ARvt / pow(np.cos(Vc4vt), 2), 0.357) * pow(lbd, 0.039)

# Fuselage weight:
Wfs = 0.052 * pow(Sfs, 1.086) * pow(nz * Wo, 0.177) * pow(lht, -0.051) * pow(
    lFS / dFS, -0.072) * pow(q, 0.241) + 11.9 * pow(Vp * DeltaP, 0.271)

Wm = 55 * 2.20538  # Moto weight (lbf)
Wpl = 100 * 2.20538  # Payload weight (lbf)

Wt = Wfs+Wvt+Wht+Ww+Wm+Wpl

print("Initial mass = \t\t\t\t", round(Wo * 0.4536, 4), "kg")
print("Wing mass = \t\t\t\t", round(Ww * 0.4536, 4), "kg")
print("Horizontal tail mass = \t\t", round(Wht * 0.4536, 4), "kg")
print("Vertical tail mass = \t\t", round(Wvt * 0.4536, 4), "kg")
print("Fuselage mass = \t\t\t", round(Wfs * 0.4536, 4), "kg")
print("Total mass = \t\t\t\t", round(Wt * 0.4536, 4), "kg")
print("Difference = \t\t\t\t", round((Wt-Wo) * 0.4536, 4), "kg")

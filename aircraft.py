import numpy as np

HP = 80  # Motor power (HP)
Mm = 55  # Motor mass (kg)
PLm = 100  # Payload mass (kg)
WS = 873  # W/S (N/m²)
g = 9.81  # Gravity acceleration (m/s²)
Pl = 12  # Power loading (lb/hp)
ARmax = 18  # Aspect ratio max
AR = ARmax  # Aspect ratio
lb_kg = 2.20462  # Convertion lb to kg

Am = HP * Pl / lb_kg  # VANT mass
Aw = Am * g  # VANT weight
S = Aw / WS  # Wing area
b = np.sqrt(S * AR)  # Span

print("VANT mass =\t\t", Am, "kg")
print("VANT weight =\t", Aw, "N")
print("Wing area =\t\t", S, "m²")
print("Span =\t\t\t", b, "m")

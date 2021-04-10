import numpy as np
from numpy import sqrt, log, pi

# Dados de entrada:
WS     = 699.24     # W/S [N/m^2]
PLoad  = 12      # [lb/hp]
ARmax  = 18      # Razão de aspecto máxima
Rosg   = 1.225   # Densidade ao nível do mar [kg/m3]
Ro     = 97     # Densidade média [kg/m^3]
RoP    = 1000    # Densidade da carga paga [kg/m^3]
RoT    = 743.11     # Densidade média do combustível [kg/m^3]
Power  = 80      # Potência do motor [hp]
Cc     = 12.4      # Consumo de combustível por hora [L/h]
Wm     = 55      # Massa do motor [kg]
Wp     = 100      # Carga paga [kg]
Wt     = 50      # Massa do tanque de combustível [kg]
CLmax  = 1.4*0.8     # Coeficiente de sustentação máxima
g      = 9.81     # Gravidade [m/s^2]
fi     = 0       # Ângulo entre o avião e a pista
mi     = 0.025   # Coeficiente de atrito da roda com o chão
Vwind  = 0       # Velocidade do vento [m/s]
Hmax   = 4500    # Altura máxima [m]
e      = 0.9    # Coeficiente de Oswald

#Cálculos gerais:
W0     = (PLoad*Power)*4.4482 # Peso da aeronave [N]
W      = W0/g                 # Massa da aeronave [kg]
W1     = W - Wt               # Massa sem combustível
S      = W0/WS                # Área da asa [m^2]
b      = sqrt(S*ARmax)        # Envergadura [m]
corda  = S/b                  # corda [m]
Vinf   = 0
Vmax   = 73                   # Velocidade máxima [m/s] obtida no gráfico de potência disponível e requerida por velocidade
K      = 1/(pi*e*ARmax)

#Dados para o cálculo da fuselagem:
W2     = 438.398#Massa só da estrutura [kg]
Vol    = 97.397        # Volume da estrutura [m^3]
VolFus = 87.643  # Volume da fuselagem [m^3]
Compr  = 6       # Comprimento da fuselagem [m]
Posic  = Compr/4      #Posição inicial da asa em relação à fuselagem


#Endurance
Roend   = 0.9379                                  # Densidade associada à altura média de 2700m [kg/m^3]
CD0endur= 0.02671                                #CD0 para altitude e velocidade do endurance
CLendur = sqrt(3*CD0endur/K)               # Coeficiente de sustentação para a velocidade que otimiza o endurance
CDendur = CD0endur + K*(CLendur**2)
Vendur  = np.sqrt(2*WS/(Roend*CLendur))      #Velocidade que otimiza o endurance

#Consumo específico de combustível
etae    = 0.67               #Eficiência (gráfico 2)
Pae     = 14800            # Potência disponível [W]
Pee     = Pae/etae           # Potência de eixo [W]
ne      = 3500              # Rotação do motor [rpm]
fce     = 0.01/3600     #Fuel consumption [m3/s]
cpowere = fce*RoT/Pee       #Consumo específico de combustível [kg/ws]
ce      = (cpowere*Vendur)/etae


E      = (CLendur/(CDendur*ce))*np.log(W/W1) # [s]

# Range:
CD0r   = 0.02568                     # CD0 para altitude 4500m e velocidade do range (processo iterativo)
CLr    = np.sqrt(CD0r/K)                # Cl que otimiza o Range
CDr     = CD0r + K*(CLr**2)
Rorange = 0.777                        #Densidade do ar a 4500m
Vminr  = sqrt((2*WS)/(Rorange*CLr))    # Velocidade que otimiza o Range [m/s]

#Consumo específico de combustível:
etar    = 0.79           # Eficiência (gráfico 2)
Par     = 17400            #Potência disponível [W]
Per     = Par/etar         #Potência de eixo [W]
nr      = 3000              #Rotação do motor [rpm]
fcr     = 7.4*((10**-3)/3600)    #Fuel consumption [m3/s]
cpowerr = fcr*RoT/Per       #Consumo especícifo de combustível [kg/ws]
cr      = (cpowerr*Vendur)/etar

R      = (Vminr*CLr/(cr*CDr))*log(W/W1) # Range ótimo [m]
          
#Distância de decolagem:
Vstall = sqrt(2*WS/(Rosg*CLmax))                         #Velocidade de stall [m/s]
Vlof   = 1.1*Vstall                                     #Velocidade de decolagem [m/s]
Vavg   = 0.707*Vlof                                      #Velocidade média [m/s]
CLlof  = 0.0                                             #Coeficiente de sustentação na decolagem, considerando alfa = 0
CD0lof = 0.02455                                         # Arrasto parasita para a decolagem
CDlof  = CD0lof + K*CLlof**2                              # Coeificiente de Arrasto
Lavg   = CLlof*Rosg*Vavg**2*S                             # Sustentação média [N]
Davg   = CDlof*Rosg*Vavg**2*S                             # Arrasto médio [N]
Tavg   = 640
a      = (g/W0)*(Tavg - Davg - W0*fi - mi*(W0 - Lavg))   # Aceleração média [m/s^2]
Vg     = Vlof - Vwind                                    # Velocidade de decolagem corrigida pelo vento [m/s]
Sg     = Vg**2/(2*a)                                      # Distância da pista de decolagem [m]

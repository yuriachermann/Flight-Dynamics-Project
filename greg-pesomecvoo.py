# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:07:16 2021

@author: Larissa Coutinho
"""

import numpy as np
import matplotlib.pylab as plt
from numpy import cos
#Aceleração da gravidade em ft/s²
g = 32.174 


#Cálculo de Atmosfera Padrão
def pho(H):
    sigma = ((1-6.875E-6*H_max)**5.2561)/(1-6.875E-6*H_max)* 0.0765
    return sigma
H_max = 10334 #Altitude máxima de cruzeiro em ft
pho_H = pho(H_max) #Densidade do ar em lb/ft³ à 10334 ft = 3150m

#Dados de entrada
PWload = 12 #Power Loading em lb/hp
W_S = 18.233   #Carga Alar lbf/ft²
Power = 80  #Potência do motor em hp
ARmax = 18  #Razão de aspecto máxima
Mm = 121.254     #Massa do motor em lb
Mpl = 220.462   #Massa da carga paga em lb
Mt = 110.231     #Massa do combustível em lb
phom = 6.05551   #Densidade média da aeronave em lb/ft³
g = 32.174    #Aceleração gravitacional em ft/s²
e = 0.9   #Coeficiente de Oswald
AR = 18   #Razão de Aspecto utilizada

#Estimativa inicial de peso da aeronave com base nos dados de entrada
Winicial = (Power * PWload) # Winicial = 960lbf
#Estimativa da área de asa de referência com base no peso inicial
S_ref = Winicial / W_S
#Estimativa inicial de envergadura
b = plt.sqrt( S_ref * ARmax )
#Estimativa inicial de corda
c = S_ref / b

#Dados obtidos com o OpenVSP
VolTotal= 97.397 #Volume total geométrico em ft³

#Peso da aeronave calculados por dados do Raymer
n = 3.8 #Fator de carga adimensional
Sw = 52.651#Area em ft² 
Wfw = 110.231 #Peso do combustível em lbf
ARw = 18 #Razão de aspecto da asa
Vc4 = 0 
q = 0.5*(232.94**2)*pho_H #Pressão dinâmica a 109,61 ft/s 
lbda = 1.00 #
tc = 0.1 #Grossura / corda do aerofólio
nz = 3.8 #Fator de carga adimensional
Wo = VolTotal  * phom #Peso total estimado em lbf, calculado pela densidade média x volume;

#Peso da asa em lbf 
Ww=0.036*(Sw**0.758)*(Wfw**0.0035)*((ARw/((cos(Vc4))**2))**0.6)*(q**0.006)*(lbda**0.04)*((100*tc/(cos(Vc4)))**(-0.3))*(nz*Wo)**0.49

Sht = 15.25
Vc4ht = 0
ARht = 8.067
lambdaHT = 0.1
#Peso estabilizador horizontal em lbf
Wht=0.016*((nz*Wo)**0.414)*(q**0.168)*(Sht**0.896)*((100*tc/(cos(Vc4ht)))**(-0.12))*((ARht/(cos(Vc4ht))**2)**0.043)*(lambdaHT**(-0.02))

Ftail = 1
Svt = 15.78
Vc4vt = 0.3839
ARvt = 2.33
#Peso estabilizador vertical em lbf
Wvt=0.073*(1+0.2*Ftail)*((nz*Wo)**0.376)*(q**0.122)*(Svt**0.873)*((100*tc/(cos(Vc4vt)))**(-0.49))*((ARvt/(cos(Vc4vt))**2)**0.357)*(lbda**0.039)

#Peso da Fuselagem em lbf
Sfus = 150.375
lht = 6.309
lfs = 19.68
dfs = 2.40
Vp = 8.7643
DeltaP = 1
Wffus = ((0.052*Sfus)**1.086)*((n*Wo)**0.177)*(lht**-0.051)*((lfs/dfs)**-0.072)*(q**0.241) + 11.9*((Vp*DeltaP)**0.271)

#Peso total da Aeronave + Motor + Carga + Combustível em lbf
W = Ww + Wht + Wvt + Wffus + Mm + Mpl + Mt
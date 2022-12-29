#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt
import numpy as np

# Objectives:
#   code:
#     https://drive.google.com/file/d/19aP8p5_P4ctM7Y8fg74ErdViTrfGOENZ/view?usp=share_link
#     Below equation numbers come from this link ^^^
#

# Sources: 
#   https://inside-guitar.com/the-ultimate-guide-to-classical-guitar-strings/
#   https://euphonics.org/publication-list-jim-woodhouse/
#   https://www.ingentaconnect.com/contentone/dav/aaua/2019/00000105/00000003/art00012
#   https://www.ingentaconnect.com/content/dav/aaua/2019/00000105/00000003/art00012#
#   https://drive.google.com/file/d/19aP8p5_P4ctM7Y8fg74ErdViTrfGOENZ/view?usp=share_link
#   https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5459001/
#   https://publicwebuploads.uwec.edu/documents/Musical-string-inharmonicity-Chris-Murray.pdf

π = pi =math.pi

# String density (kg/m**3)
rho  = 1070 # nylon

# String diameter (m)
d = 0.001

# Frequency (Hz)
f = f1 = 327.5

# Scale Length (m)
L = 0.65

# Harmonic number
n = 1

def area(d):
    # String cross-sectional area, m**2
    return π*(d**2)/4

def mass(d,rho,L):
    # Calculate string mass per scale length
    #   rho in kg/m**3
    #   d in m
    #   L in m
    return rho * (π*(d**2)/4) * L

def mu(mass,L):
    # Calculate μ = mass / L
    # linear mass density
    return mass/L

#------------------------------------------------------------------------------
# Tension calculations
#------------------------------------------------------------------------------
def tension_from_frequency_L(n,f,L,mu):
    # Equation 1: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5459001/
    return mu *((2 * f * L)/n)**2

rho = 1070
d = 0.0013
n = 1
f = 98
L = 0.755

mass = mass(d,rho,L)
mu   = mu(mass,L)

T0 = tension_from_frequency_L(n,f,L,mu)

print(mass,mu,T0)

def tension_from_velocity(mu,v):
    return mu*v**2
#------------------------------------------------------------------------------

def velocity_from_tension(T,mu):
    # Wave speed from string tension and mu = mass/L
    # Units: m/s
    return math.sqrt(T/mu)

def mu_from_tension(n,f,L,T):
    return T/(2*f*L/n)**2

def alpha(f,L):
    # Equation 18: α = Lf on page 521
    # Units: m/s**2
    return f*L

def β(d,L):
    # Equation 18: β = d/L on page 521
    # Units: none
    return d/L

def sigma(rho,alpha):
    # Equation 19: String Stress
    # Units: N/m**2 or pascal (Pa)
    return 4 * rho * (alpha**2)

#  σ = F/A

def E(sigma):
    # Equation 16: Young'e Modulous, page 519
    # Units: σ, sigma, is in GPa
    # Ep ≈ 3.2 + 41σ GPa, (fluorocarbon).
    return 4.5 + 39 * sigma + 0.25

def λ(E,d,n,rho,L,f):
    # Equation 7: governs the degree of inharmonicity
    #
    # "λ also governs the degree of inharmonicity of a string. This
    # means that design guidelines based on a threshold value
    # of λ will set a limit on inharmonicity as well as damp-
    # ing. Both damping and inharmonicity have been associ-
    # ated in earlier literature with the perceptual discrimination
    # of “warmth” versus “brightness”. The damping roll-off af-
    # fects the spectral centroid, and there is a well-established
    # correlation of perceived brightness with variation in spec-"
    return ( E * (π**2) * (d**2) * (n**2) ) / ( 64 * rho * (L**4) * (f**2) )

def T(rho,d,alpha):
    # String Tension
    return π * rho * d**2 * alpha

def gama(T,L):
    # Equation 10: the "feel", gama = Fp/δ ≈ 4T/L
    return 4 * T/L

def Z0(d,rho,alpha):
     # Equation 8: Z0 = π rho d**2alpha/2, wave impedance, page 517
     return ( π * (d**2) * rho * alpha )/ 2

m     = mass(d/1000,rho,L)
alpha = alpha(f,L)
T     = T(rho,d,alpha)
gama  = gama(T,L)
β     = β(d,L)
Z0    = Z0(d,rho,alpha)

sigma     = sigma(rho,alpha)
sigma_GPa = sigma/1000000000

print("d =",d, "\narea=",area(d)," \nT/A =",T/area(d))

E     = E(sigma_GPa)

λ  = λ(E,d,n,rho,L,f)

print("\nσ =", sigma_GPa, " (GPa)", "\nE =", E," (GPa)")

print("\nα =",alpha,"\nβ =",β,"\nλ =",λ)

print("rho =",rho,"\nd =",d)
print("T =", T)
#alpha   = np.arange(0., 300., 10.)
#d       = np.arange(0., 0.003, .0001)
#T       = π * rho * d**2 * alpha**2
#Z0      = ( π * (d**2) * rho * alpha )/ 2

#print(alpha,T,d)
#plt.plot( alpha, T)
#plt.show()
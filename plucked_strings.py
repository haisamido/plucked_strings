#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt
import numpy as np

# objectives:
#   code 
#   https://drive.google.com/file/d/19aP8p5_P4ctM7Y8fg74ErdViTrfGOENZ/view?usp=share_link
#

# sources: 
#   https://inside-guitar.com/the-ultimate-guide-to-classical-guitar-strings/
#   https://euphonics.org/publication-list-jim-woodhouse/
#   https://www.ingentaconnect.com/contentone/dav/aaua/2019/00000105/00000003/art00012
#   https://www.ingentaconnect.com/content/dav/aaua/2019/00000105/00000003/art00012#
#   https://drive.google.com/file/d/19aP8p5_P4ctM7Y8fg74ErdViTrfGOENZ/view?usp=share_link
#   https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5459001/
#   https://publicwebuploads.uwec.edu/documents/Musical-string-inharmonicity-Chris-Murray.pdf

pi =math.pi

# String density (kg/m**3)
ρ  = 1070 # nylon

# String diameter (mm)
d = 1

# Frequency (Hz)
f = f1 = 110

# Scale Length
L = 1.0

# Young'e Modulus
E = 1.0

# Harmonic number
n = 1

def m(d,ρ,L):
    return 1

def α(f,L):
     # Equation 18: α = Lf on page 521, Wave speed in string
     return f*L

def β(d,L):
    # Equation 18: β = d/L on page 521
    return d/L

def λ(E,d,n,ρ,L,f):
    # Equation 7: proportion of the potential energy?
    return ( E * (pi**2) * (d**2) * (n**2) ) / ( 64 * ρ * (L**4) * (f**2) )

def σ(ρ,α):
    # Equation 19: String Stress
    return 4 * ρ * (α**2)

def T(ρ,d):
    # Tension
     return pi * ρ * d**2 * α

def γ(T,L):
    # Equation 10: the "feel", γ = Fp/δ ≈ 4T/L
    return 4 * T/L

def Z0(d,ρ,α):
     # Equation 8: Z0 = πρd**2α/2, wave impedance
     return ( pi * (d**2) * ρ * α )/ 2

α  = α(f,L)
λ  = λ(E,d,n,ρ,L,f)
σ  = σ(ρ,α)
T  = T(ρ,d)
γ  = γ(T,L)
β  = β(d,L)
Z0 = Z0(d,ρ,α)

#print(E,α,λ,σ,T,γ,β,Z0)

print(α,β,λ)

#α   = np.arange(0., 300., 10.)
#d       = np.arange(0., 0.003, .0001)
#T       = pi * ρ * d**2 * α**2
#Z0      = ( pi * (d**2) * ρ * α )/ 2

#print(α,T,d)
#plt.plot( α, T)
#plt.show()
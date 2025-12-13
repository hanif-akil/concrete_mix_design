# Mix Design Calculator for Concrete
#importing necessary libraries
import numpy as np

prompt = "\n>>>" # prompt for user input

Gc = float(input(f"Specific gravity of concrete (Gc): 3.15 for OPC and 2.95 for PCC{prompt} ")) 
Gca  = float(input(f"Specific gravity of coarse aggregate (Gca): 2.55 to 2.80{prompt} "))
Gfa = float(input(f"Specific gravity of fine aggregate (Gfa): 2.60 to 2.70{prompt} "))
Gw = 1.00 # specific gravity of water

Yw = 1000 # weight of water in kg/m3

Wc = float(input("Enter the weight of cement per cubic meter of concrete (Wc in kg): "))   # cement content from graphs
w_c = float(input("Enter the water-cement ratio (w/c): "))                                 # wwater-cement ratio from graphs
ww = w_c * Wc

s_a = float(input("Enter the sand-aggregate ratio (s/a): "))

def cement_content (Wc, Gc, Yw):
    Vc = Wc / (Gc * Yw)
    return Vc

def water_content (Ww, Gw, Yw):
    Vw = Ww / (Gw * Yw)
    return Vw

void_per = float(input("enter void percentage: ")) / 100

Vcem = cement_content (Wc, Gc, Yw)
Vwater = water_content (ww, Gw, Yw)

# defining coefficients of equations
# main magic happens here 
a = (s_a) / ( 1 - s_a ) * (Gfa / Gca )
b = 1 / (Gca * Yw) 
c = 1 / (Gfa * Yw) 
z = 1 - Vcem - Vwater - void_per


A = np.array([[1 , -a], [c, b]])
B = np.array([0 , z])

solve = np.linalg.solve(A, B)

print(f"weight of fine aggregate per cubic meter of concrete is {solve[0]} kg")
print(f"weight of coarse aggregate per cubic meter of concrete is {solve[1]} kg")
print(f"weight of water per cubic meter of concrete is {ww} kg")
print(f"weight of cement per cubic meter of concrete is {Wc} kg")
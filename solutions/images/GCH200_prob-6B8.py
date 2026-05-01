# -*- coding: utf-8 -*-
"""
Seulement en régime de Stokes ici.

Created on Mon Apr 18 11:20:33 2016
@author: Pierre Proulx
"""
import sympy as sp
from IPython.display import *
sp.init_printing(use_latex=True)
# Paramètres, variables et fonctions
rho_s,rho,D,v_inf,mu,g=sp.symbols('rho_s,rho,D,v_inf,mu,g')  
f_f=4/3*g*D/v_inf**2*(rho_s-rho)/rho  # equation définissant le facteur f
display(f_f)
Re=rho*v_inf*D/mu                           
f_v=(sp.sqrt(24/Re)+0.5407)**2        
display(f_v)
f=f_f-f_v
R=sp.solve((f,0),D)/2
display(R)
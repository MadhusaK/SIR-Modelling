SIR-Modelling
=============

SIR (Susceptible, Infected, and Recovered) Model for a ficticious virus. No Births or Deaths. Chance of reinfection, gamma.

DE's:

dS/dt = -alpha*S*I + gamma*R - delta*S  
dI/dt = alpha*S*I - beta*I  
dR/dt = beta*I - gamma*R + delta*S  

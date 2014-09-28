SIR-Modelling
=============

Standard simple SIR (Susceptible, Infected, and Recovered) Model for a ficticious virus. No Births or Deaths.

DE's:

dS/dt = -alpha*S*I + gamma*R - delta*S  
dI/dt = alpha*S*I - beta*I  
dR/dt = beta*I - gamma*R + delta*S  

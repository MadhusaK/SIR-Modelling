SIR-Modelling
=============

Standard simple SIR (Susceptible, Infected, and Recovered) Model for a ficticious virus. No Births or Growths.

DE's:

S' = -alpha*S*I + gamma*R - delta*S
I' = alpha*S*I - beta*I
R' = beta*I - gamma*R + delta*S

SIR-Modelling
=============

Standard Modeling of the SIR (Susceptible, Infected, and Recovered) Model for a ficticious virus. 

DE's:

S' = -alpha*S*I + gamma*R - delta*S
I' = alpha*S*I - beta*I
R' = beta*I - gamma*R + delta*S

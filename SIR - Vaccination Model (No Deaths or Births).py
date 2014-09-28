import scipy.integrate
import numpy
import matplotlib.pyplot as pyplot
import SIRVariables as var

# Parameters
t_ini = 0.0
t_end = 200.0
t_inc = 1.0
t_rng = numpy.arange(t_ini,t_end,t_inc)

alpha = var.alpha
beta = var.beta
gamma = var.gamma
delta = var.delta

S0 = 0.99
I0 = 0.01
R0 = 0.00
initial_pop = (S0, I0, R0)

# System of equations - S,I, and R
def diff_SIR(SIR,t):
    ''' ODE's for S, I, R with Vaccinations '''
    
    output_SIR = numpy.zeros(3)
    
    # S' = -alpha*S*I + gamma*R - delta*S
    # I' = alpha*S*I - beta*I
    # R' = beta*I - gamma*R + delta*S
    
    output_SIR[0] = -alpha*SIR[0]*SIR[1] + gamma*SIR[2] - delta*SIR[2]
    output_SIR[1] = alpha*SIR[0]*SIR[1] - beta*SIR[1]
    output_SIR[2] = beta*SIR[1] - gamma*SIR[2] + delta*SIR[2]
    
    return output_SIR

# Plotting trajectory

sol = scipy.integrate.odeint(diff_SIR,initial_pop,t_rng)

pyplot.subplot(211)
pyplot.plot(sol[:,0],'-g',label='Susceptibles')
pyplot.plot(sol[:,1],'-k',label='Infected')

print "Survivors: %s" % sol[-1,0]
print "Infected: %s" %sol[-1,1]
print "Recovered: %s" % sol[-1,2]




    

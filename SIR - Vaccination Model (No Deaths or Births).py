import scipy.integrate
import numpy
import matplotlib.pyplot as pyplot
import SIRVariables as var

# Parameters
t_ini = 0.0
t_end = 70.0
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

x_max = 1
x_min = 0
y_max = 1
y_min = 0
points = 20
x = numpy.linspace(x_min,x_max,points)
y = numpy.linspace(y_min,y_max,points)
X,Y = numpy.meshgrid(x,y)
S_vecField = numpy.zeros(len(X))
I_vecField = numpy.zeros(len(Y))

# System of equations - S,I, and R
def diff_SIR(SIR,t=0):
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

pyplot.hold()
pyplot.figure(1)
pyplot.plot(sol[:,0],'-g',label='Susceptibles')
pyplot.plot(sol[:,1],'-b',label='Infected')
pyplot.plot(sol[:,2],'-r',label='Recovered')
pyplot.legend(loc=0)
pyplot.title('SIR - Change over time')
pyplot.xlabel('Time')
pyplot.ylabel('Population')
pyplot.hold()
pyplot.show()


print "Susceptible: %s" % sol[-1,0]
print "Infected: %s" %sol[-1,1]
print "Recovered: %s" % sol[-1,2]

# Plotting Vector Field
for i in range(0,len(X)):
    sol_Prime = diff_SIR(X[1],Y[1])
    S_vecField = sol_Prime[0]
    I_vecField = sol_Prime[1]
    
pyplot.figure(2)
pyplot.quiver(X,Y,S_vecField,I_vecField)   
pyplot.hold()

for j in numpy.arange(0,1,0.1):
    sol = scipy.integrate.odeint(diff_SIR,[1-j,0.2,j],t_rng)
    pyplot.plot(sol[:,0],sol[:,1])


pyplot.hold()



    

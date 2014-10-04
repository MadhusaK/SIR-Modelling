import scipy.integrate
import numpy
import matplotlib.pyplot as pyplot


# Parameters
t_ini = 0.0
t_end = 300.0
t_inc = 1.0
t_rng = numpy.arange(t_ini,t_end,t_inc)

alpha = 0.2
beta = 0.1
gamma = 0.05
delta = 0

I0 = (1/2.043)*10**(-6)
S0 = 1-I0
R0 = 0.00
initial_pop = (S0, I0, R0)

x_max = 1
x_min = 0
y_max = 1
y_min = 0
points = 25
x = numpy.linspace(x_min,x_max,points)
y = numpy.linspace(y_min,y_max,points)
X,Y = numpy.meshgrid(x,y)
S_vecField = numpy.zeros(X.shape)
I_vecField = numpy.zeros(Y.shape)

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
    
def diff_SI(SI,t=0):
    output_SI = numpy.zeros(2)
    
    # S' = alpha*S*I + gamma*(1 - S - I)
    # I' = alpha*S*I - beta*I
    
    output_SI[0] = -alpha*SI[0]*SI[1] + gamma*(1 - SI[0] - SI[1])
    output_SI[1] = alpha*SI[0]*SI[1] - beta*SI[1]    
    
    return output_SI

# Plotting trajectory

sol = scipy.integrate.odeint(diff_SIR,initial_pop,t_rng)

pyplot.hold(True)
pyplot.figure(1)
pyplot.plot(sol[:,0],'-g',label='Susceptibles')
pyplot.plot(sol[:,1],'-b',label='Infected')
pyplot.plot(sol[:,2],'-r',label='Recovered')
pyplot.legend(loc=0)
pyplot.title('SIR - Change over time')
pyplot.xlabel('Time')
pyplot.ylabel('Population')
pyplot.hold(False)
pyplot.show()


print "Susceptible: %s" % sol[-1,0]
print "Infected: %s" %sol[-1,1]
print "Recovered: %s" % sol[-1,2]

# Plotting Vector Field
for i in range(points):
    for j in range(points):
        X_mesh = X[i,j]
        Y_mesh = Y[i,j]

        sol_Prime = diff_SI([X_mesh,Y_mesh,])
        S_vecField[i,j] = sol_Prime[0]
        I_vecField[i,j] = sol_Prime[1]


    
pyplot.figure(2)
pyplot.hold(True)
pyplot.quiver(X,Y,S_vecField,I_vecField)   
pyplot.xlabel('Susceiptible')
pyplot.ylabel('Infected')
pyplot.ylim(0,1)
pyplot.xlim(0,1)

for j in numpy.arange(0,0.1,0.05):
    sol = scipy.integrate.odeint(diff_SI,[1-j,j],t_rng)
    pyplot.plot(sol[:,0],sol[:,1], label ='S =%s, I =%s' %(1,1))

for j in numpy.arange(0,1,0.1):
    sol = scipy.integrate.odeint(diff_SI,[1-j,j],t_rng)
    pyplot.plot(sol[:,0],sol[:,1], label = 'S')


sol = scipy.integrate.odeint(diff_SI,[0.4,0.01],t_rng)
pyplot.plot(sol[:,0],sol[:,1],'-b')


pyplot.hold(False)



    


from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# ode function
def my_ode(y, t, a, b):
    y0, y1 = y
    diff = [a*(y0 -y0*y1),
            b*(-y1+y0*y1)]
    
    return diff

# initialize variables
end_year = 5
count_of_years = end_year + 1
y0_initial = 0.1
y1_initial = 1.0
a = 1
b = 0.2

# initialize arguments
t = np.linspace(0, end_year, count_of_years)
y0_vector = np.array([y0_initial, y1_initial])

# solve ode and obtain array of values
sol = odeint(my_ode, y0_vector, t, args=(a, b))

# plotting y0=0.1 and y1 against t
plt.subplot(121)
y0_col = 0
y1_col = 1
plt.plot(t, sol[:, y0_col], 'b', label=r'$y_0$')
plt.plot(t, sol[:, y1_col], 'r', label=r'$y_1$')
plt.title('$y_0$ = %f'%( y0_initial ) )
plt.legend(loc='best')
plt.xlabel('$t$')
plt.ylabel('$y$')

#plotting y1 agaisnt y0=0.1
plt.subplot(122)
plt.plot(sol[:,y0_col],sol[:,y1_col],'g',label='Predator y1 against Prey y0')
plt.title('Predator y1 against Prey y0=0.1')
plt.legend(loc='best')
plt.xlabel('$y_0$=%f'%(y0_initial))
plt.ylabel('$y$')

#######

# changing y0_initial
y0_initial = 0.11
y0_vector = np.array([y0_initial, y1_initial])

# solving 
sol = odeint(my_ode, y0_vector, t, args=(a,b))

# plotting y0=0.11 and y1 against t
plt.figure()
plt.subplot(121)
y0_col = 0
y1_col = 1
plt.plot(t, sol[:, y0_col], 'b', label=r'$y_0$')
plt.plot(t, sol[:, y1_col], 'r', label=r'$y_1$')
plt.title('$y_0$ = %f'%( y0_initial ) )
plt.legend(loc='best')
plt.xlabel('$t$')
plt.ylabel('$y$')

#plotting y1 agaisnt y0=0.11
plt.subplot(122)
plt.plot(sol[:,y0_col],sol[:,y1_col],'g',label='Predator y1 against Prey y0')
plt.title('Predator y1 against Prey y0=0.11')
plt.legend(loc='best')
plt.xlabel('$y_0$=%f'%(y0_initial))
plt.ylabel('$y$')
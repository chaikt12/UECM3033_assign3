import numpy as np
import sympy as sy
#Your optional code here
#You can import some modules or create additional functions

# DO NOT CHANGE THE NAME OF gausslegendre() function
def gausslegendre(f, a, b, n=20):
    ans = 0
    # wf is the weight multiple by the function f(y)
    wf=0 
    #Sn is sample point, W is weight
    [Sn,W]=np.polynomial.legendre.leggauss(n)       
    i=1
    for i in range(n):
       y=((b-a)/2)*Sn[i]+((a+b)/2)
       wf+=W[i]*f(y)
    ans=((b-a)/2)+wf
    return ans




if __name__ == "__main__":
    def f(x):
        return (x**2 +7*x)/(1 +np.sqrt(x))**4
    
    def my_integral():
        x = sy.Symbol('x')
        ans = sy.integrate((x**2 +7*x)/(1 +sy.sqrt(x))**4, (x,0, 1))
        return ans
    
    print('Answer:                    I = ', my_integral())
    print('Your implementation gives: I = ', gausslegendre(f, 0,1))

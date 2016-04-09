UECM3033 Assignment #3 Report
========================================================

- Prepared by: ** Chai Kun Ting**
- Tutorial Group: T3

--------------------------------------------------------

## Task 1 --  Gauss-Legendre formula

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/chaikt12/UECM3033_assign3.git](https://github.com/chaikt12/UECM3033_assign3.git)


Explain how you implement your `task1.py` here.
In the task1, the define function gausslegendre will take in function, f(x) , lower and upper limit, a and b, and the n. The answer is set to be 0 initially. The weight multiple by the function is defined to be wf and it is initialize to be 0. then the sample point and the weight is calculated by a module which will be discuss below. Next, it will move into a for loop to sum up all n times of weight multiple by the function. Noted that due to the lower and upper limit is not -1 to 1, thus we will nid to change the interval into -1 to 1. It become $$\int_a^{b} f(x) dx = \frac{b-a}{2}\int_{-1}^{1} f(\frac{b-a}{2}x+\frac{a+b}{2}) dx.$$ 
At the main function part, the integration is defined and calculated using sympy.integrate and the self defined gausslegendre function.
Explain how you get the weights and nodes used in the Gauss-Legendre quadrature.
the weight and node can be obtained by numpy..polynomial.legendre.leggauss. It will return sample point and weight in the form of array. 
---------------------------------------------------------

## Task 2 -- Predator-prey model

Explain how you implement your `task2.py` here, especially how to use `odeint`.


Put your graphs here and explain.

Is the system of ODE sensitive to initial condition? Explain.

-----------------------------------

<sup>last modified: change your date here</sup>

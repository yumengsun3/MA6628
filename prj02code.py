# Application of BSM evaluation to Geometric asian option price

import numpy as np
import scipy.stats as ss
import math
import time

S0 = 100.0 #initial stock price
K = 110.0 #strike
r=0.0475 #interest rate
sigma = 0.20 #vol
T = 1. #maturity
Otype='C' #Call type
n = 4 #number of periods
t = np.linspace(0., T, n+1)[1:] #times to be used for geometric averaging stock price 
def d1f(St, K, t, T, r, sigma):
    ''' Black-Scholes-Merton d1 function.
    Parameters see e.g. BSM_call_value function. '''
    d1 = (math.log(St / K) + (r + 0.5 * sigma ** 2)
            *(T - t)) / (sigma * math.sqrt(T - t))
    return d1

def BSM_call_value(St, K, t, T, r, sigma):
    ''' Calculates Black-Scholes-Merton European call option value.
    Parameters
    ==========
    St : float
        stock/index level at time t
    K : float
        strike price
    t : float
        valuation date
    T : float
        date of maturity/time-to-maturity if t = 0; T > t
    r : float
        constant, risk-less short rate
    sigma : float
        volatility
    Returns
    =======
    call_value : float
        European call present value at t
    '''
        
    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T - t)
    call_value = St * ss.norm.cdf(d1) - math.exp(-r * (T - t)) * K * ss.norm.cdf(d2)
    return call_value

# recall the relationship and calculate sigma_ht and r_ht for GAC price by BSM

sigma_ht=sigma/n*math.sqrt((n+1)*(2*n+1)/6)#This is the relationship between sigma_ht and sigma 
r_ht=1/2*sigma_ht**2+(n+1)*(r-1/2*sigma**2)/(2*n)#This is the relationship between r_ht and t
GAC_price=math.exp(r_ht*T-r*T)*BSM_call_value(S0, K, 0, T, r_ht, sigma_ht)
print('GAC price by BSM= ', GAC_price)

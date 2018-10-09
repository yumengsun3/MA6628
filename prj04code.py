%reset -f
#The difference between BSM call price and market call price
import numpy as np
import scipy.stats as ss
import scipy.optimize as so
import math
import time

Today = np.datetime64('2018-09-27')#
Maturity = np.datetime64('2018-12-31')
T = (Maturity - Today)/np.timedelta64(1,'D')/365 #time to maturity in year
S0 = 290.68 #Spot price
K = 288.#strike
r = 0.02 #interest rate
sigma = 0.3
Call = 9.23 

def d1f(St, K, t, T, r, sigma):
    ''' Black-Scholes-Merton d1 function.
    Parameters see e.g. BSM_call_value function. '''
    d1 = (math.log(St / K) + (r + 0.5 * sigma ** 2)
            *(T - t)) / (sigma * math.sqrt(T - t))
    return d1
def BSM_call_value(St, K, t, T, r, sigma):
    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T - t)
    call_value = St * ss.norm.cdf(d1) - math.exp(-r * (T - t)) * K * ss.norm.cdf(d2)
    return call_value

BSM_call_value = BSM_call_value(S0, K, 0, T, r, sigma)
print('the BSM call price with volatility 30% =', BSM_call_value)

Difference = BSM_call_value - Call 
print('the difference between BSM call price and market call price with 30% vol=', Difference)

#Compute the implied volatility 
#Script is shown below
%cat ImpliedVolatility.py

import numpy as np
from ImpliedVolatility import IVolBsm
print('Implied volatility is %f' %IVolBsm(S0, K, T, r, Call))#with the volatility=11.8%, the BSM call price=market call price #Market call price #with the volatility=11.8%, the BSM call price=market call price

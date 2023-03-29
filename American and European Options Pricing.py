import math
#############################################################################################################################################
dict = {'strike' : 100, 'price' : 100, 'time steps' : 10, 'sigma': 0.2, 'years': 1, 'risk-free rate': 0.04, 'dividend': 0.02, 
        'callput': 1, 'AmerEu': -1}
Tstep = dict['time steps']
# call = 1, put = -1; in callput
# American = 1, European = -1; in AmerEu

u = math.exp(dict['sigma']*math.sqrt(1/dict['time steps']))
d = 1/u
probup = (((math.exp((dict['risk-free rate']-dict['dividend'])*dict['years']/dict['time steps'])) - d) / (u - d))
discount_factor = dict['risk-free rate']/dict['time steps']
duration_of_time_step = float(dict['years']/dict['time steps'])

if dict['callput'] > 0:
    type = 'call'
else:
    type = 'put'
if dict['AmerEu'] > 0:
    exercise = 'American'
else:
    exercise = 'European'
    #############################################################################################################################################  

def binomial():
    Tstep = dict['time steps']
    
    payoffs = []
    n = 0
    while n < (Tstep + 1): 
        payoffs.append(max(0, dict['callput']*(dict['price']*(u**((Tstep)-n))*(d**n) - dict['strike'])))
        n += 1
    print(exercise, type,'payoffs at expiration are', payoffs)
    
    while Tstep >= 1:
#############################################################################################################################################
    # not used in the actual calculation but useful to see what the probabilities of each node is at a specific timestep    
        def combos(n, i):
            return math.factorial(n) / (math.factorial(n-i)*math.factorial(i))

        pascal = []
        for i in range(Tstep+1):
            pascal.append(combos(Tstep, i))

        probabilities = []
        i = 0
        for i in range(Tstep+1):
            probabilities.append(pascal[i]*(probup**((Tstep)-i))*((1-probup)**i))
            i += 1
#############################################################################################################################################
        discounting1 = []
        i = 0
        while i < (Tstep):
            if dict['AmerEu'] == 1:
                American_payoff = (dict['callput']*(dict['price']*(u**(Tstep-i-1)*(d**i)) - dict['strike']))
                European_payoff = (((probup)*payoffs[i]) + ((1-probup)*payoffs[i+1])) / (math.exp(discount_factor))
                discounting1.append(max(American_payoff, European_payoff))
            elif dict['AmerEu'] == -1:
                discounting1.append((((probup)*payoffs[i]) + ((1-probup)*payoffs[i+1]))
                                    / (math.exp(discount_factor)))
            else:
                pass
            i += 1  
            
        payoffs.clear()
        payoffs.extend(discounting1)
        
        delta_calculation = []
        if len(payoffs) == 2: 
            delta_calculation.extend(payoffs)
            delta = (delta_calculation[0] - delta_calculation[1]) / (dict['price']*u - dict['price']*d)    
        else:
            pass
        
        delta_for_gamma = []
        if len(payoffs) == 3: 
            theta_calculation = float(payoffs[1])
            delta_for_gamma.extend(payoffs)
            gamma = ((((delta_for_gamma[0] - delta_for_gamma[1]) / (dict['price']*(u**2) - dict['price']*u*d)) - 
                    ((delta_for_gamma[1] - delta_for_gamma[2]) / (dict['price']*u*d - dict['price']*(d**2)))) 
                                    / (dict['price']*u - dict['price']*d))   
        else:
            pass
        Tstep -= 1
    
    theta = float(discounting1[0] - theta_calculation) / float(2*(duration_of_time_step))
    daily_theta_decay = theta/365
    return f"The price of the {exercise} {type} option is {discounting1[0]}; while its theta is {round(theta, 2)}, daily theta decay is {round(daily_theta_decay, 3)}, delta is {round(delta, 2)}, and gamma is {round(gamma, 2)}"

print(binomial())
       


def vega():
    vega_calculation = []
    return 
    
def rho():
    rho_calculation = []
    return
    
    
# need to find how to calculate vega and rho, which are dependent on volatility and interest rate




###############################################################################################################################################

# Overall, the difference between the American and European option is changed the most when changing the dividend rate, 
# and the effect is felt more strongly by put options than call options 

# The put-call symmetry argument is dependent on Geometric Brownian motion, which gives a generally lognormal curve when modelling 
# stock prices; the equation for the model states that the put option of interest rate=x and dividend rate =y 
# is the same as a call option with r=y and div=x, assuming all other parameters are the same.

# as of current mathematical analysis, the put-call symmetry does not explicitly work in the binomial model,
# only for the black-scholes is there a formula, which only works with the Black-Scholes model since it depeends on GBM and a lognormal stock price distribution


# no arbitrage in the binomial model is when the interest rate is between u and d


# the european call option in the binomial model converges to the black-scholes equation
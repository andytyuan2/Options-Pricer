import math
#############################################################################################################################################
dict = {'strike' : 100, 'price' : 100, 'time steps' : 10, 'sigma': 0.2, 'years': 1, 'risk-free rate': 0.04, 'dividend': 0.02, 
        'callput': 1, 'AmerEu': -1}
# call = 1, put = -1; in callput
# American = 1, European = -1; in AmerEu
u = math.exp(dict['sigma']*math.sqrt(1/dict['time steps']))
print('up move is', u)
d = 1/u
print('down move is', d)
probup = (((math.exp((dict['risk-free rate']-dict['dividend'])*dict['years']/dict['time steps'])) - d) / (u - d))
print('probability of an up move is', probup)
print('probability of a down move is', (1-probup))
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
def binomial(strike, price, time_steps, sigma, riskfree_rate, years, dividend):
    payoffs = []
    n = 0
    while n < dict['time steps'] + 1: 
        payoffs.append(max(0, dict['callput']*(dict['price']*(u**((dict['time steps'])-n))*(d**n) - dict['strike'])))
        n += 1
    print(exercise, type,'payoffs at expiration are', payoffs)
    
    dict['time steps']
    while dict['time steps'] >= 1:
#############################################################################################################################################
    # not used in the actual calculation but useful to see what the probabilities of each node is at a specific timestep    
        def combos(n, i):
            return math.factorial(n) / (math.factorial(n-i)*math.factorial(i))

        pascal = []
        for i in range(dict['time steps']+1):
            pascal.append(combos(dict['time steps'], i))

        probabilities = []
        i = 0
        for i in range(dict['time steps']+1):
            probabilities.append(pascal[i]*(probup**((dict['time steps'])-i))*((1-probup)**i))
            i += 1
#############################################################################################################################################
        discounting1 = []
        i = 0
        while i < (dict['time steps']):
            if dict['AmerEu'] == 1:
                American_payoff = (dict['callput']*(dict['price']*(u**(dict['time steps']-i-1)*(d**i)) - dict['strike']))
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
            print(exercise, type, 'option delta is', delta)
        else:
            pass
        
        delta_for_gamma = []
        if len(payoffs) == 3: 
            theta_calculation = float(payoffs[1])
            delta_for_gamma.extend(payoffs)
            gamma = ((((delta_for_gamma[0] - delta_for_gamma[1]) / (dict['price']*(u**2) - dict['price']*u*d)) - 
                      ((delta_for_gamma[1] - delta_for_gamma[2]) / (dict['price']*u*d - dict['price']*(d**2)))) 
                                    / (dict['price']*u - dict['price']*d))
            print(exercise, type, 'option gamma is', gamma)
        else:
            pass
        
        dict['time steps'] -= 1
        
    theta = float(discounting1[0] - theta_calculation) / float(2*(duration_of_time_step))
    print(exercise, type, 'option theta is', theta)
    daily_theta_decay = theta/365
    print(exercise, type, 'option daily theta decay is', daily_theta_decay)
    return discounting1

# need to find how to calculate vega and rho, which are dependent on volatility and interest rate

print(exercise, type, 'option price at t=0 is', binomial(dict['strike'], dict['price'], dict['risk-free rate'], dict['sigma'], dict['time steps'], dict['years'], dict['dividend']))

# Overall, the difference between the American and European option is changed the most when changing the dividend rate, 
# and the effect is felt more strongly by put options than call options 

# no arbitrage in the binomial model is when the interest rate is between u and d
# the european call option in the binomial model converges to the black-scholes equation

import math
#########################################################################################################################################################################
dict = {'strike' : 100, 'price' : 1, 'time steps' : 10, 'sigma': 0.2, 'years': 1, 'risk-free rate': 0.04, 'dividend': 0.02, 
        'callput': -1, 'AmerEu': -1}

# call = 1, put = -1; in callput
# American = 1, European = -1; in AmerEu

Prices_different_rates = []

while dict['price'] < 300: 
    u = math.exp(dict['sigma']*math.sqrt(dict['years']/dict['time steps']))
    d = 1/u
    probup = (((math.exp((dict['risk-free rate']-dict['dividend'])*dict['years']/dict['time steps'])) - d) / (u - d))
    discount_factor = dict['risk-free rate']/dict['time steps']
    duration_of_time_step = (dict['years']/dict['time steps'])

    if dict['callput'] > 0:
        type = 'call'
    else:
        type = 'put'
    if dict['AmerEu'] > 0:
        exercise = 'American'
    else:
        exercise = 'European'
    #########################################################################################################################################################################
    def binomial():
        Tstep = dict['time steps']
        payoffs = []
        n = 0
        while n < (Tstep + 1): 
            payoffs.append(max(0, dict['callput']*(dict['price']*(u**((Tstep)-n))*(d**n) - dict['strike'])))
            n += 1
        
        while Tstep >= 1:
    #########################################################################################################################################################################
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
    #########################################################################################################################################################################
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
            
            Tstep -= 1
        return discounting1
    if binomial()[0] >= 0:
        Prices_different_rates.append(binomial()[0])
    else:
        Prices_different_rates.append(0)
    dict['price'] += 1
    
print(Prices_different_rates)

# The put-call symmetry argument is dependent on Geometric Brownian motion, which gives a generally lognormal curve when modelling stock prices; 
# the equation for the model states that the put option of interest rate=x and dividend rate =y,
# is the same as a call option with rate=y and dividend=x, assuming all other parameters are the same.

# As of current mathematical analysis, the put-call symmetry does not explicitly work in the binomial model,
# only for the black-scholes is there a formula, which only works with the Black-Scholes model since it depeends on GBM and a lognormal stock price distribution

# No arbitrage in the binomial model is when the interest rate is between u and d
# The european call option in the binomial model converges to the black-scholes equation

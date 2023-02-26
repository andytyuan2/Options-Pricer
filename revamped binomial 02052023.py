import math

dict = {'strike' : 90, 'price' : 100, 'time steps' : 10, 'sigma': 0.1, 'risk-free rate': 0.04, 'years': 1, 'dividend': 0.2}
# there is an implication that the time steps are the number of exercises I am considering a year 
u = math.exp(dict['sigma']* (math.exp(dict['years']/dict['time steps'])))
print('up move is', round(u, 3))
d = math.exp(-dict['sigma']* (math.exp(dict['years']/dict['time steps'])))
print('down move is', round(d, 3))
probup = (((math.exp((dict['risk-free rate']-dict['dividend'])*dict['years']/dict['time steps'])) - d) / (u - d))
print('probability of moving up is', round(probup, 3))

# ^^^ this portion describes the up and down moves as well as the independent probability of an up move, similar to the CRR parameter setup from the MATLAB example

def binomial(price, time_steps, sigma, riskfree_rate, years):
    payoffs = []
    n = 0
    while n < dict['time steps'] + 1: 
        payoffs.append (round(max(0, dict['price']*(u**((dict['time steps'])-n))*(d**n) - dict['strike']), 2))
        n += 1
    print('payoffs at specified time step are', payoffs) 
    dict['time steps']
    while dict['time steps'] >= 1:
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

        discounting1 = []
        i = 0
        while i < (dict['time steps']):
            discounting1.append((((probabilities[i] /        (probabilities[i]+probabilities[i+1]))*payoffs[i]) + 
                                 ((probabilities[i+1]   /      (probabilities[i]+probabilities[i+1]))*payoffs[i+1]))
                                    / (math.exp(dict['risk-free rate']/dict['time steps'])))
            i += 1   
        print('discounted payoffs at time =', (dict['time steps'] - 1), 'are', discounting1)
        
        payoffs.clear()
        payoffs.extend(discounting1)
        
        dict['time steps'] -= 1
    return discounting1

# this loop starts off with the payoffs at the pre-determined time step, then discounts it back towards t=0

print('option price at t=0 is', binomial(dict['price'], dict['risk-free rate'], dict['sigma'], dict['time steps'], dict['years']))
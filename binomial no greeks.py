import math
#####################################################################################################################################################################################
dict = {'strike' : 100, 'price' : 90, 'time steps' : 10, 'sigma': 0.1, 'years': 1, 'risk-free rate': 0.02, 'dividend': 0.04, 
        'callput': -1, 'AmerEu': 1}
# call = 1, put = -1; in callput
# American = 1, European = -1; in AmerEu

u = math.exp(dict['sigma']*math.sqrt(dict['years']/dict['time steps']))
d = 1/u
probup = (((math.exp((dict['risk-free rate']-dict['dividend'])*dict['years']/dict['time steps'])) - d) / (u - d))
discount_factor = dict['risk-free rate']/dict['time steps']
duration_of_time_step = (dict['years']/dict['time steps'])

if dict['callput'] > 0:
    type = 'calls'
else:
    type = 'puts'
if dict['AmerEu'] > 0:
    exercise = 'American'
else:
    exercise = 'European'
##################################################################################################################################################################################### 
def binomial():
    Tstep = dict['time steps']
    payoffs = []
    for n in range(Tstep +1): 
        payoffs.append(max(0, dict['callput']*(dict['price']*(u**((Tstep)-n))*(d**n) - dict['strike'])))     
    while Tstep >= 1:
#####################################################################################################################################################################################
    # not used in the actual calculation but useful to see what the probabilities of each node is at a specific timestep    
        def combos(n, i):
            return math.factorial(n) / (math.factorial(n-i)*math.factorial(i))

        pascal = []
        for i in range(Tstep+1):
            pascal.append(combos(Tstep, i))

        probabilities = []
        for i in range(Tstep+1):
            probabilities.append(pascal[i]*(probup**((Tstep)-i))*((1-probup)**i))
#####################################################################################################################################################################################
        discounting1 = []
        i = 0
        for i in range(0,Tstep):
            if dict['AmerEu'] == 1:
                American_payoff = (dict['callput']*(dict['price']*(u**(Tstep-i-1)*(d**i)) - dict['strike']))
                European_payoff = (((probup)*payoffs[i]) + ((1-probup)*payoffs[i+1])) / (math.exp(discount_factor))
                discounting1.append(max(American_payoff, European_payoff))
            elif dict['AmerEu'] == -1:
                discounting1.append((((probup)*payoffs[i]) + ((1-probup)*payoffs[i+1]))
                                    / (math.exp(discount_factor)))
            else:
                pass 
                
        payoffs.clear()
        payoffs.extend(discounting1)
        Tstep -= 1

    return discounting1

print(exercise, type, "option price is $", binomial()[0])

#####################################################################################################################################################################################

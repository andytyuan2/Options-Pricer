# The Binomial Options Pricing Model, in Python

## Synopsis and Background

This is the CRR binomial pricing model for both American and European options; using python. Written by Andy Yuan (me) in 2023 at Western University with the mathematical support of professor Lars Stentoft. At the time I was in my third year of a 4-year bachelor's degree, majoring in accounting and applied statistics. This project was a testing point to apply my newfound Python and quantitative finance knowledge. 

Thank you for reading!

## Guide to Use of Files

### Main File
The [main file](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/blob/main/Main%20File.py) that includes Greeks and Probabilities has a variety of functions. It calculates all the Greeks, some by using the tree and some by using finite differences (derivatives). Additionally, the probabilities of the individual nodes at payoff according to the binomial distribution is calculated. 

### Option Price Parameter Effect folder
The [option price effect](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/tree/main/Option%20Price%20Parameter%20Effect) folder examines the option price sensitivity to changes in those parameters. 

     The default parameters are:

    - Option Strike = $100
    - Underlying Asset Price = $100
    - Implied Volatility = 20%
    - Time to Expiry (Years) = 1 year
    - Risk-Free Rate = 4%
    - Continuous Dividend Yield = 2%
    - Time Steps in the Tree = 10 steps

### Excel File of Sensitivity Data 
The data I pulled from the sensitivity analysis is within the [Excel File](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/blob/main/Excel%3B%20Options%20Price%20Sensitivity%20Analysis.xlsm). 
- Just to note, most of the parameter sensitivities do not have an imposed decimal limit on the ending option price, but the risk-free rate sensitivity analysis does. For the analysis without the risk-neutral adjustment: the European call has a 2 decimal place limit; the European put and American call/put have a 3 decimal place limit. For the file with the risk-neutral adjustment, there is a 5 decimal limit.

- The reason why the decimal place limits exist is because I modeled the prices up to 400% risk-free rate. The graph for that would be essentially useless however, so I only captured the relevant portion for this repository.

### Other Files
The other three files: [American Options Only](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/blob/main/American%20Options%20Only.py), [European Options Only](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/blob/main/European%20Options%20Only.py), and [Adjusted Tree with Real-World Drift](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/blob/main/Adjusted%20Tree%20with%20Real-World%20Drift.py) are supportive to the main file. 
- The European Options Only file runs through only the European method of valuing the option, only taking the discounted version of the payoffs
- The American Options Only file is similar to the European method of valuing the option, but takes into account the payoff at the specific time step. It chooses the maximum of the discounted payoffs and the payoff at exercise.
- The Adjusted Tree differentiates itself from the main file by changing how the up and down movements are calculated. In tandem, it also changes the respective probabilities of up and down movement.
  - Up, down, probability calculation without risk-neutral adjustment:
    - ``u = math.exp(dict['sigma']*math.sqrt(dict['years']/dict['time steps']))``
    - ``d = 1/u``
    - ``probup = (((math.exp((dict['risk-free rate']-dict['dividend'])*dict['years']/dict['time steps'])) - d) / (u - d)) ``
    - ``probdown = 1-probup``
  - Up, down, probability calculation with risk-neutral adjustment:
    - ``u = math.exp((math.log(dict['strike']) - math.log(dict['price']))/dict['time steps'] + dict['sigma']*math.sqrt(dict['years']/dict['time steps']))``
    - ``d = math.exp((math.log(dict['strike']) - math.log(dict['price']))/dict['time steps'] - dict['sigma']*math.sqrt(dict['years']/dict['time steps']))``
    - ``probup = (((math.exp((dict['risk-free rate']-dict['dividend'])*dict['years']/dict['time steps'])) - d) / (u - d))``
    - ``probdown = 1-probup``

## Sensitivity Graphs
> Y-axis is the option price, X-axis is the parameter being changed

### Risk-Free Rate without Risk-Neutral Drift Adjustment:
![image](https://user-images.githubusercontent.com/125106540/231875230-f2ddda38-612e-4ca4-85e9-ec3cb476141a.png)

### Risk-Free Rate with Risk-Neutral Drift Adjustment:
![image](https://user-images.githubusercontent.com/125106540/231875608-c4b39b7b-c168-4538-9c80-59d77b51a6d4.png)

### Risk-Free Rate with Risk-Neutral Drift Adjustment, up to 75% risk-free rate:
![image](https://user-images.githubusercontent.com/125106540/233242638-5295569d-f0d6-4c65-85f7-0e833e1af761.png)

### Risk-Free Rate with Risk-Neutral Drift Adjustment, up to 5% risk-free rate:
![image](https://user-images.githubusercontent.com/125106540/233242870-f3f23069-184b-4d87-bf6c-a8ed890048d1.png)

### Dividend Yield:
![image](https://user-images.githubusercontent.com/125106540/231875795-c2f0400f-18a0-423f-977b-d3e5aa03cff3.png)

### Volatility:
![image](https://user-images.githubusercontent.com/125106540/231027488-6fbbca4e-db94-4918-9d8c-5d1ec22c9065.png)

### Years / Time to Expiry:
![image](https://user-images.githubusercontent.com/125106540/231875908-f597c952-0912-4f1a-968f-2ef51aa1a8b7.png)

### Time Steps:
![image](https://user-images.githubusercontent.com/125106540/231875992-9d56cb0a-ef20-41d4-861b-3bd7c5e3dd12.png)

### Option Strike:
![image](https://user-images.githubusercontent.com/125106540/231876066-e1cf0338-a5d3-4ba7-a7c7-444ba494379c.png)

### Underlying Price:
![image](https://user-images.githubusercontent.com/125106540/231876195-f7a7d929-d7d1-43b6-82f2-e5e654c5be03.png)

<!-- ## Thoughts on the Graphs
### Risk-Free Rate without Risk-Neutral Drift Adjustment
### Risk-Free Rate with Risk-Neutral Drift Adjustment
### Risk-Free Rate with Risk-Neutral Drift Adjustment, up to 75% risk-free rate 
### Risk-Free Rate with Risk-Neutral Drift Adjustment, up to 5% risk-free rate
### Dividend Yield
### Volatility
### Years / Time to Expiry
### Time Steps
### Option Strike
### Underlying Price -->

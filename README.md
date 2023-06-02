# The Binomial Options Pricing Model, in Python

## Synopsis and Background

This is the CRR binomial pricing model for both American and European options; using Python. Written by Andy Yuan (me) in 2023 at Western University (UWO) with the mathematical support of professor Lars Stentoft. At the time I was in my third year of a 4-year bachelor's degree, majoring in accounting and applied statistics. This project was a testing point to apply my newfound Python and quantitative finance knowledge. 

### My Contact Information 
- [LinkedIn](https://www.linkedin.com/in/andytyuan/)
- University of Western Ontario Email: ayuan45@uwo.ca
- Personal Email: andy.yuan2tdsb@gmail.com

### A Visualization of the Binomial Model
![image](https://user-images.githubusercontent.com/125106540/233267193-514cf2d7-6b5e-4a42-80db-f4236f9cd045.png)

The option moves up or down and has the same choices for each node it reaches. The CRR model is recombinant on the underlying price. For example, one up and one down movement cancels each other out to reach the initial underlying price. 

## Guide to Use of Files

### Main File
The [Pricing & Greeks](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/blob/main/Pricing%20%26%20Greeks.py) that includes Greeks and Probabilities has a variety of functions. It calculates all the Greeks, some by using the tree and some by using finite differences (derivatives). Additionally, the probabilities of the individual nodes at payoff according to the binomial distribution is calculated. 

### Option Price Parameter Effect folder
The [option price effect](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/tree/main/Option%20Price%20Parameter%20Effect) folder examines the option price sensitivity to changes in those parameters. 

   The default parameters are:

   - Option Strike (K) = $100
   - Underlying Asset Price (S<sub>0</sub>) = $100
   - Implied Volatility (σ) = 20%
   - Time to Expiry (T) = 1 year
   - Risk-Free Rate (*r*) = 4%
   - Continuous Dividend Yield (δ) = 2%
   - Time Steps in the Tree (N) = 10 steps
    
   The default option prices are:
    
   - European put = $6.60708
   - European call = $8.548
   - American put = $6.90391
   - American call = $8.548

### Excel File of Sensitivity Data 
The data I pulled from the sensitivity analysis is within the [Excel File](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/blob/main/Excel%3B%20Options%20Price%20Sensitivity%20Analysis.xlsm). 
- Just to note, most of the parameter sensitivities do not have an imposed decimal limit on the ending option price, but the risk-free rate sensitivity analysis does. For the analysis without the risk-neutral adjustment: the European call has a 2 decimal place limit; the European put and American call/put have a 3 decimal place limit. For the file with the risk-neutral adjustment, there is a 5 decimal limit.

- The reason why the decimal place limits exist is because I modeled the prices up to 400% risk-free rate. The graph for that would be essentially useless however, so I only captured the relevant portion for this repository.

### Sharpe Ratio Calculator
This [calculator](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/blob/main/Sharpe%20Ratio%20Calculator%20.py) scrapes real world data from Yahoo! Finance and calculates a Sharpe ratio based on the binomial model pricing by measuring returns as the percentage difference between the binomial calculated price and the market price. It supports the effectiveness of the binomial model in the real world because there is no opportunity for profitable investment.

### Other Files\
Within the [Pricing Models Folder](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/tree/main/Pricing%20Models), there are three files:
- The European Options Only file runs through only the European method of valuing the option, only taking the discounted version of the payoffs
- The American Options Only file is similar to the European method of valuing the option, but takes into account the payoff at the specific time step. It chooses the maximum of the discounted payoffs and the payoff at exercise.
- The Adjusted Tree differentiates itself from the main file by changing how the up and down movements are calculated. In tandem, it also changes the respective probabilities of up and down movement.
  - Applicable to both models: 
    - ![image](https://user-images.githubusercontent.com/125106540/233430658-4c61a038-5070-4207-8524-3551584904d3.png)
    - ![image](https://user-images.githubusercontent.com/125106540/233430735-6041496d-8888-4d4a-9ee7-861b85a3e7c6.png)

  - Up, down, probability calculation without risk-neutral adjustment (CRR Model):
    - ![image](https://user-images.githubusercontent.com/125106540/233267484-b09b0d4c-226e-4590-a66e-a47cc289a29f.png)

  - Up, down, probability calculation with risk-neutral adjustment:
    - ![image](https://user-images.githubusercontent.com/125106540/233266813-042d0d08-f7ae-4954-b958-33b50e393b35.png)
      - Where ![image](https://user-images.githubusercontent.com/125106540/233266940-bdc620d6-afa3-4fb6-b057-9b9fd1d25da4.png)

Without the risk-neutral drift adjustment, the tree is recombinant on the underlying price. With the drift adjustment, the tree is recombinant on the risk-free rate instead. This prevents the drift from occurring, which will be illustrated in its specific graph.
> I referenced [this article](https://fbe.unimelb.edu.au/__data/assets/pdf_file/0010/2591884/170.pdf) for the calculations of up and down.

## Sensitivity Graphs
> Y-axis is the option price, X-axis is the parameter being changed

### Risk-Free Rate without Risk-Neutral Drift Adjustment:
![image](https://user-images.githubusercontent.com/125106540/234461153-17a1b9ba-4442-453c-89b8-7b31e4a3d671.png)

### Risk-Free Rate with Risk-Neutral Drift Adjustment:
![image](https://user-images.githubusercontent.com/125106540/231875608-c4b39b7b-c168-4538-9c80-59d77b51a6d4.png)

### Risk-Free Rate with Risk-Neutral Drift Adjustment, up to 75% risk-free rate:
![image](https://user-images.githubusercontent.com/125106540/233242638-5295569d-f0d6-4c65-85f7-0e833e1af761.png)

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

## Thoughts and Explanations on the Graphs

### Risk-Free Rate without Risk-Neutral Drift Adjustment
With the original CRR model, the up and down movements recombine on the original underlying price. This is what gives the model its binomial name. We see in the graph without the risk-neutral drift adjustment that the prices of the options begin to deviate from regular options theory. 

A basic financial concept is that a security or asset will always be worth more if you are given choice in what you can do with it. This is why options, which give the **option** to exercise at expiry, have a premium while forwards, which absolutely must be exercised at expiry, do not. For an option, the European style of exercise gives the holder only one exercise opportunity at the end of the contract. The American style of exercise gives the holder unlimited exercise opportunity up until the end of the contract. This choice allows for further profit if prices are favourable **now**, rather than waiting for an uncertain price in the future. 

In the graph, we see that as the risk-free rate increases past a large number, around 100% for the puts and around 120% for the calls, the prices of the European options begin to increase exponentially while the American options stagnate at their previous pace. This result is because of risk-neutral drift. In simpler terms, the risk-neutral drift arises from the probability of the up and down movements as the risk-free rate plays an integral role in determining the probabilities. Without going into specifics involving more difficult mathematical concepts and the underlying assumptions surrounding the black-scholes-merton and binomial models, I will say that the risk-neutral drift can be combatted by adding the presence of an adjustment in the form of ![image](https://user-images.githubusercontent.com/125106540/234463918-262a9a81-e988-4457-86ea-862969affd2c.png) with ![image](https://user-images.githubusercontent.com/125106540/233266940-bdc620d6-afa3-4fb6-b057-9b9fd1d25da4.png). This adjustment allows for the up and down movements to rely on both the strike and underlying price, which takes off some of the drift associated with the risk-free rate and only recombining on the underlying price.

> I found these slides from MIT to be helpful in explaining some of the concepts: https://math.mit.edu/~sheffield/600/Lecture36.pdf

### Risk-Free Rate with Risk-Neutral Drift Adjustment, up to 400% and up to 75%
With the adjustment, we see that the option prices move as we expect. The European and American prices at the very least follow each other, only differing by decimal places too small for python to bother with. You may notice it is strange that the puts are worth more than the calls at the very start of the graph, but this is present in the previous graph without the adjustment too. 

### Dividend Yield
I set a limit of 100% because a negative stock price would arise if more than 100% of the underlying were distributed as a dividend.

If the dividend yield of a stock increases, then investors expect the price of the stock to decease by the dividend amount. This is true in the case of a continuous dividend yield as pictured here or with discrete dividends. As such, this explains the movement of an increasing put option since the payoffs increase as the price of the underlying decreases. 

It is interesting to see that at around 90% dividend yield, the call prices begin to increase to just under $1 for the European call. Theoretically, the American option should follow, but at this time I genuinely do not know why the model behaves as such. It is fair to assume that a 90% dividend yield is virtually impossible, so for now it will be chalked up to a numerical error of a model that does not typically take extreme values.

### Volatility
Implied volatility is essentially the standard deviation of the option. As it increases, the option price should also increase because the range of possible exercises increases too. This is shown in the graph as the prices follow a parabolic curve as the implied volatility rises. 

At around 400%, notice that the prices begin to plateau, seemingly slowing down to a maximum. Initially, my professor and I thought it was a numerical issue that would be solved as the number of steps increased in the model. After increasing the steps from 10 to 50, I saw that the shape persisted. From further analysis, I can deduce that the option price cannot increase past the initial underlying's price. This conclusion comes as a surprise because the discounted cash flows from both sides of the tree should be enough to increase past the underlying's initial price as seen with the other parameters. An explanation on why this happens is pending further research, but I predict that it is because volatility effects the option up and down factor by an exponential amount both up and down, so the amount of movement is actually limited to the underlying price. Thus, the option price is limited to as equal or less than the initial underlying's price.

### Years / Time to Expiry
The graph of the option's price in reaction to the change of the time to expiry is similar to a natural logarithm's graph. From option theory, this movement is expected as a an option's price is essentially intrinsic value + time value. With more time to expiry, there is more of an opportunity for the option to profit as the range of possible underlying prices becomes larger with more time given. In this case, since the up movement of the option is slightly more probable, hanging around **P(u) = 0.5000000105409483** to **P(u) = 0.5001176546431096**, the call option ends up more expensive than the put option. 

This graph also shows that the time premium is not the biggest determinant of option price. Even when time to expiry approaches 5 years, the option price does not change drastically. As seen in the other graphs, the option price can reach magnitudes of over $1000 under the right conditions. 

### Time Steps
Perhaps the graph that gives the most satisfaction, it shows the convergence of the binomial model to the black-scholes-merton model. the price actually oscillates around the black-scholes-merton model.

This is the black-scholes-merton model:
![image](https://user-images.githubusercontent.com/125106540/233411762-38b60c24-abba-46f9-b1ca-6f215c4d0404.png)

The 'N' in the model is the cumulative distribution function of the normal distribution. There are a few limitations to the BSM model, namely the assumptions that the stock has no dividends and the option is European. The binomial model takes care of these restrictions.

### Option Strike
As the strike gets larger while the price remains the same, put and call options move opposite to each other. If the strike is below the underlying price, the call option's value is higher because of the intrinsic value of exercising at time 0. If the strike is above the underlying price, the put option's value is higher for the same reason. 

Both lines should intersect around when the strike reaches the underlying price. This concept is explained using the put-call symmetry, which will be discussed later. 

### Underlying Price
As the direct opposite of the option strike graph, the value of puts incease as the underlying price is below the option strike. Similarly, the value of calls increase as the underlying price is above the option strike. 

Again, the lines intersect around when the underlying price equals the strike.

## The put-call symmetry theory
Most academic options courses introduce put-call parity as one of the core concepts in options pricing. Since it is fairly intuitive and has a number of limitations, it is a good start for a student who wants to learn more about options. 

![image](https://user-images.githubusercontent.com/125106540/233417000-f25561e5-dd82-4774-822e-14845f83cec8.png)

The model is based off the continuous Black-Scholes-Merton model, and as such is restricted to European options only. Since the binomial model outlined above has application to both the American and European model, we want to use a rule applicable to both American and European options. Thankfully, the put-call symmetry theory exists as first pointed out by David Bates' ['The Skewness Premium: Option Pricing Under Asymmetric Processes'](https://www.biz.uiowa.edu/faculty/dbates/papers/skewprem.pdf).

The put-call symmetry theory states that a put option will be the same price as a call option if the (strike and underlying) and (risk-free rate and dividend yield) are switched. Since the theory works with American options and is also based off the Black-Scholes-Merton model, I would like to compare it with the results obtained from the binomial model. The relevant graphic to look at will be the [increasing time step graph](###-time-steps:).

![image](https://user-images.githubusercontent.com/125106540/235369801-c9d4f164-46de-4946-a7f7-e42eb788e3ee.png)

For a call with:
    - Strike: $90
    - Underlying Price: $100
    - Time Steps: 10
    - Implied Volatility: 20%
    - Time to Maturity: 1 year
    - Risk-free Rate: 4%
    - Dividend Yield: 2%

- European call option price is $ 14.534419943634203
- American call option price is $ 14.534419943634203

Then for a put with: 
    - Strike: $100
    - Underlying Price: $90
    - Time Steps: 10
    - Implied Volatility: 20%
    - Time to Maturity: 1 year
    - Risk-free Rate: 2%
    - Dividend Yield: 4%

- European put option price is $ 14.534419943634173
- American put option price is $ 14.534419943634173

So, we see here that the prices for both puts and calls are the same up until the 13th decimal place, where this decimal is likely too insignificant to affect the listed price. We can conclude with reasonable certainty that for a period of about 36 days, the prices for puts and calls using the put-call symmetry theory are in tune with the expected outcome. 

The complicated part of using the put-call symmetry theory is that it bases itself off the black-scholes-merton model, which is continuous. In contrast, the binomial model is discrete, with the accuracy of the model depending on the number of time steps. 

> Thank you to Louis Mao, a family friend, for pointing this connection out to me. His [LinkedIn](https://www.linkedin.com/in/louis-mao-4555b866/).

We have already established that the binomial model with enough steps will converge to the black-scholes-merton model. I believe evaluating the model with a low number of steps will be valuable to assess as the prices already oscillate even at a low number of time steps. 

The following graphs zoom into the time step graph to show the effect of a time step of up to about 30 days. It's obvious that the oscillation of the price begins to lose its height as more time steps are added. The trend line begins to pass through the graph closer to the upward oscillation, but eventually makes its way to the middle of both oscillations. We can ensure that the trendline is linear because the binomial alternates up and down AROUND the price shown in the black-scholes model. 

![image](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/assets/125106540/66edfb9b-4bd3-4365-b52d-157d78f32cf5)

![image](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/assets/125106540/c77b61b9-6ddf-4f95-b612-9862b2403c73)

![image](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/assets/125106540/881ff83a-5eb0-4675-8027-dc9444e9d81e)

For the call options, the expected value with a low number of time steps is the y-intercept: $9.2357. For the put options, the expected value with a low number of time steps is the y-intercept: $7.5089 for American puts and $7.2302 for European puts.

We then compare these values to when the number of time steps increases to when the oscillation's height is small. I pulled the values from time steps 250 to 299. 

![image](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/assets/125106540/eaf0fd08-8130-49f5-8dba-728f328e5db5)

![image](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/assets/125106540/a27a482b-1578-40e9-8d3e-b0ac6128f46d)

We see here that the slope of the respective trendlines is taken to the 4th significant figure, so we will take this as a 0 slope. Thus, the expected value of a call option is $8.7398 while the expected value of a put is $7.02 and $6.7989 for American and European puts, respectively. 

You may notice that the approximation of the binomial model with a low number of time steps is not a very accurate measure of an option's price. 

Differences: 
- Call Prices: 9.2357/8.7398 - 1 = **5.674%**
- Put Prices: 
    - American Put: 7.5089/7.02 - 1 = **6.964%**
    - European Put: 7.2302/6.7989 - 1 = **6.344%**

A difference of this magnitude would be detrimental to most traders' accounts, especially because of the markets' volatility. Let us also see the put-call symmetry at work with a low number of steps. We will have the dividend yield be 4% while the risk-free rate will be 2%. The strike and underlying are both 100, so there is no switching to do. As established before, the put-call symmetry should work. 

![image](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/assets/125106540/94de00a8-cb7b-4827-873e-784eb5c851da)

![image](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/assets/125106540/addc0da2-560c-41bf-abf9-391ac06ef7b1)

This is definitely encouraging, as the expected value of the calls is exactly the same as the puts on the other side of the put-call symmetry: $7.5089 for American exercise and $7.2302 for European exercise. For the puts, the difference between the expected value is -0.699% at $9.1711. This is a small difference that will likely not have a drastic effect on the overall theory. Something else that is encouraging is the behaviour of the option prices after applying put-call symmetry. Before, the call prices seemed to be almost the same while the put prices had a noticeable difference between put and call. Now with the symmetry applied, the behaviour is reversed so that the calls behave as the previous puts and the puts behave like the previous calls.

Now we evaluate the same for the actual expected value of the puts and calls and compare it to the low time step prices. Again, I pulled the values from time steps 250 to 299. 

![image](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/assets/125106540/f4a301ad-80a8-4f33-87de-f343e3db61ee)

![image](https://github.com/andytyuan2/Binomial-Options_Pricing-Andy-Y/assets/125106540/ae6a8d3f-aa38-48ab-9b4e-797774b41a87)

Now, the expected value of a call option is $7.0193 for American exercise and $6.798 for European Exercise. The expected value of a put option is $8.7389, which can be rounded to $8.739. Again, there is a discrepancy between the 'continuous' price vs the discrete price. We expect this difference to be the same as without PCS applied. 

Differences with PCS applied: 
- Call Prices: 
    - American Call: 7.5089/7.0193 = **6.9751%**
    - European Put: 7.2302/6.798 = **6.3578%**
- Put Prices: 9.1711/8.7389 = **4.9457%**

The main change in this is from the call price conversion to put price. The percentage change of the change in the discrete vs continuous price is 14.7259%, while the absolute change is 0.7283%. 

<!-- I anticipate that this change is the result of slight numerical differences in the tree. -->

This comparison seems to confirm that put-call symmetry works in the binomial model almost as well as its use in the continuous black-scholes model. Since the binomial model can evaluate each node instead of spitting out one value, the use for it is more well rounded, especially with the addition of the put-call symmetry.

## Sharpe Ratio Calculation to Support the Binomial Model's use in the Market

<!--I calculated a Sharpe ratio to validate the pricing model's use when compared to market prices. Typically a Sharpe ratio of under 1 is considered subpar and not worthy of investment. In the code, the user specifies the ticker symbol and a date of expiry for the option. The calculator will then run through data from Yahoo! Finance and come back with a Sharpe ratio. Through all of my tests, the Sharpe ratio is consistently under 1, typically around 0.5. This supports the use of the binomial model to price options. It is able to accurately calculate the option's price. -->

I calculated a Sharpe ratio to support the pricing model's use in markets. Of course, a market maker will not necessarily be using the binomial model, but it is useful to see the comparisons brought up by the calculation. The Sharpe ratio is a formula that measures an investment's performance while factoring in risk adjustments. The return of the investment is compared to the risk-free rate outlined by the 3-month treasury rate and an expected return is then calculated. 

![image](https://user-images.githubusercontent.com/125106540/236105083-51834092-7e25-4fd4-bf72-b0cad5bc6e6e.png)

The way that I calculated the Sharpe ratio for this options pricer is by first establishing that the return on the options would be from 'mispricings' that had positive returns. This meant that for an option, if the market price was less than the binomial calculated price, then the action taken would be to sell. Similarly, if the market option was more than the binomial calculated price, then the action to buy would be executed. This ensured that all the returns were positive and I was able to calculate a Sharpe ratio based on market mispricings rather than absolute returns. The concept behind the mispricing return was that the market would adjust to the calculated price. This approach considered price risk only as the correction is assumed to be instant. 

I calculated the expected value through the open interest totals. This was done through the Python packages yahoo_fin and yfinance. The calculation first specifies if the relevant option is a call or put, then evaluates the excessive return by scanning through the relevant bid and ask. It can be done for any stock in the yahoo_fin package, which directly scrapes from Yahoo! Finance website. From there, a standard deviation is calculated by sqrt(E(v^2) - E^2(v)). Again, the probabilities/weights of the purchase were directly related to the open interest totals. 

The Sharpe ratio evaluates performance by how large the result is. In most cases, a Sharpe ratio of 1 is fair, below 1 is poor, and above 1 is good. The greater the ratio, the greater is the risk-adjusted performance of the portfolio or asset of interest. There are some limitations to the metric, namely that the Sharpe ratio measures the standard deviation according to a normal distribution. As seen in many open interest numbers, the options market does not folow a normal distribution. I believe the way I handled the Sharpe ratio calculation stops the possibility of if the price can move up or down as my calculator only looks at an absolute positive return after mean reversion.

The bottom line of my building this calculator is that the returns from mean reversion of market options are too minuscule to have any meaningful impact on a portfolio. The sharpe ratio of all the possible options are consistently lower than 1 for all symbols and option types I tested. For example, on May 30, 2023 for the June 21, 2024 expiry, the MSFT put option Sharpe ratio was 0.5428074151836801, definitively under the benchmark ratio of 1. Similarly, the Sharpe ratio for AAPL with the same expiry and type was 0.667020814931802. As tests go further, which I implore you do with the provided code, the Sharpe ratio is consistently under 1. 

This supports the use of the binomial model in the options markets to price options, and may very well be a basic strategy of some options market makers. It does not suit a retail investor or even an institution because the risk from using the model would far outweigh the return. It is effective as a pricing strategy but not a source of alpha for most people. 

## Closing Thoughts

> coming soon

<!-- SOURCES

https://www.investopedia.com/terms/s/sharperatio.asp sharpe ratio




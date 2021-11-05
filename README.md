# Is dollar cost averaging or a monthly limit order better for total market Investing?  

[Dollar cost averaging](https://www.investopedia.com/terms/d/dollarcostaveraging.asp) is an investment strategy consisting of prorated, equal value investments made at a set frequency. This strategy aims to reduce the effects of market volatility and eliminates any attempts to time the market and emotion based investing.  

But what if you set a limit order for a dip in the market during the determined time period instead of dollar cost averging. If the limit order fires all is good and well, if it doesn't, simply purchase the asset at the end of the month anyway. Unfortunately, any growth in the market made during that month will be lost, but will there be enough successful limit orders to actually win out over plain DCA? Some quick python code can give us the answer. This code tests these two methods using monthly S&P 500 investments for different time periods.  

### Some Definitions  
Factor - the fractional value of the DCA purchase made on the 1st that the limit order will be set to for that month. This is the size of the dip we are hoping will occur that month.  
Shares Gained - how many more total shares the limit order method had over DCA.  
Order Success rate - the percentage of limit orders filled instead of just buying at end of month.  


### From 2009-11-11 to 2021-11-01
Factor | Shares Gained | Order Success Rate  
------------ | ------------- | ------------
0.99 | -0.079578 | 72.92 %
0.995 | 0.164123 | 90.97 %
0.998 | 0.12128 | 98.61 %
0.999 | 0.07568 | 100.0 %
0.9995 | 0.037821 | 100.0 %
0.9998 | 0.015124 | 100.0 %
0.9999 | 0.007561 | 100.0 %

### From 2005-11-11 to 2021-11-01
Factor | Shares Gained | Order Success Rate  
------------ | ------------- | ------------
0.99 | -0.059484 | 74.48 %
0.995 | 0.186808 | 91.67 %
0.998 | 0.201279 | 98.96 %
0.999 | 0.115639 | 100.0 %
0.9995 | 0.057791 | 100.0 %
0.9998 | 0.023109 | 100.0 %
0.9999 | 0.011554 | 100.0 %

### From 2000-11-11 to 2021-11-01
Factor | Shares Gained | Order Success Rate  
------------ | ------------- | ------------
0.99 | 0.262972 | 77.38 %
0.995 | 0.367058 | 92.46 %
0.998 | 0.31154 | 99.21 %
0.999 | 0.170714 | 100.0 %
0.9995 | 0.085315 | 100.0 %
0.9998 | 0.034116 | 100.0 %
0.9999 | 0.017056 | 100.0 %

### From 1995-11-11 to 2021-11-01  
Factor | Shares Gained | Order Success Rate  
------------ | ------------- | ------------
0.99 | 0.314627 | 78.21 %
0.995 | 0.518474 | 93.27 %
0.998 | 0.436753 | 99.36 %
0.999 | 0.233258 | 100.0 %
0.9995 | 0.116571 | 100.0 %
0.9998 | 0.046614 | 100.0 %
0.9999 | 0.023305 | 100.0 %


# Further Testing  
This was a quick and dirty proof of concept. More robust investigation would include shifting the purchase date for DCA and the time window for limit orders by several days and comparing those results against the results above which used the first of each month. Another variable that can be changed is the length of time the limit order is open. Reducing the time window for the limit order would minimize gains lost when the market never reaches the limit anyway, but this would also prevent some limit orders from succeeding.  

# Is it worth it?
Nope. Even if this method was robustly tested and determined to yield the 0.5 shares at best above DCA after 25 years it still wouldn't be worth the time of setting and checking limit orders every month. Also these limit orders would have to be rounded to the nearest cent which may reduce the advantage of this method.  
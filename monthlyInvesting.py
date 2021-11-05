#!/usr/bin/python
import yfinance as yf
import matplotlib.pyplot as plt
startdates = ['2009-11-11','2005-11-11', '2000-11-11', '1995-11-11'] 
enddate = '2021-11-01'
for startdate in startdates:

    df = yf.download('SPY', startdate, enddate) # S&P500 confirmed by graph
    df['Adj Close'].plot()
    #plt.show()
    print("From "+startdate + " to " + enddate)   
    factors = [0.99, 0.995, 0.998, 0.999, 0.9995, 0.9998, 0.9999]

    for factor in factors:
        DCA = 0
        prevMonth = 0
        order = 0
        orderBought = False
        orderLimit = 9999999
        ordersFilled = 0
        ordersOverriden = 0        
        for rowindex in range(df.shape[0]):
            row = df.iloc[rowindex]
            time = df.index[rowindex]
    
            if(time.month != prevMonth):
                DCA += (100 / row['Close']) # buy $100 worth of shares at close price
                prevMonth = time.month
        
                if (orderLimit != 9999999 and not orderBought): # order failed, buy previous close
                    order += ( 100 / df.iloc[rowindex - 1]['Close'])
                    ordersOverriden += 1                    
                
                orderBought = False # this is a new month, begin limit order
                orderLimit = row['Close'] * factor
                
            if (not orderBought and row['Low'] < orderLimit):
                order += (100 / orderLimit)
                orderBought = True
                ordersFilled += 1


        orderSuccessPercent = round(100* ordersFilled / (ordersFilled + ordersOverriden),2)
        print(str(factor)+ " | " + str(round(order-DCA,6))+" | " +str(orderSuccessPercent)+" %")
#        print(" factor: "+str(factor)+ " margin: " + str(round(order-DCA,6))+" with "+str(ordersFilled)+" limits hit")

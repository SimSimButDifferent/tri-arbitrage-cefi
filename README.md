# Triangular Arbitrage - Cefi - Poloniex

Following crypto wizards calculating triangular arbitrage course on udemy.

This bot currently running on poloniex

### Step 0 - Finding coins which can be traded
  1. Extract list of coins and prices from exchange
  2. Loop through each object and find tradable pairs
  3. Return list of tradable coins
  
 ### Step 1 - Structuring triangular pairs for calculation
  1. Structure the list of tradable triangular arbitrage pairs
  2. Save structured list to json file

### Step 2 - Calculate Surface Arbitrage opportunities
  1. Get structured pairs
  2. Get latest surface prices
  3. Loop through and structure price information
  
### Code executes (at current settings) every 20 seconds, looping through all the pairs on poloniex and returning any profitable arbitrage opportunities.
- Not recommended, with my testing so far i have not seen any that would give more then 0.01 percent profit (not including trading fees). This is purely to get the         code structure for this type of arbitrage, so that it can be applied to other things. Also this code will probably stop working from january 31st 2023, when the         legacy poloniex api is decomissioned.

import func_arbitrage
import json
#import time

# Set Variables
coin_price_url = "https://poloniex.com/public?command=returnTicker"

"""
    Step 0: Finding coins which can be traded
    Exchange: Poloniex
    https://docs.legacy.poloniex.com/#introduction
"""
def step_0():

    # Extract list of coins and prices from exchange
    coin_json = func_arbitrage.get_coin_tickers(coin_price_url)

    # Loop through each object and find tradable pairs
    coin_list = func_arbitrage.collect_tradables(coin_json)

    # Return list of tradable coins
    return coin_list


"""
    Step 1: Structuring triangular pairs
    Calculation only
"""
def step_1(coin_list):

    # Structure the list of tradable triangular arbitrage pairs
    structured_list = func_arbitrage.structure_triangular_pairs(coin_list)


    # Save structured list
    structured_list_json = json.dumps(structured_list)
    #print(structured_list_json)

    # Write list to .json file
    with open("structured_triangular_pairs.json", "w") as fp:
        fp.write(structured_list_json)

""" 
    Step 2: Calculate Surface Arbitrage opportunities
    Exchange: Poloniex
    https://docs.legacy.poloniex.com/#introduction
"""

def step_2():

    # Get structured pairs
    with open("structured_triangular_pairs.json") as json_file:
        structured_pairs = json.load(json_file)

    # Get latest surface prices
    prices_json = func_arbitrage.get_coin_tickers(coin_price_url)

    # Loop through and structure price information
    for t_pair in structured_pairs:
        prices_dict = func_arbitrage.get_price_for_t_pair(t_pair, prices_json)
        surface_arb = func_arbitrage.calc_triangular_arb_surface_rate(t_pair, prices_dict)
        if len(surface_arb) > 0:
            print(surface_arb["trade_description_3"])


""" MAIN """
if __name__ == "__main__":
    #coin_list = step_0()
    #structured_pairs = step_1(coin_list)
    step_2()

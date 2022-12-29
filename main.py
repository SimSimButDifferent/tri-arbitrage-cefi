import func_arbitrage
import json

"""
    Step 0: Finding coins which can be traded
    Exchange: Poloniex
    https://docs.legacy.poloniex.com/#introduction
"""
def step_0():

    # Extract list of coins and prices from exchange
    coin_json = func_arbitrage.get_coin_tickers("https://poloniex.com/public?command=returnTicker")

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
    print(structured_list_json)

    with open("structured_triangular_pairs.json", "w") as fp:
        fp.write(structured_list_json)

    #with open("structured_triangular_pairs.json", "w") as fp:
        #json.dump(structured_list, fp)

""" MAIN """
if __name__ == "__main__":
    coin_list = step_0()
    structured_pairs = step_1(coin_list)

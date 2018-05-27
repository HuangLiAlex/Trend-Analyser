from fraganalyser.generate_fragment_graph import generate_fragment_graph as gf
from fraganalyser.binance_historical_data import fetch_trading_data as fetch
from common import json_reader as reader
from common.plot import plot_candle


if __name__ == "__main__":
    
    """ [0] set defalt value """
    #json_file = "Binance_BTCUSDT_1d.json"
    effective_days = 3
    
    #symbol = "ZECBTC"
    #symbol = "NEOUSDT"
    symbol = "BTCUSDT"
    
    start_time = "01 Jan 2018"
    end_time = "10 May 2018"
    interval = "1d"
    
    """ [1] fetch historical data """
    json_file = fetch(symbol, start_time, end_time, interval)
    
    
    """ [2] get graph """
    graph = reader.Json_Reader.read(json_file)
    
    
    """ [3] generate fragment graph data """
    fragment_graph = gf(graph, effective_days)
    
    
    """ [4] generate graphs """
    graph_name = symbol + "_" + end_time.replace(" ", "_")
    frag_graph_name = symbol + "_frag_" + end_time.replace(" ", "_")
    
    plot_candle(graph, graph_name, online=False)
    plot_candle(fragment_graph, frag_graph_name, online=False)


    """ test print """
#    with open("graph.txt", 'w') as file:
#        for item in graph:
#            file.write("{}\n".format(item))
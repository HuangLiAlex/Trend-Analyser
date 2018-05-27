from fraganalyser.generate_fragment_graph import generate_fragment_graph as fg
from fraganalyser.tushare_historical_data import fetch_trading_data as fetch
from fraganalyser.generate_xxx_graph import generate_xxx_graph as xg
from common.json_reader import Json_Reader as r
import common.plot as p

if __name__ == "__main__":
    
    """ [0] define variable defalt  value """
    effective_days = 3
    effective_value = 50
    
    code = "000001"     # code for stock
    index = True        # if code is index
    start_time = "2018-03-04"   # YYYY-MM-DD
    end_time = "2018-03-20"
    ktype = "D"         # D, W, M, 5, 15, 30, 60
    autotype = "qfq"    # qfq, hfq, None
    
    """ [1] fetch historical data """
    out_dir = "data/"
    json_file = out_dir + "Stock_" + code + ".json"
    json_file = fetch(code)
    

    """ [2] get graph """
    graph = r.read_stock(json_file)
    
    
    """ [3] generate fragment graph data """
    fragment_graph = fg(graph, effective_days)
    
    #xxx_graph = xg(graph, effective_value)
    
    
    """ [4] generate graphs """
    graph_name = "上证指数_" + end_time
    #p.plot_candle(graph, graph_name, online=False)
    
    frag_graph_name = "上证指数新三段_X日期_" + end_time
    #p.plot_candle(fragment_graph, frag_graph_name, online=False)
    
    xxx_graph_name = "上证指数蟹行线_X日期_" + end_time
    p.plot_line(fragment_graph, xxx_graph_name, online=False)
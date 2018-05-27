import tushare as ts

def fetch_trading_data(code):
    klines = ts.get_k_data(code, index=True)
    
    with open("data/Stock_{}.json".format(code), 'w') as f:
            f.write(klines.to_json(orient='records', lines=True))
            
    return f.name

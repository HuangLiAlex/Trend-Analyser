from common import container as ct

def generate_xxx_graph(graph, effective_days):
    
    """ initialize variables """
    point_list = []
    barrier_stack = []
    
    fixed_value = 50
    fixed_rate = 5 / 100;
    
    trend_inverse = False

    
    
    """ initialize first line data """
    current_idx = 0
    macro_index = current_idx
    #start_time = graph[current_idx].get("Time")
    start_open = graph[current_idx].get("Open")
    start_close = graph[current_idx].get("Close")
    
    start_point = [current_idx, start_open]
    point_list.append(start_point)
    
    next_point = [current_idx, start_close]
    point_list.append(next_point)
    
    if (start_close > start_open):
        micro_trend = 'up'
        macro_trend = 'up'
    else:
        micro_trend = 'down'
        macro_trend = 'down'
        
    last_micro_trend = micro_trend
    
    """ loop next coor data """
    current_idx += 1
    
    next_close = graph[current_idx].get("Close")
    
    ''' compare with micro '''
    if (next_close > start_close):
        micro_trend = 'up'
        diff = next_close - start_close
    else:
        micro_trend = 'down'
        diff = start_close - next_close
    
    if (micro_trend == last_micro_trend):
        trend_inverse = False
    else:
        trend_inverse = True
        
    if(trend_inverse):
        if (diff > accumulated):
            accumulated = diff - accumulated
            
        else
            
    
    
    
    
    
    
    
    return point_list

""" check barrier """
def get_barrier(barrier_stack, effective_days):
    accumulated_days = len(barrier_stack)
    if (accumulated_days <= effective_days):
        return barrier_stack[0]
    else:
        return barrier_stack[accumulated_days-effective_days]
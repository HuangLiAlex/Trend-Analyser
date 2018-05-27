from common import container as ct

def generate_fragment_graph(graph, effective_days):
    
    """ initialize variables """
    fragment_graph = []
    barrier_stack = []
    
    trend_inverse = False
    last_trend = None
    new_trend = None
    barrier = None
    
    
    """ 
    start_time = "22 Aug, 2017"
    
    for stick in graph:
        if (stick.get("Time") == dm(start_time)):
            start_index = graph.index(stick)
            break
    """
    
    """ get first candle data """
    start_index = 0
    start_time = graph[start_index].get("Time")
    start_open = graph[start_index].get("Open")
    start_close = graph[start_index].get("Close")
    new_stick = ct.Stick.fromFragment(start_time, start_open, start_close)
    fragment_graph.append(new_stick)
    barrier_stack = [start_open]   # to specify initial barrier
    
    """ get next """
    total_days = len(graph) - start_index -1
    for index in range(total_days):
        next_index = start_index + 1
        start_open = graph[start_index].get("Open")
        start_close = graph[start_index].get("Close")
        start_index = next_index
        next_close = graph[next_index].get("Close")
        next_trend = graph[next_index].get("Trend")
        
        """ verify valid trend and figure """
        if(float(next_close) > float(start_close)):
            new_trend = 'up'
        else:
            new_trend = 'down'
        
        if new_trend != next_trend:
            continue
        
        if(last_trend is None):
            last_trend = fragment_graph[-1].get("Trend")
        
        if(new_trend != last_trend):
            trend_inverse = True
        else:
            trend_inverse = False
        
        if not trend_inverse:
            if((next_trend == 'up' and float(next_close) > float(barrier_stack[-1])) or 
               (next_trend == 'down' and float(next_close) < float(barrier_stack[-1]))):
                
                next_open = fragment_graph[-1].get("Close")
                next_time = graph[next_index].get("Time")
                new_stick = ct.Stick.fromFragment(next_time, next_open, next_close)
                fragment_graph.append(new_stick)
                barrier_stack.append(next_close)
            else:
                continue
            
        else:
            barrier = get_barrier(barrier_stack, effective_days + 1)
            
            if(next_trend == 'up' and float(next_close) > float(barrier)):
                last_trend = new_trend
                new_trend = 'down'
                new_open = fragment_graph[-1].get("Open")
                next_time = graph[next_index].get("Time")
                new_close = next_close
                new_stick = ct.Stick.fromFragment(next_time, new_open, new_close)
                fragment_graph.append(new_stick)
                barrier_stack.clear()
                barrier_stack.append(new_open)
                barrier_stack.append(next_close)
                
            elif(next_trend == 'down' and float(next_close) < float(barrier)):
                last_trend = new_trend
                new_trend = 'up'
                new_open = fragment_graph[-1].get("Open")
                next_time = graph[next_index].get("Time")
                new_close = next_close
                new_stick = ct.Stick.fromFragment(next_time, new_open, new_close)
                fragment_graph.append(new_stick)
                barrier_stack.clear()
                barrier_stack.append(new_open)
                barrier_stack.append(next_close)
            else:
                continue
            
    return fragment_graph


""" check barrier """
def get_barrier(barrier_stack, effective_days):
    accumulated_days = len(barrier_stack)
    if (accumulated_days <= effective_days):
        return barrier_stack[0]
    else:
        return barrier_stack[accumulated_days-effective_days]
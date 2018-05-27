import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

def plot_candle(graph, name, online=False):

    df = pd.DataFrame(graph)

    trace = go.Candlestick(
                x = df.index,
                open = df.Open,
                close = df.Close,
                high = df.High,
                low = df.Low,
                text = df.Time
            )
    
    layout = go.Layout(
                title = name
            )
    
    data = [trace]
    
    fig = go.Figure(data=data, layout=layout)
    
    name = "data/" + name
    if online:
        py.iplot(fig, filename=name, auto_open=True)
    else:
        plotly.offline.plot(fig, filename=name, validate=False)


def plot_line(name, online=False):

    #df = pd.DataFrame(graph)

    trace1 = go.Scatter(
        x = df.index,
        close = df.Close,
        mode='lines+markers',
        name="'linear'",
        hoverinfo='name',
        line=dict(
            shape='linear'
        )
    )

    trace2 = go.Scatter(
        x = df.index,
        close = df.Close,
        mode='lines+markers',
        name="'vh'",
        hoverinfo='name',
        line=dict(
            shape='vh'
        )
    )
    data = [trace1]
    
    fig = dict(data = data)
    
    name = "data/" + name
    if online:
        py.iplot(fig, filename=name, auto_open=True)
    else:
        plotly.offline.plot(fig, filename=name, validate=False)

    return data

if __name__ == "__main__":
    data = plot_line("line-plot", online=False)
    data.help('attribute')
    
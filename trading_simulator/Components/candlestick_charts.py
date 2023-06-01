import plotly.graph_objects as go
import pandas as pd
import time

PLOTLY_CONFIG = {
    'displaylogo': False,
    'modeBarButtonsToRemove': ['toImage', 'select','lasso2d']
}

def create_graph(dataframe, timestamp='', next_graph=True, range=10):
    """
    Create a candlestick chart for the selected stock or update an existing one

    Parameters
    ----------
    dataframe : str
        dataframe containing the market data

    timestamp : str
        timestamp of the initial market data to display (optional)
        if not specified, the oldest market data will be displayed

    range : int
        number of data points to display (default: 10)

    Returns
    -------
    plotly.graph_objects.Figure
        Candlestick chart to display

    datetime.datetime
        Last timestamp of the default market data used to create the chart
    """

    # if this is the first time the graph is being created
    if (timestamp == ''):
        if range == 0:
            dftmp = dataframe[:1]
        else:
            dftmp = dataframe[:range]
    else: # if the graph is being updated
        idx = dataframe.index.get_loc(timestamp)
        if next_graph: # You want to see the graph with new data
            if range == 0:
                dftmp = dataframe.iloc[:idx + 1]
            else:
                dftmp = dataframe.iloc[idx - (range - 2) : idx + 2]
        else: # You want to see the graph of another company
              # And so with the same timestamp as the previous graph
            if range == 0:
                dftmp = dataframe.iloc[idx - 1 : idx]
            else:
                dftmp = dataframe.iloc[idx - (range - 1) : idx + 1]

     # Create candlestick chart for the selected stock
    figure = go.Figure(
        data = [go.Candlestick(
            x = dftmp.index,
            open  = dftmp['Open'],
            high  = dftmp['High'],
            low   = dftmp['Low'],
            close = dftmp['Close']
        )]
    )

    # Define chart layout
    figure.update_layout(
        #title = company_id + ' stock price',
        xaxis_title = 'Date',
        yaxis_title = 'Prix',
        yaxis_tickprefix = '€',
        showlegend=False
    )

    return figure, dftmp.index[-1]

if __name__ == '__main__':
    import os

    name = 'TSLA'

    file_path = os.path.join('market_data' , name + '.csv')
    df = pd.read_csv(file_path, index_col=0)

    fig,endtime = create_graph(df)
    fig.show()

    testtime = 3
    while testtime > 0:
        time.sleep(5)

        fig,endtime = create_graph(df, endtime)
        print(endtime)

        fig.show()
        testtime -= 1
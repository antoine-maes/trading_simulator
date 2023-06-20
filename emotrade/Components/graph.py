import os
import pandas as pd
from dash import Output, Input, State, ctx, no_update, page_registry as dash_registry
import dash
import plotly.graph_objects as go

import emotrade as etd
from emotrade.Components.candlestick_charts import create_graph
from emotrade.Locales import translations as tls


@dash.callback(
	Output('company-graph', 'figure'),          # new graph
	Output('market-timestamp-value', 'data'),   # new timestamp
	Input('periodic-updater', 'n_intervals'), 	# periodicly updated
	Input('market-dataframe', 'data'),          # new company is selected
	State('market-timestamp-value', 'data') 	# Last timestamp
)
def update_graph(n, df, timestamp, range=100):
	""" Update the graph with the latest market data
		Periodicly updated or when the user selects a new company
	"""
	# Determining which callback input changed
	if ctx.triggered_id == 'periodic-updater':
		next_graph = True
	else:
		# If the user selected a new company
		# Don’t change the timestamp.
		next_graph = False

	dftmp = pd.DataFrame.from_dict(df)
	fig, timestamp = create_graph(
		dftmp,
        timestamp,
		next_graph,
        range
    )
	# Define chart layout
	fig.update_layout(
		# xaxis_title = tls[dash_registry['lang']]["market-graph"]['x'],
        # yaxis_title = tls[dash_registry['lang']]["market-graph"]['y'],
        yaxis_tickprefix = '€',
        margin = dict(l=0, r=0, t=0, b=0),
        height = 300,
		legend = dict(x=0, y=1.0)
    )
	# Change language on the legend
	fig.for_each_trace(lambda t:
		t.update(name = tls[dash_registry['lang']]["market-graph"]['legend'][t.name])
	)

	return fig, timestamp


@dash.callback(
	Output('revenue-graph', 'figure'),
	Output('graph-tabs', 'value'),
	Output('tab-revenue', 'style'),
	Input('company-selector', 'value')
)
def update_revenue( company):
	""" Display the revenue graph
	"""
	# If the user select an index, force the tab to be the market graph
	if company in etd.INDEX.keys():
		return no_update, 'tab-market', {'display': 'none'}

	# Import income data of the selected company
	file_path = os.path.join('Data', 'revenue.csv')
	df = pd.read_csv(file_path, index_col=0, header=[0,1])

	# Format these data to be easily used
	df = df[company].T.reset_index()
	df['NetIncome'] = pd.to_numeric(df['NetIncome'], errors='coerce')
	df['TotalRevenue'] = pd.to_numeric(df['TotalRevenue'], errors='coerce')

	# Create the graph
	fig = go.Figure(data=[
		go.Bar(
			name = tls[dash_registry['lang']]["revenue-graph"]['totalRevenue'],
			x = df['asOfDate'], y = df['TotalRevenue']
		),
		go.Bar(
			name = tls[dash_registry['lang']]["revenue-graph"]['netIncome'],
			x = df['asOfDate'], y = df['NetIncome']
		)
	])
	fig.update_layout(
		yaxis_tickprefix = '€',
        margin = dict(l=0, r=0, t=0, b=0),
        height = 300,
		legend=dict(x=0, y=1.0)
	)

	# Go back to the market graph when the user selects a new company
	return fig, 'tab-market', {'display': 'block'}
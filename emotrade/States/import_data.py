import os
import pandas as pd
from dash import Output, Input, State
import dash

from emotrade.defaults import defaults as dlt

# Callbacks
@dash.callback(
    Output("market-dataframe", "data"),
	Output("price-dataframe", "data"),
    Input('company-selector', 'value'),
	State("price-dataframe", "data"),
)
def import_market_data(company_id, price_list):
	""" Import market data from CSV file
	"""
	# Import market data
	file_path = os.path.join(dlt.data_path, 'market_data.csv')
	df = pd.read_csv(file_path, index_col=0, header=[0,1])

	# Extract price list from market data
	if not price_list: # if the dataframe has not been loaded yet
		price_list = df.xs('Close', axis=1, level=1)
		price_list = price_list.to_dict()

	return df[company_id].to_dict(), price_list

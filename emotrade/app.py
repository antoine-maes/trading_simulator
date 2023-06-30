from dash import Dash, html, dcc
import dash

from emotrade.Layouts import dashboard

# Initialize Dash app
app = Dash(__name__,
    use_pages=True, # use_pages is used for multi-language support
    suppress_callback_exceptions=True, # Disable ids check because we use dynamic layout
)

# Set app layout
# This will be replaced by the page content (layout with the selected language)
app.layout = html.Div([
    *dashboard.global_variables,
    dash.page_container
])

# Variables used to disable the start button on the home page
app.home_start_button_disabled = False


if __name__ == '__main__':
	# Run app
    app.run_server(debug=True) #TODO: change to False when deploying
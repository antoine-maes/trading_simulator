import dash

from emotrade.Layouts import dashboard
from emotrade.Locales import translations as tls


dash.register_page(
    __name__,
    path='/dashboard',
    path_template="/<lang>/dashboard",
)


def layout(lang="fr"):
    from emotrade.app import app # Import here to avoid circular import
    app.dashboardIsRunning = True # Set the dashboard as running

    if lang not in tls.keys(): lang = "fr" # Handle invalid language
    dash.page_registry['lang'] = lang      # Provide the language to the callbacks

    return dashboard.main_layout(lang) # Import the layout with the selected language


# Import callbacks
from emotrade.States import import_data, save_state
from emotrade.Components import graph, portfolio, requests, news


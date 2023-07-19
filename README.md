<!-- References -->
[repo-url]: https://github.com/kelhad00/trading_simulator/
[library-exemple-url]: https://raw.githubusercontent.com/kelhad00/trading_simulator/main/main.py
[requirements-url]: https://raw.githubusercontent.com/kelhad00/trading_simulator/main/requirements.txt
<!-- [discussion-url]: https://github.com/kelhad00/trading_simulator/discussions -->
[wiki-url]: https://github.com/kelhad00/trading_simulator/wiki
<!-- [license-url]: https://raw.githubusercontent.com/kelhad00/trading_simulator/main/LICENSE -->


# emotrade

A stock market site simulator for collecting data on stocks carried out by the trader.

![emotrade interface home page](https://raw.githubusercontent.com/kelhad00/trading_simulator/main/.github/images/homepage.png)

![emotrade interface dashboard](https://raw.githubusercontent.com/kelhad00/trading_simulator/main/.github/images/dashboard.png)


## Table of contents

- [Requirements](#requirements)
- [Installing](#installing)
- [Usage](#usage)
    - [Using the command line tool](#using-the-command-line)
    - [Using it as a library](#integrating-it-into-your-program)
- [Handling the application](#handling-the-application)
    - [Modify default configuration](#default-configuration)
    - [Modify running application](#modify-application-status-during-operation)
- [The Setup toolbox](#the-setup-toolbox)
- [Why was this project created?](#why-was-this-project-created)
- [Contributing](#contributing)


## Requirements

- [Python](https://www.python.org/) == 3.10 (Has not been tested for more recent versions)
- [dash](https://github.com/plotly/dash) >= 2.10.2 : Low-code framework for rapidly building data apps in Python.
- [Pandas](https://pandas.pydata.org/) >= 2.0.2 : Fast, powerful, flexible and easy to use open source data analysis and manipulation tool

### Optional (if you want to use `emotrade.setup` tools)
- [yahooquery](https://yahooquery.dpguthrie.com/) >= 2.3.1 : Python wrapper for an unofficial Yahoo Finance API

The complete list is in [requirements.txt](requirements-url)


## Installing

<!-- Install and update using pip:
```bash
pip install -U emotrade
``` -->

Download the latest version of the repository and install the package locally with pip:
```bash
# Clone the repository or download the latest version on the corresponding page
cd trading_simulator # Move to project root
pip install setuptools . # Don't forget the dot at the end to install emotrade from local files
```


## Usage
### Using the command line

Simply use the command line tool.
```bash
emotrade <data_directory>
```

For more information on the command line :
```bash
emotrade -h
```


### Integrating it into your program

If you want to integrate it into your program, here's a simple example:
```python
# main.py
from emotrade import app
from emotrade.Setup import download_market_data

download_market_data() # Prepare the minimum necessary for interface operation

# [Your program...]

app.set_layout() # Import the layout before starting the server
app.run_server() # Server startup blocks the next instruction until the user presses ctrl-c in the terminal.
```

For a more realistic example, have a look at the [`main.py`](library-exemple-url) file in this repository.

For more complex use, with other instructions during server operation, it's best to put your program in a different thread. Like this:
```python
# main.py
from threading import Thread
from emotrade import app

download_market_data() # Prepare the minimum necessary for interface operation

# [A few instructions before getting started...]

th = Thread(target=your_program)
th.start()

app.set_layout() # Import the layout
app.run_server() # Starts the server and blocks the following instructions.
```

## Handling the application

The application can be fully manipulated using the `app` object available from `emotrade`.

### Default configuration

The default values are available from `app.defaults` or its abbreviated version `app.d`. It is strongly recommended not to modify them after calling `app.set_layout()` and/or `app.run_server()`.

Here is a description of the default values used:
```python
# Period of time used to update data on the dashboard
app.d.update_time = 60*1000 # in milliseconds

# Maximum number of requests the user can make on the dashboard
app.d.max_requests = 10

# Initial money the user has
app.d.initial_money = 100000

# Path to the data folder
app.d.data_path = "Data"

# Stocks used in the interface
# They are also used to download data with the download_market_data setup tool
# The key is the ticker and the value is the name of the company
# So the data provided in the Data folder must have the same name as the symbol
app.d.companies = {
    "MC.PA" : "LVMH MOËT HENNESSY LOUIS VUITTON SE (MC)",
    "OR.PA" : "L'ORÉAL (OR)",
    "RMS.PA" : "HERMÈS INTERNATIONAL (RMS)",
    "TTE.PA" : "TOTALENERGIES SE (TTE)",
    "SAN.PA" : "SANOFI (SAN)",
    "AIR.PA" : "AIRBUS SE (AIR)",
    "SU.PA" : "SCHNEIDER ELECTRIC SE (SU)",
    "AI.PA" : "AIR LIQUIDE (AI)",
    "EL.PA" : "ESSILORLUXOTTICA (EL)",
    "BNP.PA" : "BNP PARIBAS (BNP)",
    "KER.PA" : "KERING (KER)",
    "DG.PA" : "VINCI (DG)",
    "CS.PA" : "AXA (CS)",
    "SAF.PA" : "SAFRAN (SAF)",
    "RI.PA" : "PERNOD RICARD (RI)",
    "DSY.PA" : "DASSAULT SYSTÈMES SE (DSY)",
    "STLAM.MI" : "STELLANTIS N.V. (STLAM)",
    "BN.PA" : "DANONE (BN)",
    "STMPA.PA" : "STMICROELECTRONICS N.V. (STMPA)",
    "ACA.PA": "CRÉDIT AGRICOLE S.A. (ACA)"
}

# Indexes used in the interface
# Same use as the companies variable
app.d.indexes = {
    "^GSPC" : "S&P 500",
    "^DJI" : "Dow Jones Industrial Average",
    "^FCHI" : "CAC 40",
    "^SPGSGC" : "S&P GSCI Gold Index",
}
```

### Modify application status during operation

The `app` object also provides variables for manipulating the interface and/or finding out the state of an element while the interface is running.

These variables and their default values are described below:
```python
# Enables or disables the start button on the home page.
# Takes a Boolean as input
app.home_start_button_disabled = false

# Describe the state of the application,
# i.e. whether the dashboard is displayed or not.
# This variable is set when the user arrives on a page.
# It is therefore undefined until this happens.
app.dashboardIsRunning
```

## The `Setup` toolbox

The `emotrade.Setup` toolbox provides additional functions for creating an interface environment.
Here's a list:

```python
def download_market_data():
    """ Download daily stock market data for companies and indexes
        defined respectively by `app.d.companies` and `app.d.indexes`
        over the last two years, then save them in the folder defined
        by `app.d.data_path`.
    """
    pass

def analyse_news_data(data_path='Data'):
    """ Opens a jupyter notebook at the location
        defined by the data_path argument
        to analyze the data it contains in the form of graphs.
    """
    pass

```

For legal reasons, we do not provide a way to generate the news.csv file. It is up to you to obtain this file and place it in the folder defined by `app.d.data_path`. It must contain the columns `title;content;ticker;date` with the separator ";".

## Why was this project created?

<!-- Add explanations here -->
...


<!-- ## Wiki

Check out the [wiki](wiki-url) for more info. -->


## Contributing

Feel free to create an issue/PR if you want to see anything else implemented.
<!-- If you have some question or need help with configuration, start a [discussion](discussion-url). -->

<!-- Please read [CONTRIBUTING.md](./CONTRIBUTING.md) before opening a PR. -->
You can also help with documentation in the [wiki](wiki-url).


<!-- ## Legal Stuff

**emotrade** is distributed under the <Add license here> license. See the [LICENSE](license-url) file in the release for details. -->
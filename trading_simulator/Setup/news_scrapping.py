from stocknews import StockNews
import pandas as pd
import numpy as np
import datetime

# GET THE DATA
COMP = [ # List of stocks to download
    "MC.PA",  "TTE.PA", "SAN.PA", "OR.PA",  "SU.PA", \
    "AI.PA",  "AIR.PA", "BNP.PA", "DG.PA",  "CS.PA", \
    "RMS.PA", "EL.PA",  "SAF.PA", "KER.PA", "RI.PA", \
    "STLAM.MI",  "BN.PA",  "STMPA.PA",  "CAP.PA", "SGO.PA"
]
# sn = StockNews(COMP, wt_key='MY_WORLD_TRADING_DATA_KEY') 
# df = sn.summarize()

# READ THE DATA
dff = pd.read_csv('data/news.csv',sep=';',usecols=['stock','title','p_date']) # 'sentiment_title'


# get current date
current_date = datetime.date.today()
date = datetime.date(2023, 5, 19)
# print(date)


def date_wanted():
    liste_date = list(dff['p_date'])
    wanted_dates_ind = []
    wanted_dates=[]
    # print(liste_date)
    for d in liste_date:
        if str(date) in d: 
            print(d)
            wanted_dates_ind.append(liste_date.index(d))
            # wanted_dates.append(dff[dff['p_date']==d])
            # print(dff[dff['p_date']==d])
    print(wanted_dates_ind)
    return wanted_dates

date_wanted()

# my_df = dff[dff['p_date']=='CAP.PA_2023-05-02']
# required_df =df.loc[df['hits']>20]
# print(my_df)
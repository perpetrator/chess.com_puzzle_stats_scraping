#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from datetime import datetime


# In[50]:


def parseDate(date):
    return datetime.strptime(date, "%b %d, %Y")


# In[57]:


try:
    config = json.load(open('config.json'))
    print('Config successfully loaded!')
except:
    print('There is a problem with the config file!')


# In[52]:


res = requests.get("https://www.chess.com/stats/puzzles/"+config['chess_com_user'])
soup = BeautifulSoup(res.content,'lxml')
table = tab = soup.find("table",{"class":"table progress-table problems-table with-row-highlight"})
df = pd.read_html(str(table))[0]
df['Date'] = df['Date'].apply(parseDate)


# In[53]:


try:
    engine = create_engine('mysql+pymysql://'+config['user']+':'+config['password']+'@'+config['server']+'/'+config['db'])
except:
    print("There is a problem with DB connection")


# In[54]:


try:
    existing = pd.read_sql(config['sql1'], engine, parse_dates = True)
    existing = existing.drop(columns=['Number'])
except:
    existing = pd.DataFrame()


# In[55]:


if(not existing.empty):
    df = df.merge(existing, on=['Date','Rating', 'Moves', 'Target Time', 'My Time', 'Outcome','Avg Time','My Rating', 'ID'], 
                   how='left', indicator=True).loc[lambda x : x['_merge']=='left_only']
    df = df.drop(columns=['_merge'])
else:
    Print('First import!')


# In[56]:


if(not df.empty):
    df = df.iloc[::-1]
    df.to_sql(config['table_name'], con=engine, if_exists='append',index = False)
    print('New solved puzzles:')
    print(df)
else:
    print("Nihil novi")


# In[ ]:





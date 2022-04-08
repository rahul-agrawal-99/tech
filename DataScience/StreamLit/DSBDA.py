# import numpy as np
import streamlit as st
# import re
# import requests
# import base64
# from bs4 import BeautifulSoup
import datetime

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import date

st.title("- Crypto Trend Analysis - ")

# avilable crypto  shib , btc ,doge , trx , usdt  , wazirx , bnb ,  etherum , litecoin , ripple , neo , eos , zil , ftm , ctsi ,matic , iotx , oneinch

crypto = ['SHIB-USD', 'BTC-USD', 'DOGE-USD', 'TRX-USD', 'USDT-USD', 'WRX-USD', 'BNB-USD', 'ETH-USD', 'LTC-BTC', 'XRP-USD', 'NEO-USD', 'EOS-USD', 'ZIL-INR', 'FTM-USD', 'CTSI-USD', 'MATIC-USD', 'IOTX-INR']
# crypto_list = ["shib","btc","doge","tron","usdt","wazirx","bianance coin","etherum","litecoin","ripple","neo","eos","zil","ftm","ctsi","matic","iotx"]



def fetch_data (start_date , end_date, tickers): 
    data = yf.download(tickers=tickers, start= start_date , end=end_date , interval = '1d')   
    return data

def get_pch(df):
    mean = df[op].mean()
    base_price = df.iloc[0][0]
    pch_list = []
    # pch_list.append(0)
    print("mean is " , mean)
    for i in range(len(df)):
        a= (df.iloc[i][0] - base_price)  / mean
        
        pch_list.append(a*100)
    # for i in range(1,len(df)):
    #     a= df.iloc[i][0]  / base_price
    #     if a > 1 :
    #         a= a -1 
    #     else:
    #         a = -(1 - a)
    #     pch_list.append(a*100)
    
    df = pd.DataFrame(pch_list)
    
    return df




col1, col2  = st.sidebar.columns((1,1 )) 

cry1 = col1.selectbox("Select Crypto 1 " , tuple(crypto) )
cry2 = col2.selectbox("Select Crypto 2" , tuple(crypto) )
op = st.sidebar.selectbox("Select the Col for graph", ("Close", "Open", "High", "Low"))


start_date = col1.date_input("From" , datetime.date(2021,1,1))
end_date  = col2.date_input("Upto", datetime.date(2022,1,21))   # Y - M -D

from datetime import datetime
diff = end_date - start_date
diff_today =  datetime.today().date() - end_date

days = st.sidebar.slider("Rolling mean Window in days",1,10,5)

mybtn = st.sidebar.button("Show Data")

expander = st.sidebar.expander("About Project ")

expander.markdown(f""" 
                    Credits: \n
                   ## @rahul_agrawal
                   ## @shreyas_arali
                   ## @prathamesh_chatala
                  """)


col1, col2 = st.columns((1,1 )) 


if mybtn and diff.days >0 and diff_today.days <= days:
    # -------------------------   col1  for crypto 1------------------------------------------------------------
    col1.write(f"### Showing data for ")
    col1.write(f"# {cry1}")
    df1 = fetch_data(start_date,end_date,tickers=cry1)
    
    expander_bar1 = col1.expander(f"Show Data for {cry1}")
    expander_bar1.markdown(df1)
    
    
    #    line chart
    col1.subheader("Line_chart")
    col1.line_chart(df1[op])
    
    col1.write("***")
    
    #  volume traded
    col1.subheader("Volume traded")
    col1.line_chart(df1['Volume'])
    
    col1.write("***")
    
    #  current status 
    col1.subheader("Current change in price based on start date")
    col1.metric(f"{cry1}", f"{df1[op].iloc[len(df1)-1]}", f"{round(((df1[op].iloc[len(df1)-1] - df1[op].iloc[1])/ df1[op].iloc[1])*100 , 2)}%") 
    col1.caption(f"returns in {len(df1)} days")
    
    col1.write("***")
    #  rolling mean
    
    col1.subheader("Line_chart based on Rolling mean")
    df1[f'{op}-{days}d-rolling'] = df1[op].rolling(window=days).mean()
    col1.line_chart(df1.loc[: ,[op, f'{op}-{days}d-rolling']])
    col1.write("***")
    
    #  corr matrix 
    col1.subheader(f"Corr betn {op} and Volume")
    fig, ax = plt.subplots()
    corr = df1[[op,"Volume"]].corr()
    sns.heatmap(corr , annot=True)
    col1.pyplot(fig)
    col1.write("***")
    
    #  bar plot
    
    col1.subheader(f"Bar-Plot For {op} and Volume")  
                    # a greater fluctuation in the stock price may be a reason behind more transactions of stocks that day
    fig, ax = plt.subplots()
    sns.barplot(data=df1, x = op, y="Volume")
    col1.pyplot(fig)
    col1.write("***")
    
    
    
    df11 = get_pch(pd.DataFrame(df1[op]) )
   
    # -------------------------   col2  for crypto 2------------------------------------------------------------
    
    col2.write(f"### Showing data for ")
    col2.write(f"#  {cry2}")
    df2 = fetch_data(start_date,end_date,tickers=cry2)
    
    expander_bar2 = col2.expander(f"Show Data for {cry2}")
    expander_bar2.markdown(df2)
    
    col2.subheader("Line_chart")
    col2.line_chart(df2[op])
    col2.write("***")
    
    #  volume traded
    col2.subheader("Volume traded")
    col2.line_chart(df2['Volume'])
    col2.write("***")
    
    #  current status 
    col2.subheader("Current change in price based on start date")
    col2.metric(f"{cry2}", f"{df2[op].iloc[len(df2)-1]}", f"{round(((df2[op].iloc[len(df2)-1] - df2[op].iloc[1])/ df2[op].iloc[1])*100 , 2) } %")
    col2.caption(f"returns in {len(df2)} days") 
    col2.write("***")
    
    #  rolling mean
    
    col2.subheader("Line_chart based on Rolling mean")
    df2[f'{op}-{days}d-rolling'] = df2[op].rolling(window=days).mean()
    col2.line_chart(df2.loc[: ,[op, f'{op}-{days}d-rolling']])
    col2.write("***")
    
    #  corr matrix 
    col2.subheader(f"Corr betn {op} and Volume")
    fig, ax = plt.subplots()
    corr = df2[[op,"Volume"]].corr()
    sns.heatmap(corr , annot=True)
    col2.pyplot(fig)
    col2.write("***")
    
        #  bar plot
    
    col2.subheader(f"Bar-Plot For {op} and Volume")  
                    # a greater fluctuation in the stock price may be a reason behind more transactions of stocks that day
    fig, ax = plt.subplots()
    sns.barplot(data=df2, x = op, y="Volume")
    col2.pyplot(fig)
    col2.write("***")
    
    
    
    df21 = get_pch(pd.DataFrame(df2[op]) )
    
    
    # ------------------------------mergerd output --------------------------------------------
    
    st.write("***")
    if cry1 ==  cry2:
        st.write("# Selected both crypto's are same ")
    else:
        st.header(" Percentage change in values per day basis")
        merge_df  = df11.merge(df21, how='inner', left_index=True, right_index=True)
        merge_df.columns = [f"{cry1}", f"{cry2}"]
        merge_df.index = pd.to_datetime(df1.index)

        
        st.dataframe(merge_df)
        
        st.header(" Line Chart Based On Percentage change ")
        st.line_chart(merge_df)
    
else:
    if (diff.days < 0):
        st.write("# Select valid dates")
    elif(diff_today.days > days):
        st.write("# Select valid dates as per todays date and rolling window size \n ## selected date diff is {} days but rolling window is {}".format(diff.days ,  days))
    else:
        st.write("# Select input data")

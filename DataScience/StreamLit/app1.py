

import datetime
import yfinance as yf
import numpy as np
import pandas as pd
import streamlit as st   # streamlit run filename.py
import re
import requests

from bs4 import BeautifulSoup



def fetch_data (start_date , end_date, tickers='BTC-USD'):
    pattern = r'''<a href="/url\?q=https://finance.yahoo.com/quote/([A-Z|\-|\.]+)'''  

    x = re.findall(pattern, str(BeautifulSoup(requests.get(f"https://google.com/search?q={tickers}+on+yahoo+finance").content, 'html.parser').find_all('a')))

    
    if len(x) == 0:
        return False,False ,False 
    tickers = x[0]
     
    data = yf.download(tickers=tickers, start= start_date , end=end_date , interval = '1d')   
    
    return data, tickers , True



def main():
    st.header("Stock Price Viewer")
    
    expander_bar = st.expander("About the project")
    expander_bar.markdown("""
    * **Python libraries:** pandas, streamlit, numpy, yfinance , BeautifulSoup, requests , time
    * **Data source:** [YahooFinance](https://finance.yahoo.com/)
    * **Credit:** [@RahulAgrawal](https://rahul-agrawal.me/site/)
    """)
    st.subheader("Stock Price Viewer subhead")
    start_date = st.date_input("From" , datetime.date(2021,1,1))
    end_date  = st.date_input("Upto", datetime.date(2022,1,21))   # Y - M -D
    stock_name = st.text_input("Enter the stock name", "AMZN")
    op = st.selectbox("Select the Col for graph", ("Close", "Open", "High", "Low"))
    btn = st.button("Show Data")
    if btn:
        df,correct_ticker,status = fetch_data( start_date , end_date,tickers=stock_name)
        if status :
            pattern = r"<h1 class=\"D(.*?)\">(.*?)<\/h1>"
            x = re.findall(pattern, str(BeautifulSoup(requests.get(f"https://finance.yahoo.com/quote/{correct_ticker}").content, 'html.parser').find_all('h1')))
            try:
                x = x[0][1]
            except Exception as e:
                st.write(f"Error: {e} for X = {x}")
            x= re.split("\(", x)
            stock_name = x[0]
            stock_id= x[1][:-1]
            st.write(f'''
                    ### Showing data for \n
                    # {stock_name} 
                    #### from {start_date} to {end_date}''')
            st.subheader(f"Stock Price OF {stock_name} ")
            st.write(df.head(3) , " *** " ,df.tail(5))   # *** => <hr>
            st.write(f" ## Line Chart for {stock_id}[{op}]")
            st.line_chart(df[op])
            st.write(f" ## Line Chart for {stock_id}[Volume]")
            st.line_chart(df["Volume"])
        else:
            st.write(f"Please enter a valid stock name \n nothing found like {stock_name}")
  
    
    
if __name__ == '__main__':
    main()
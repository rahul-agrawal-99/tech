

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
  

    st.sidebar.header('User Input ')
    
    start_date = st.sidebar.date_input("From" , datetime.date(2021,1,1))
    end_date  = st.sidebar.date_input("Upto", datetime.date(2022,1,21))   # Y - M -D
    stock_name = st.sidebar.text_input("Enter the stock name", "AMZN")
    op = st.sidebar.selectbox("Select the Col for graph", ("Close", "Open", "High", "Low"))
    btn = st.sidebar.button("Show Data")
    expander_bar = st.sidebar.expander("About the project")
    expander_bar.markdown("""
    * **Python libraries:** pandas, streamlit, numpy, yfinance , BeautifulSoup, requests , time
    * **Data source:** [YahooFinance](https://finance.yahoo.com/)
    * **Credit:** [@RahulAgrawal](https://rahul-agrawal.me/site/)
    """)

    code(start_date , end_date , stock_name , op)
      
    # if btn:
    #     code(start_date , end_date , stock_name , op)
  
    
def code(start_date , end_date , stock_name , op):
        df,correct_ticker,status = fetch_data(start_date , end_date,tickers=stock_name)
        if status :
            st.write(f'''
                    ### Showing data for 
                    # {stock_name} 
                    ### [{correct_ticker}]
                    #### From {start_date} To {end_date}''')
            pattern = r"<h1 class=\"D(.*?)\">(.*?)<\/h1>"
            x = re.findall(pattern, str(BeautifulSoup(requests.get(f"https://finance.yahoo.com/quote/{correct_ticker}").content, 'html.parser').find_all('h1')))
            if len(x) > 0:
                x = x[0][1]
                x= re.split("\(", x)
                stock_name = x[0]
                stock_id= x[1][:-1]
                st.subheader(f"Trading Price OF {stock_name} ")
                st.write(df.astype(str))   # *** => <hr>
                st.write(f" ## Line Chart for {stock_id}[{op}]")
                st.line_chart(df[op])
                st.write(f" ## Line Chart for {stock_id}[Volume]")
                st.line_chart(df["Volume"])
            else:
                st.subheader(f"Trading Price OF {stock_name} ")
                st.write(df.astype(str))   # *** => <hr>
                st.write(f" ## Line Chart for {correct_ticker}[{op}]")
                st.line_chart(df[op])
                st.write(f" ## Line Chart for {correct_ticker}[Volume]")
                st.line_chart(df["Volume"])
           
        else:
            st.write(f"Please enter a valid stock name \n nothing found like \n # {stock_name}")
    
if __name__ == '__main__':
    main()
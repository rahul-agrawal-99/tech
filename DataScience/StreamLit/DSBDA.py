
'''
    Cryptocurrency Trend Analysis And Forecasting  
'''

#    Required Libraries

import datetime   # for datetime purpoes
import yfinance as yf   # for collecting data
import matplotlib.pyplot as plt   # plotting the data
import pandas as pd               # restructuring the data
import seaborn as sns           # plotting the data
from PIL import Image          # render images
from statsmodels.tsa.arima_model import ARIMA       # predict the future price
import streamlit as st                    # main dashboard
import requests                       # get page froom internet
from bs4 import BeautifulSoup          # web scrapping



#  Get top crypto currencies list from yahoo and using web scrap , get details of each crypto currency
url = "https://finance.yahoo.com/cryptocurrencies"
res = requests.get(url) 
source = res.content
soup = BeautifulSoup(source, 'html.parser')  
div = soup.find_all('tr')
div = div[1:]
cry_id =[]
cry_name = []
cry_curr = []
market_cap = []
img_link = []
last_24hrs_traded_vol = []
supply = []
for i in div:
    cry_id.append(i.find_all('td')[0].text)
    name = i.find_all('td')[1].text
    name = name.split(' ')
    length = len(name)
    market_cap.append(i.find_all('td')[5].text)  
    last_24hrs_traded_vol.append(i.find_all('td')[7].text)
    supply.append(i.find_all('td')[9].text)
    if length <= 2:
        cry_name.append(name[0])
        cry_curr.append(name[1])
    else:
        cry_name.append(name[0] + ' ' + name[1])
        cry_curr.append(name[length-1])
    try:
        img = i.find_all('img')[0]['src']
        img_link.append(img)
    except:
        img_link.append(0)
    


#  Title
st.title("- Crypto Trend Analysis - ")

#  Header Image
main_img = Image.open('img/main.jpg')
st.image(main_img, width=700 ,  caption='Crypto Trend Analysis')


crypto = sorted(cry_id)


# '''
# Fetching data from yahoo finance

# Input:

#     start_date: start date of the data
#     end_date: end date of the data
#     tickers: ID of the crypto currency
    
# Return:

#     data: dataframe contains high , low , volumne , datetime of that crypto currency
# '''
def fetch_data (start_date , end_date, tickers): 
    data = yf.download(tickers=tickers, start= start_date , end=end_date , interval = '1d')   
    return data


# '''
# Get percentage change in the crypto currency value based on first day value

# input:

#     df: dataframe containg only one column feauture
    
# output:

#     df : percentage change in the crypto currency value

# '''
def get_pch(df):
    mean = df[op].mean()
    base_price = df.iloc[0][0]
    pch_list = []
    for i in range(len(df)):
        a= (df.iloc[i][0] - base_price)  / mean
        pch_list.append(a*100) 
    df = pd.DataFrame(pch_list)
    return df


#     ----------------------  SideBar for Inputs  ----------------------

#  dividing the sidebar into two parts
col1, col2  = st.sidebar.columns((1,1 )) 
cry1 = col1.selectbox("Select Crypto 1 " , tuple(crypto) )   # get 1st crypto currency
cry2 = col2.selectbox("Select Crypto 2" , tuple(crypto) )     # get 2nd crypto currency
op = st.sidebar.selectbox("Select the Col for graph", ("Close", "Open", "High", "Low"))   # choose feature for analysis
start_date = col1.date_input("From" , datetime.date(2021,1,1))    # get start date in YYYY-MM-DD format
end_date  = col2.date_input("Upto", datetime.date(2022,4,1))   # get end date
days = st.sidebar.slider("Rolling mean Window in days",1,10,5)   # get rolling mean window for moving average
train_percent = st.sidebar.slider(" % of data used for training ",5,30,20)   # divide train data for training  
no_of_days_pred = st.sidebar.selectbox("Prediction upto days" , range(1,16) )   # get prediction upto days
chk_box = st.sidebar.checkbox("Show bar plot for Volume ", value=False, key=None, help=None, on_change=None, args=None, kwargs=None)
st.sidebar.caption(" Requires More Time")
mybtn = st.sidebar.button("Start Visualization")            # start analysis button

expander = st.sidebar.expander("About Project ")          #  about project button
expander.markdown(f""" 
                    Credits: \n
                   ## @rahul_agrawal
                   ## @shreyas_arali
                   ## @prathamesh_chatala
                  """)



#  ----------------------  Main Dashboard  ----------------------


#  divider for main dashboard for crypto 1 and 2
col1, col2 = st.columns((1,1 )) 


from datetime import datetime, timedelta
diff = end_date - start_date     # get difference between start and end date
diff_today =  datetime.today().date() - end_date    # get difference between today and end date



#   if user click on start analysis button                  And 
#       if the difference between start and end date is greater than 0 days     And
#                     if the difference between today and end date is graeter than rolling mean window
if mybtn and diff.days >0 and diff_today.days > days:
    
    #  dividing data rate
    train_percent = train_percent / 100
    
    
    # -------------------------   col1  for crypto 1------------------------------------------------------------
    
    
    df1 = fetch_data(start_date,end_date,tickers=cry1)  # get data for crypto 1
    cry1_name = cry_name[cry_id.index(cry1)]    # get name of crypto 1
    cry1_img_link = img_link[cry_id.index(cry1)]  # get image link of crypto 1
    cry1_market_cap = market_cap[cry_id.index(cry1)]    # get market cap of crypto 1
    cry1_currency = cry_curr[cry_id.index(cry1)]     # get currency in which crypto 1 is traded
    
    
    if cry1_currency == "USD": # setting currency symbol for crypto 1
        sign = "$"
    else:
        sign= "₹"
    
    col1.write(f"### Showing data for ")
    
    #  displaying crypto 1 image if it has image link 
    if cry1_img_link!=0:
        cry1_img = Image.open(requests.get(cry1_img_link, stream=True).raw)
        col1.image(cry1_img, width=300 ,  caption=f"{cry1_name}")
    else:
        col1.write(f"""No image for {cry1_name}\n\n
                   . 
                   .
                   .
                   .
                   .
                   .
                   .
                   .
                   .
                   .
                   .
                   """)
  
    expander_bar1 = col1.expander(f"About {cry1_name}")   #  about crypto 1 
    expander_bar1.markdown(f"""
                           ### Crypto Rank:
                           # {cry_id.index(cry1)+1} 
                           ### Market Cap: 
                           # {cry1_market_cap} {sign}
                           ### Total Supply:
                           # {supply[cry_id.index(cry1)]} 
                           ##### Total Volume Traded in past 24 hrs:
                           # {last_24hrs_traded_vol[cry_id.index(cry1)]} {sign}
                           """)
    
    
    #   ------------------------- line chart
    col1.subheader("Line_chart")
    col1.line_chart(df1[op])
    col1.write("***")
    
    #  -------------------------- volume traded
    col1.subheader("Volume traded")
    col1.line_chart(df1['Volume'])
    col1.write("***")
    
    #  ------------------------  current status 
    col1.subheader("Current change in price based on start date")
    col1.metric(f"{cry1}", f"{sign} {round(df1[op].iloc[len(df1)-1],3)}", f"{round(((df1[op].iloc[len(df1)-1] - df1[op].iloc[1])/ df1[op].iloc[1])*100 , 2)}%") 
    col1.caption(f"returns in {len(df1)} days")
    col1.write("***")
    
    #  --------------------------  rolling mean
    col1.subheader("Line_chart based on Rolling mean")
    df1[f'{op}-{days}d-rolling'] = df1[op].rolling(window=days).mean()
    col1.line_chart(df1.loc[: ,[op, f'{op}-{days}d-rolling']])
    col1.write("***")
    
    #  --------------------------  corr matrix 
    col1.subheader(f"Corr betn {op} and Volume")
    fig, ax = plt.subplots()
    corr = df1[[op,"Volume"]].corr()
    sns.heatmap(corr , annot=True)
    col1.pyplot(fig)
    col1.write("***")
    
    #  --------------------------  bar plot
    
    # a greater fluctuation in the stock price may be a reason behind more transactions of stocks that day
    
    if chk_box:
        col1.subheader(f"Bar-Plot For {op} and Volume")  
        fig, ax = plt.subplots()
        sns.barplot(data=df1, x = op, y="Volume")
        col1.pyplot(fig)
        col1.write("***")
    
    
    
    df11 = get_pch(pd.DataFrame(df1[op]) )
    
    
    #     --------------  Prediction for crypto1   --------
    
    col1.write(f"### Next {no_of_days_pred} days Prediction for {cry1}")   # header
    
    train_sample = int(len(df1) - len(df1)*train_percent)       # actual training sample size
    train_data_cry1 = list(df1[train_sample:][op])             # training data for crypto 1
    pred_cry1 = []                                             # prediction data list for crypto 1
    for i in range(no_of_days_pred):
        model = ARIMA(train_data_cry1, order=(4,1,0))        # ARIMA model for crypto 1 with p = 4, d = 1, q = 0
        model_fit = model.fit()
        output = model_fit.forecast()
        pred_cry1.append(output[0][0])
        train_data_cry1.append(output[0][0])
    sdate = df1.index[len(df1)-1]                           # start date
    edate = sdate +  timedelta(days=no_of_days_pred)        # end date  for plot
    pred_date_range = pd.date_range(sdate,edate-timedelta(days=1),freq='d')
    
    #     prediction plot for crypto 1
    fig , ax = plt.subplots()
    plt.plot(df1.index[train_sample:],train_data_cry1[:len(df1) - train_sample] , label = 'Actual_data')
    plt.plot(pred_date_range, pred_cry1 , label = 'predicted values' , marker = 'o' , linestyle = 'dashed')
    plt.legend()
    col1.pyplot(fig)
    col1.write("***")
    
    # ---------------- Future values metric
    
    future_cry1  =round(((pred_cry1[len(pred_cry1)-1] - df1[op].iloc[len(df1)-1] )/ df1[op].iloc[len(df1)-1])*100 , 2)
    col1.metric(f"Estimated Future price of {cry1} after {no_of_days_pred} days", f"{sign} {round(pred_cry1[len(pred_cry1)-1] , 3)}", f"{future_cry1} %") 
    col1.write("***")
   
    # -------------------------   col2  for crypto 2------------------------------------------------------------
    
    df2 = fetch_data(start_date,end_date,tickers=cry2)
    
    cry2_name = cry_name[cry_id.index(cry2)]
    cry2_img_link = img_link[cry_id.index(cry2)]
    cry2_market_cap = market_cap[cry_id.index(cry2)]
    cry2_currency = cry_curr[cry_id.index(cry2)]
    
    if cry2_currency == "USD":
        sign = "$"
    else:
        sign= "₹"
    
    col2.write(f"### Showing data for ")
    
    
    if cry2_img_link!=0:
        cry2_img = Image.open(requests.get(cry2_img_link, stream=True).raw)
        col2.image(cry2_img, width=300 ,  caption=f"{cry2_name}")
    else:
        col2.write(f"""No image for {cry2_name}\n\n
                   . 
                   .
                   .
                   .
                   .
                   .
                   .
                   .
                   .
                   .
                   .
                   """)
 
    expander_bar2 = col2.expander(f"About {cry2_name}")   #  about crypto 1 
    expander_bar2.markdown(f"""
                           ### Crypto Rank:
                           # {cry_id.index(cry2)+1} 
                           ### Market Cap: 
                           # {cry2_market_cap} {sign}
                           ### Total Supply:
                           # {supply[cry_id.index(cry2)]} 
                           ##### Total Volume Traded in past 24 hrs:
                           # {last_24hrs_traded_vol[cry_id.index(cry2)]} {sign}
                           """)
    
    col2.subheader("Line_chart")
    col2.line_chart(df2[op])
    col2.write("***")
    
    #  volume traded
    col2.subheader("Volume traded")
    col2.line_chart(df2['Volume'])
    col2.write("***")
    
    #  current status 
    col2.subheader("Current change in price based on start date")
    col2.metric(f"{cry2}", f"{sign} {round(df2[op].iloc[len(df2)-1],3)}", f"{round(((df2[op].iloc[len(df2)-1] - df2[op].iloc[1])/ df2[op].iloc[1])*100 , 2) } %")
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
    if chk_box:
        col2.subheader(f"Bar-Plot For {op} and Volume")  
        fig, ax = plt.subplots()
        sns.barplot(data=df2, x = op, y="Volume")
        col2.pyplot(fig)
        col2.write("***")
    
    
    
    df21 = get_pch(pd.DataFrame(df2[op]) )
    
    #    --------------  Prediction  --------
    
    col2.write(f"### Next {no_of_days_pred} days Prediction for {cry2}")
    train_data_cry2 = list(df2[train_sample:][op])
    pred_cry2 = []
    sdate = df2.index[len(df2)-1]  # start date
    edate = sdate +  timedelta(days=no_of_days_pred)   # end date
    pred_date_range = pd.date_range(sdate,edate-timedelta(days=1),freq='d')
    for i in range(no_of_days_pred):
        model2 = ARIMA(train_data_cry2, order=(4,1,0))
        model_fit = model2.fit()
        output = model_fit.forecast()
        pred_cry2.append(output[0][0])
        train_data_cry2.append(output[0][0])
    fig , ax = plt.subplots()
    plt.plot(df2.index[train_sample:],train_data_cry2[:len(df2) - train_sample] , label = 'Actual_data')
    plt.plot(pred_date_range, pred_cry2 , label = 'predicted values' , marker = 'o' , linestyle = 'dashed')
    plt.legend()
    col2.pyplot(fig)
    col2.write("***")
    
    #                 Future values metric
    
    future_cry2  =round(((pred_cry2[len(pred_cry2)-1] - df2[op].iloc[len(df2)-1] )/ df2[op].iloc[len(df2)-1] )*100 , 2)
    col2.metric(f"Estimated Future price of {cry2} after {no_of_days_pred} days", f"{sign} {round(pred_cry2[len(pred_cry2)-1] , 3)}", f"{future_cry2} %") 
    col2.write("***")
    
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
    
    # ------------------------------  Conclusion  --------------------------------------------
        st.header(f"Conclusion")
        st.write(f"# Based on Data Analysis of {cry1} and {cry2} ")
        if future_cry1 < 0 and future_cry2 < 0 :
            st.header("Since Both crypto's are in decline it is great time to invest")
            if future_cry1 > future_cry2:
                st.write(f"### but '{cry1}' seems better than '{cry2}' according to our analysis")
            else:
                st.write(f"### but '{cry2}' seems better than '{cry1}' according to our analysis")
                
        else:
            if future_cry1 < 0:
                st.write(f"### '{cry2}' seems great deal to invest rather than '{cry1}' "
                         f" But keep the note that differance betn {cry1} and {cry2} is {round((future_cry2 - future_cry1),3)} %")
            else:
                st.write(f"### '{cry1}' seems great deal to invest rather than '{cry2}' "
                         f"But keep the note that differance betn {cry1} and {cry2} is {round((future_cry1 - future_cry2),3)} %")
                        
else:
    if (diff.days < 0):
        st.write("# Select valid dates")
    elif(diff_today.days >= days):
        st.write(f" Today is {datetime.today().date()} but you selected {start_date} and {end_date}")
        st.write("# Select valid dates as per todays date and rolling window size \n ## selected date diff is {} days but rolling window is {}".format(diff_today.days ,  days))
    else:
        st.write("# Select input data")


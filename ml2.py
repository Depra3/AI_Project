import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mat
import numpy as np
import tensorflow as tf
from tensorflow import keras
import seaborn as sns
import os
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from time import sleep  
from stqdm import stqdm
import warnings
warnings.filterwarnings("ignore")
import matplotlib.font_manager as fonm
import prophet
import yfinance as yf 
from prophet import Prophet



def prediction2():
    st.header('전세 실거래가 예측')
    
    PATH = 'data/'
    file_list = os.listdir(PATH + 'ml_data')
    list = []
    for i in file_list:
        a = i.split('.')[0]
        if a !='':
            list.append(a)
    # list
   
    s =st.selectbox('원하는 구를 선택하세요',(list))
    # st.write(s)

    data = pd.read_csv(PATH + 'ml_data/' + s + '.csv', encoding='cp949', index_col=False)
    
    # st.write(data)

    data['CNTRCT_DE'] = pd.to_datetime(data['CNTRCT_DE'])

    close_data = data.filter(['RENT_GTN'])
    dataset = close_data.values
    training = int(np.ceil(len(dataset) * .95))

            
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)
            
    train_data = scaled_data[0:int(training), :]
            # prepare feature and labels
    x_train = []
    y_train = []
            
    for i in range(60, len(train_data)):
        x_train.append(train_data[i-60:i, 0])
        y_train.append(train_data[i, 0])
            
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    model = keras.models.Sequential()
    model.add(keras.layers.LSTM(units=64,
                                    return_sequences=True,
                                    input_shape=(x_train.shape[1], 1)))

    model.add(keras.layers.LSTM(units=64))
    model.add(keras.layers.Dense(32))
    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(1))
                
    model.compile(optimizer='adam',
                    loss='binary_crossentropy',
                    metrics='accuracy')



    for epochs in stqdm(range(10)):
        model.fit(x_train,
                    y_train,
                    epochs=1,
                    validation_split=0.2)
        sleep(0.5)
   

    # history = model.fit(x_train,
    #                     y_train,
    #                     epochs=10,
    #                     validation_split=0.2)

  
    test_data = scaled_data[training - 60:, :]
    x_test = []
    y_test = dataset[training:, :]
    for i in range(60, len(test_data)):
        x_test.append(test_data[i-60:i, 0])
            
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))



    # predict the testing data
    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)
    # evaluation metrics
    mse = np.mean(((predictions - y_test) ** 2))

    train = data[:training]
    test = data[training:]
    test['Predictions'] = predictions

    mat.rcParams['font.family']='Gulim'

    plt.figure(figsize=(15, 8))
    plt.plot(train['RENT_GTN'])
    plt.plot(test[['RENT_GTN', 'Predictions']])
    plt.title(f'{s}',fontsize=30)
    plt.xlabel('Date', fontsize=15)
    plt.ylabel("Deposit",fontsize=15)
    plt.legend(['Train', 'Test', 'Predictions'])
    st.pyplot(plt)

    # def predicts(data):
    #     df_train = data[['CNTRCT_DE', 'RENT_GTN']]
    #     df_train = df_train.rename(columns={"CNTRCT_DE": "ds", "RENT_GTN": "y"})
    #     m = Prophet()
    #     m.fit(df_train)

    #     future = m.make_future_dataframe(periods=7)
    #     forecast = m.predict(future)
    #     st.write(forecast)

    #     fig = m.plot(forecast)
    #     plt.title(f'{s}')
    #     st.pyplot(fig)

    # def main():

    #     # data = get_data(tickers = 'AAPL')
    #     st.dataframe(data)
    #     predicts(data)



    # # if __name__ == "__main__":
    # #     main()


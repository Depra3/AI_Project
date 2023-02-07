import requests
import pandas as pd
import numpy as np
import streamlit as st
import urllib
import json


data = pd.read_csv('data/bds_data.csv', encoding='cp949')
st.write("시작")
data_ud = []
# service_key = '4d42486779706d3034365957634870'
# url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/tbLnOpendataRentV/1/1000/%20/%20/%20/%20/%20/%20/%20/20220101'

# data = []
# for j in range(1, 700):
#     # st.write(data)
#     service_key = '4d42486779706d3034365957634870'
#     url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/tbLnOpendataRentV/{1+((j-1)*1000)}/{j*1000}'
    # url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/tbLnOpendataRentV/{1+((j-1)*1000)}/{j*1000}/%20/%20/%20/%20/%20/%20/%20/20230131'
    # print(url)
    # req = requests.get(url)
    # content = req.json()
    # con = content['tbLnOpendataRentV']['row']
    # # st.write(con)
    # st.dataframe(con)
# for j in range(1, 3):
#     service_key = '4d42486779706d3034365957634870'
#     url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/tbLnOpendataRentV/{1+((j-1)*1000)}/{j*1000}/2023'

#     # # 데이터 가져오기
#     # response = urllib.request.urlopen(url)
#     # json_str = response.read().decode('utf-8')

#     # # JSON -> Dict으로 변환
#     # json_object = json.loads(json_str)
#     # st.write(json_object)

#     # # Dict -> 데이터프레임으로 변환
#     # update_data = pd.json_normalize(json_object['tbLnOpendataRentV']['row'])
#     # st.write(update_data.head())
#     # st.write(update_data.count())
#     # update_data.append
#     # # st.wtite(update_data.columns)

#     print(url)
#     req = requests.get(url)
#     content = req.json()
#     con = content['tbLnOpendataRentV']['row']

#     for h in con:
#         dic = {}
#         dic['SGG_CD'] = h['SGG_CD']
#         dic['SGG_NM'] = h['SGG_NM']
#         dic['BJDONG_CD'] = h['BJDONG_CD']
#         dic['BJDONG_NM'] = h['BJDONG_NM']
#         dic['BOBN'] = h['BOBN']
#         dic['BUBN'] = h['BUBN']
#         dic['FLR_NO'] = h['FLR_NO']
#         dic['CNTRCT_DE'] = h['CNTRCT_DE']
#         dic['RENT_GBN'] = h['RENT_GBN']
#         dic['RENT_AREA'] = h['RENT_AREA']
#         dic['RENT_GTN'] = h['RENT_GTN']
#         dic['RENT_FEE'] = h['RENT_FEE']
#         dic['BLDG_NM'] = h['BLDG_NM']
#         dic['BUILD_YEAR'] = h['BUILD_YEAR']
#         dic['HOUSE_GBN_NM'] = h['HOUSE_GBN_NM']
#         # dic = data.append(pd.Serise('row', index=data.columns), ignore_index=True)
#         data_ud.append(dic, ignore_index=True)
#         st.dataframe(data_ud.count())
#   ===
# --
# df = pd.DataFrame(data)
# st.write(data)
# df['BOBN'].replace('', np.nan, inplace=True)
# df['BUBN'].replace('', np.nan, inplace=True)
# df['BLDG_NM'].replace('', np.nan, inplace=True)
# df['BUILD_YEAR'].replace('', np.nan, inplace=True)
# df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
# df['CNTRCT_DE'] = df['CNTRCT_DE'].apply(lambda x: pd.to_datetime(str(x), format="%Y/%m/%d"))
# df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
# df['CNTRCT_DE'].replace('T00:00:00', '', inplace=True)
# df = df.dropna()
# # st.write("확인?")
# st.write(df)

# st.write(df[df['CNTRCT_DE']] == '20230131')
# df = df.to_csv('data.csv',encoding='euc-kr', index=False)
# st.write(df)
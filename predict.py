# 전세 시세 예측
# st.title('전세 예측📈')

# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import matplotlib
# matplotlib.use('Agg')
# import plotly.graph_objects as go
# import geopandas as gp
# import json
# from datetime import datetime
# from dateutil.relativedelta import relativedelta
# from stqdm import stqdm
# from time import sleep
# import warnings
# warnings.filterwarnings("ignore")
# from ml2 import prediction2
# ###########################################################
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib
matplotlib.use('Agg')
import plotly.graph_objects as go
import geopandas as gp
# import json
# import matplotlib.pyplot as plt
# import tensorflow as tf
# from tensorflow import keras
# import seaborn as sns
# import joblib # 모델 내보내기
# import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from stqdm import stqdm
from time import sleep
import warnings
warnings.filterwarnings("ignore")
# from stqdm_model import stqdm_model
from ml2 import prediction2

def run_predict():
    st.title("전세 예측📈")
    st.markdown("""
    *※ 왼쪽 사이드바에 원하시는 메뉴를 선택하세요 ※*
    """)
    df = pd.read_csv('data/bds_data.csv', encoding='cp949')
    df_copy = df.copy()
    data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    sub_menu = ['전월세 월평균 그래프', '전월세 실거래수 지역 순위', '날짜별 거래', '전세예측']
    sub_choice = st.sidebar.selectbox("메뉴", sub_menu)
    # gu = np.array(j_m_mean['SGG_NM'].unique())

    if sub_choice == '전월세 월평균 그래프':
        st.subheader("전월세 월평균 그래프")
        t1, t2 = st.tabs(['전세 월평균 그래프', '월세 월평균 그래프'])
        j_m_mean = pd.read_csv('data/gu_j_m_mean.csv', encoding='cp949')
        w_m_mean = pd.read_csv('data/gu_w_m_mean.csv', encoding='cp949')
        gu = np.array(j_m_mean['SGG_NM'].unique())

        with t1:
            c1 = st.checkbox('전세 월평균 그래프', True)
        
            fig = go.Figure()
            dic = {}
            if c1:
                fig = px.scatter(width=700)
                for i in gu:
                    dic.update({i : j_m_mean[j_m_mean['SGG_NM']==i]['RENT_GTN']})
            
                for j in gu:
                    df = j_m_mean[j_m_mean['SGG_NM']==j]
                    fig.add_scatter(x=df['YM'], y=df['RENT_GTN'], name=j)
                fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(k=천만원)')
                st.plotly_chart(fig)

            else:
                st.write(j_m_mean)

        with t2:
            c1, c2 = st.columns([1,1])
            s1 = c1.checkbox('보증금 월평균 그래프', True)
            s2 = c2.checkbox('월세 월평균 그래프', True)

            p1 = c1.empty()
            p2 = c2.empty()
        
            fig = go.Figure()
            dic = {}
            if s1:
                with p1.container():
                    fig = px.scatter(width=350)
                    for i in gu:
                        dic.update({i : w_m_mean[w_m_mean['SGG_NM']==i]['RENT_GTN']})
                
                    for j in gu:
                        df = w_m_mean[w_m_mean['SGG_NM']==j]
                        fig.add_scatter(x=df['YM'], y=df['RENT_GTN'], name=j)
                    fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(k=천만원)')
                    st.plotly_chart(fig)

            else:
                c1.write(j_m_mean)
                p1 = st.empty()

            if s2:
                with p2.container():
                    fig = px.scatter(width=350)
                    for i in gu:
                        dic.update({i : w_m_mean[w_m_mean['SGG_NM']==i]['RENT_GTN']})
                
                    for j in gu:
                        df = w_m_mean[w_m_mean['SGG_NM']==j]
                    
                        fig.add_scatter(x=df['YM'], y=df['RENT_FEE'], name=j)
                    fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(만원)')
                    st.plotly_chart(fig)
            else:
                c2.write(w_m_mean)
                p2 = st.empty()
        
        # st.write(df_copy['SGG_NM'].unique())
        a = np.array(df_copy['SGG_NM'].unique())
        gu = st.multiselect('지역구 선택', a, default='강남구')
        sel_gu = []
        for i in gu:
            sel_gu.append(df_copy[df_copy['SGG_NM']==i]['BJDONG_NM'].unique())
        gu_idx1 = 0
        dong = []
        dic = {}
        for i in sel_gu:
            sel_dong = st.multiselect(f'{gu[gu_idx1]} 동 선택', i)
            dic.update({gu[gu_idx1] : sel_dong})
            gu_idx1 += 1
        fig = go.Figure()
        for gu in gu:
            for dong in dic[gu]:
                df2 = df_copy[(df_copy['SGG_NM']==gu) & (df_copy['BJDONG_NM']==dong) & (df_copy['HOUSE_GBN_NM']=='아파트') & (df_copy['RENT_GBN']=='전세') & (df_copy['CNTRCT_DE'] < '2023-01-01') & (df_copy['CNTRCT_DE'] > '2022-01-01')]
                fig.add_scatter(x=df2['CNTRCT_DE'], y=df2['RENT_GTN'], name=dong)
        fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(k=천만원)')
        st.plotly_chart(fig)

    elif sub_choice == '전월세 실거래수 지역 순위':
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("""
            💵월세 실거래수 지역 순위
            - *현재 월세 실거래수 TOP 10*🥇
            """)
            # 월세인 데이터 추출
            data_m = data[data['RENT_GBN'] == '월세']
            # 구, 동 합치기
            cols = ['SGG_NM', 'BJDONG_NM']
            data_m['주소'] = data_m[cols].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
            data_addr = data_m['주소'].value_counts().rename_axis('주소').reset_index(name='거래 수')
            #인덱스 재지정
            data_addr = data_addr.reset_index(drop=True)
            data_addr.index = data_addr.index+1

            # 그래프
            c1 = st.checkbox('월세 실거래 수 지역 순위 그래프', True)
            fig = go.Figure()
            if c1:
                fig = px.bar(x=data_addr.head(10)['주소'], y=data_addr.head(10)['거래 수'], width=350,
                            color=data_addr.head(10)['주소'])
                fig.update_layout(xaxis_title='지역 동', yaxis_title='보증금(만원)')
                st.plotly_chart(fig)
            else:
                # 데이터
                st.write(data_addr.head(10))

        # 전세 실거래 수 지역 순위(월세와 같은 방식)
        with col2:
            st.subheader("""
            💳전세 실거래수 지역 순위
            - *현재 전세 실거래수 TOP10*🏆
            """)
            data_m = data[data['RENT_GBN']=='전세']
            cols = ['SGG_NM', 'BJDONG_NM']
            data_m['주소'] = data_m[cols].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
            data_addr = data_m['주소'].value_counts().rename_axis('주소').reset_index(name='거래 수')
            data_addr = data_addr.reset_index(drop=True)
            data_addr.index = data_addr.index+1
            # 그래프
            c1 = st.checkbox('전세 실거래 수 지역 순위 그래프', True)
            fig = go.Figure()
            if c1:
                fig = px.bar(x=data_addr.head(10)['주소'], y=data_addr.head(10)['거래 수'], width=350,
                            color=data_addr.head(10)['주소'])
                fig.update_layout(xaxis_title='지역 동', yaxis_title='보증금(만원)')
                st.plotly_chart(fig)
            else:
                # 데이터
                st.write(data_addr.head(10))
    elif sub_choice == '날짜별 거래':
        st.subheader("날짜별 거래")
        ef = "data/ef.geojson"
        dgg = gp.read_file(ef,encoding='euc-kr')
        #map_df = gp.read_file(fp)
        #map_df.to_crs(pyproj.CRS.from_epsg(4326), inplace=True)
        ab = "data/dong_j_d_mean.csv"
        dff =  pd.read_csv(ab,encoding='euc-kr')
        date1 = st.date_input("날짜선택")
        date2 = st.selectbox("동선택", dgg['adm_nm'].unique())
        map_dong = dgg[dgg['adm_nm'] == f'{date2}']
        map_si = dff[dff['CNTRCT_DE'] == f'{date1}']
        merged = map_dong.set_index('adm_nm').join(map_si.set_index('BJDONG_NM'))
        fig = px.choropleth_mapbox(merged, geojson=merged.geometry, locations=merged.index, color="RENT_GTN", mapbox_style="carto-positron", zoom=9.8,
        center = {"lat": 37.575651, "lon": 126.97689}, opacity=0.6)
        fig.update_geos(fitbounds="locations", visible=True)
        #fig.show()
        if  merged["RENT_GTN"].values > 0:
            st.plotly_chart(fig)
        else:
            st.markdown('# 금일 거래는 없습니다.')
            st.plotly_chart(fig)
    elif sub_choice == '전세예측':
        st.subheader("전세예측")
        prediction2()



    # a = np.array(df['SGG_NM'].unique())
    # gu = st.multiselect('지역구 선택',a ,default='강남구')
    # sel_gu = []
    # for i in gu:
    #     sel_gu.append(df[df['SGG_NM']==i]['BJDONG_NM'].unique())
    # gu_idx1 = 0
    # dong = []
    # dic = {}
    # for i in sel_gu:
    #     sel_dong = st.multiselect(f'{gu[gu_idx1]} 동 선택', i)
    #     dic.update({gu[gu_idx1] : sel_dong})
    #     gu_idx1 += 1
    # fig = go.Figure()
    # for gu in gu:
    #     for dong in dic[gu]:
    #         df2 = df[(df['SGG_NM']==gu) & (df['BJDONG_NM']==dong) & (df['HOUSE_GBN_NM']=='아파트') & (df['RENT_GBN']=='전세') & (df['CNTRCT_DE'] < '2023-01-01') & (df['CNTRCT_DE'] > '2022-01-01')]
    #         fig.add_scatter(x=df2['CNTRCT_DE'], y=df2['RENT_GTN'], name=dong)
    # fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(k=천만원)')
    # st.plotly_chart(fig)

    # ef = "data/ef.geojson"
    # dgg = gp.read_file(ef,encoding='euc-kr')
    # #map_df = gp.read_file(fp)
    # #map_df.to_crs(pyproj.CRS.from_epsg(4326), inplace=True)
    # ab = "data/dong_j_d_mean.csv"
    # dff =  pd.read_csv(ab,encoding='euc-kr')
    # date1 = st.date_input("날짜선택")
    # date2 = st.selectbox("동선택", dgg['adm_nm'].unique())
    # map_dong = dgg[dgg['adm_nm'] == f'{date2}']
    # map_si = dff[dff['CNTRCT_DE'] == f'{date1}']
    # merged = map_dong.set_index('adm_nm').join(map_si.set_index('BJDONG_NM'))
    # fig = px.choropleth_mapbox(merged, geojson=merged.geometry, locations=merged.index, color="RENT_GTN", mapbox_style="carto-positron", zoom=9.8,
    # center = {"lat": 37.575651, "lon": 126.97689}, opacity=0.6)
    # fig.update_geos(fitbounds="locations", visible=True)
    # #fig.show()
    # if  merged["RENT_GTN"].values > 0:
    #     st.plotly_chart(fig)
    # else:
    #     st.markdown('# 금일 거래는 없습니다.')
    #     st.plotly_chart(fig)
    
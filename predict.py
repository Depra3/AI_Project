# 전세 시세 예측

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib
matplotlib.use('Agg')
import plotly.graph_objects as go


def run_predict():
    st.title('전세 예측📈')
    df = pd.read_csv('data/bds_data.csv', encoding='cp949')
    
    a = np.array(df['SGG_NM'].unique())
    gu = st.multiselect('지역구 선택',a ,default='강남구')
    # st.write('==========================')
    sel_gu = []
    for i in gu:
        sel_gu.append(df[df['SGG_NM']==i]['BJDONG_NM'].unique())

    # st.write(gu)
    # st.write(type(gu))

    # st.write(sel_gu)
    # st.write(type(sel_gu))​
    
    gu_idx1 = 0
    dong = []
    dic = {}
    for i in sel_gu:
        sel_dong = st.multiselect(f'{gu[gu_idx1]} 동 선택', i)
        dic.update({gu[gu_idx1] : sel_dong})
        gu_idx1 += 1

    # st.write(dic)
    # st.write(type(dic))


    # st.write(dong)
    # st.write(type(dong))

    fig = go.Figure()
    for gu in gu:
        for dong in dic[gu]:
            df2 = df[(df['SGG_NM']==gu) & (df['BJDONG_NM']==dong) & (df['HOUSE_GBN_NM']=='아파트') & (df['RENT_GBN']=='전세') & (df['CNTRCT_DE'] < '2023-01-01') & (df['CNTRCT_DE'] > '2022-01-01')]
            fig.add_scatter(x=df2['CNTRCT_DE'], y=df2['RENT_GTN'], name=dong)
    
    fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(k=천만원)')

    st.plotly_chart(fig)
    
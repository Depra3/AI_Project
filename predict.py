# 전세 시세 예측
# st.title('전세 예측📈')

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib
matplotlib.use('Agg')
import plotly.graph_objects as go
import geopandas as gp
import json

def run_predict():
    st.title('전세 예측')
    df = pd.read_csv('data/bds_data.csv', encoding='cp949')
    a = np.array(df['SGG_NM'].unique())
    gu = st.multiselect('지역구 선택',a ,default='강남구')
    sel_gu = []
    for i in gu:
        sel_gu.append(df[df['SGG_NM']==i]['BJDONG_NM'].unique())
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
            df2 = df[(df['SGG_NM']==gu) & (df['BJDONG_NM']==dong) & (df['HOUSE_GBN_NM']=='아파트') & (df['RENT_GBN']=='전세') & (df['CNTRCT_DE'] < '2023-01-01') & (df['CNTRCT_DE'] > '2022-01-01')]
            fig.add_scatter(x=df2['CNTRCT_DE'], y=df2['RENT_GTN'], name=dong)
    fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(k=천만원)')
    st.plotly_chart(fig)
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
    
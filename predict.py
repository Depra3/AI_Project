# 전세 시세 예측

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
    st.title('전세 예측📈')
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
    m_df = pd.read_csv('data/bds_data.csv', encoding='euc-kr')
    m_gu = pd.read_csv('data/gu_mean.csv', encoding='euc-kr')
    geo = gp.read_file('data/layer1 (2).json')
    st.header("지역구별 평균 실거래가 확인")
    with open('data/layer1 (2).json', encoding='UTF-8') as f:
        data = json.load(f)
    for x in data['features']:
        x['id'] = x['properties']['SIG_KOR_NM']
    for idx, _ in enumerate(data['features']):
        print(data['features'][idx]['id'])
    mapper = [
    ('송파구', '송파구'),
    ('강남구', '강남구'),
    ('성동구', '성동구'),
    ('구로구', '구로구'),
    ('영등포구', '영등포구'),
    ('양천구', '양천구'),
    ('도봉구', '도봉구'),
    ('서초구', '서초구'),
    ('관악구', '관악구'),
    ('중구', '중구'),
    ('동대문구', '동대문구'),
    ('광진구', '광진구'),
    ('은평구', '은평구'),
    ('중랑구', '중랑구'),
    ('노원구', '노원구'),
    ('강동구', '강동구'),
    ('동작구', '동작구'),
    ('마포구', '마포구'),
    ('강북구', '강북구'),
    ('강서구', '강서구'),
    ('용산구', '용산구'),
    ('성북구', '성북구'),
    ('금천구', '금천구'),
    ('종로구', '종로구'),
    ('서대문구', '서대문구'),
    ]
    get_region = lambda SGG_NM: [x[1] for x in mapper if x[0] == SGG_NM][0]
    m_gu['geo_region'] = m_gu.SGG_NM.apply(get_region)
    cal = st.date_input('날짜를 선택하세요')
    sel=m_gu[m_gu['CNTRCT_DE']== f'{cal}']
    fig = px.choropleth_mapbox(
        sel,
        geojson=data,
        locations='geo_region',
        color='RENT_GTN',
        color_continuous_scale=["orange", "red",
                                         "green", "blue",
                                         "purple"],
        # featureidkey="properties.CTP_KOR_NM", # featureidkey를 사용하여 id 값을 갖는 키값 지정
        mapbox_style="carto-positron",
        zoom=10,
        center = {"lat": 37.517, "lon": 127.047},
        opacity=0.6,
        labels={'RENT_GTN':'가격'}
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    # fig.show()
    st.plotly_chart(fig)
    
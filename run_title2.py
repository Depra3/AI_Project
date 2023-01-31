# -*- coding : utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu



def run_title2():
    data = pd.read_csv('data/bds_data_1.csv', encoding='cp949')
    st.markdown("## 전월세 검색결과")

    # 해당 구 선택
    st.sidebar.selectbox('구', data['SGG_NM'].unique())

    # 해당 동 선택
    # with st.sidebar.selectbox('동', data['BJDONG_NM'].unique()):
    #     if data[['SGG_NM'] == '성북구']:
    #         data['BJDONG_NM']
        # pass
    # 보증금
    # 월세
    # 면적(평) 
    # 전월세 선택
    # 
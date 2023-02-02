# -*- coding : utf-8 -*-

# 전월세 검색 탭

import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import math



def run_search():
    st.markdown("## 전월세 검색결과🔍️")
    data = pd.read_csv('data/bds_data.csv', encoding='cp949')

    # 해당 구 선택
    gu = data['SGG_NM'].unique()
    gu_select = st.sidebar.selectbox('구를 선택해주세요', gu)

    # 해당 동 선택
    # gu_select = data['SGG_NM'].unique()
    # a = st.sidebar.selectbox('구', gu_select)
    dong = data['BJDONG_NM'][data['SGG_NM'] == gu_select].unique()
    dong_selcet = st.sidebar.selectbox('동을 선택해주세요', dong)

    # 전월세 선택
    rent_type = data['RENT_GBN'].unique()
    type_select = st.sidebar.selectbox('전세/월세', rent_type)

    # 보증금 범위 설정
    rent_gtn_list = data['RENT_GTN'].values.tolist()
    rent_gtn_select = st.sidebar.select_slider('보증금(만단위)', 
    options = np.arange(min(rent_gtn_list), max(rent_gtn_list)+1),
    value = (min(rent_gtn_list), max(rent_gtn_list)))

    # 월세 범위 설정
    # rent_fee_list = 데이터의 유니크 값을 리스트로 한 것
    # rent_fee_select = 
    rent_fee_list = data['RENT_FEE'].values.tolist()
    rent_fee_select = st.sidebar.select_slider('월세(만단위)', 
    options = np.arange(0, max(rent_fee_list)+1),
    value = (0, max(rent_fee_list)))

    # 면적(평) 
    # pyeong()
    rent_area_list = data['RENT_AREA'].values.tolist()
    min_rent_list = min(rent_area_list)
    max_rent_list = max(rent_area_list)
    # 제곱미터 => 평 전환
    min_pyeong = math.floor(min_rent_list / 3.3058)
    max_pyeong = math.ceil(max_rent_list / 3.3058)
    rent_area_select = st.sidebar.select_slider('면적(평)', 
        options = np.arange(min_pyeong, max_pyeong +1),
        value = (min_pyeong, max_pyeong))
    rent_area_min = rent_area_select[0] * 3.3058
    rent_area_max = rent_area_select[1] * 3.3058
    

    # 버튼 생성
    if st.sidebar.button('조회'):
        gu_search = (data['SGG_NM'] == gu_select)
        dong_search = (data['BJDONG_NM'] == dong_selcet)
        type_search = (data['RENT_GBN'] == type_select)
        rent_gtn_search = (rent_gtn_select[0] <= data['RENT_GTN']) & (data['RENT_GTN'] <= rent_gtn_select[1])
        rent_fee_search = (rent_fee_select[0] <= data['RENT_FEE']) & (data['RENT_FEE'] <= rent_fee_select[1])
        rent_area_search = (rent_area_select[0]<= data['RENT_AREA']) & (data['RENT_AREA'] <= rent_area_select[1])

        data_search = data[gu_search & dong_search & type_search & rent_gtn_search & rent_fee_search & rent_area_search]

        data_search['FLR_NO'] = data_search['FLR_NO'].astype(str) + '층'
        data_search = data_search.drop(['SGG_CD', 'BJDONG_CD'], axis=1)

        cols = ['BOBN', 'BUBN']
        data_search['번지'] = data_search[cols].apply(lambda row: '-'.join(row.values.astype(str)) 
                                            if row['BUBN'] != 0
                                            else row['BOBN'], axis=1)

        data_search['BLDG_NM'] = data_search['BLDG_NM'].str.replace("아파트", "")
        data_search['BLDG_NM'] = data_search['BLDG_NM'].str.replace("오피스텔", "")

        cols1 = ['SGG_NM', 'BJDONG_NM', '번지', 'BLDG_NM', 'HOUSE_GBN_NM', 'FLR_NO']
        data_search['주소'] = data_search[cols1].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
        data_search = data_search.drop(['SGG_NM', 'BJDONG_NM', 'BOBN', 
    'BUBN', 'FLR_NO', 'BLDG_NM', '번지', 'HOUSE_GBN_NM'], axis=1)

        data_search['RENT_AREA'] = data_search['RENT_AREA'].apply(lambda x: math.trunc(x / 3.3058))
        data_search.columns = ['계약일', '전월세 구분', '임대면적(평)',
     '보증금(만원)', '임대료(만원)', '건축년도', '주소']

        data_search = data_search[['계약일', '주소', '보증금(만원)', 
     '임대료(만원)', '임대면적(평)', '건축년도', '전월세 구분']]

        data_search = data_search.reset_index(drop=True)
        data_search.index = data_search.index+1

        st.write(data_search)

# def pyeong():
#     data = pd.read_csv('data/bds_data.csv', encoding='cp949')
#     rent_area_list = data['RENT_AREA'].values.tolist()
#     min_list = min(rent_area_list)
#     max_list = max(rent_area_list)
#     min_p = math.floor(min_list / 3.3058)
#     max_p = math.ceil(max_list / 3.3058)
#     st.sidebar.select_slider('평수', 
#         options = np.arange(min_p, max_p+1),
#         value = (min_p, max_p))
    
    

        


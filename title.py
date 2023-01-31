import streamlit as st
from streamlit_option_menu import option_menu


def title():

    st.title('TITLE')

    selected3 = option_menu(None, ["🏠Home", " 🔎전월세 검색",  "📊전세vs월세?", '💬건의사항'], 
        # icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "gray", "font-size": "15px"}, 
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#47C83E"},
        }
    )
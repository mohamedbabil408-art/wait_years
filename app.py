# -*- coding: utf-8 -*-
"""
تطبيق حساب سنوات الانتظار لطلاب الدراسة الخارجية (الأبطال)
يعمل على Streamlit Cloud - لا حاجة لـ tkinter
"""

import streamlit as st
import time
import os

# ============ إعدادات الصفحة العامة ============
st.set_page_config(
    page_title="حساب سنوات الانتظار - الخارجي الأبطال",
    page_icon="🎓",
    layout="centered",
)

# ============ تنسيق CSS: خلفية سوداء وألوان ============
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    h1, h2, h3, p, label, .stMarkdown {
        color: #FFFFFF !important;
        text-align: center;
    }
    .stTextInput input {
        text-align: center;
        background-color: #1a1a1a;
        color: #FFFFFF;
        border: 1px solid #00C896;
    }
    div.stButton > button {
        background-color: #00C896;
        color: #000000;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 20px;
        border: none;
        display: block;
        margin: 0 auto;
    }
    div.stButton > button:hover {
        background-color: #00a37a;
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============ حالة الجلسة: هل انتهت شاشة الترحيب؟ ============
if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

WELCOME_IMAGE_PATH = "welcome.png"  # ضع صورتك بهذا الاسم بجانب app.py في GitHub

# ============ شاشة الترحيب ============
if not st.session_state.splash_done:
    placeholder = st.empty()
    with placeholder.container():
        st.write("")
        st.write("")
        if os.path.exists(WELCOME_IMAGE_PATH):
            st.image(WELCOME_IMAGE_PATH, use_container_width=True)
        else:
            st.markdown(
                "<h1 style='color:#00C896;'>مرحباً بطلاب الخارجي الأبطال</h1>",
                unsafe_allow_html=True,
            )

    time.sleep(3)
    st.session_state.splash_done = True
    placeholder.empty()
    st.rerun()

# ============ الواجهة الرئيسية (بعد الترحيب) ============
else:
    st.markdown("<h1 style='color:#00C896;'>حساب سنوات الانتظار</h1>", unsafe_allow_html=True)
    st.write("")

    year_input = st.text_input("اكتب سنة امتحانك الأخير (مثال: 2023):")

    if st.button("حساب السنوات"):
        raw = year_input.strip()

        if not raw.isdigit():
            st.error("الرجاء إدخال سنة صحيحة (أرقام فقط)، مثال: 2023")
        else:
            x = int(raw)

            wait_year_1 = x + 1
            wait_year_2 = x + 2
            new_submit_year = x + 3
            new_exam_year = x + 4

            st.write("")
            st.markdown(
                f"<h3 style='color:#ff6b6b;'>{wait_year_1} &nbsp;&nbsp; انتظار</h3>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<h3 style='color:#ff6b6b;'>{wait_year_2} &nbsp;&nbsp; انتظار</h3>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<h3 style='color:#ffd166;'>{new_submit_year} &nbsp;&nbsp; تقديم</h3>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<h3 style='color:#06d6a0;'>{new_exam_year} &nbsp;&nbsp; امتحان</h3>",
                unsafe_allow_html=True,
            )

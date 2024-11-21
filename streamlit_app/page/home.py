import streamlit as st
import streamlit.components.v1 as components
import codecs
import requests
import os
import time

def st_slideshow(photoslider_html, height=300):
    current_dir = os.path.dirname(__file__)
    full_path = os.path.join(current_dir, photoslider_html)

    with codecs.open(full_path, 'r', 'utf-8') as slideshow_file:
        page = slideshow_file.read()
    components.html(page, height=height)

# def fetch_notifications():
#     if st.session_state.user:
#         user_id = st.session_state.user['user_id']
#         response = requests.get(f"http://localhost:8000/api/notifications/")
#         if response.status_code == 200:
#             notifications = response.json()
#             for notification in notifications:
#                 st.toast(notification['message'], icon="🔔")
#         else:
#             st.error("Failed to fetch notifications")

def show():
    _, center_col, _ = st.columns([1, 1, 1])

    with center_col:
        st.markdown(
            """
            <div style='text-align: center;'>
                <img src='http://localhost:8000/media/profiles/square_logo_dark.png' width='200'>
                <br><br><br>
            </div>
            """,
            unsafe_allow_html=True
        )

    st_slideshow("slider.html")

    st.markdown("<h3 style='text-align: center; font-family: \"Montserrat\", sans-serif;'>The Sweetest Spot in Town!</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; font-family: \"Montserrat\", sans-serif;'>Explore our delicious cakes and treats!</h4>", unsafe_allow_html=True)

    _, center_col, _ = st.columns([1, 2, 1])
    with center_col:
        if st.button("Explore Cakes", use_container_width=True):
            st.session_state.page = "cakes"
            st.rerun()

    # while True:
    #     fetch_notifications()
    #     time.sleep(60)

if __name__ == '__main__':
    show()
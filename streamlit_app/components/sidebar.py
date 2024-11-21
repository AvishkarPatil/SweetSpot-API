import streamlit as st
import requests

# LOGO_URL_LARGE = "static/large_logo.png"
# LOGO_URL_SMALL = "static/small_logo.png"

def sidebar():
    with st.sidebar:

        # st.logo(
        #     LOGO_URL_LARGE,
        #     link="https://streamlit.io/gallery",
        #     icon_image=LOGO_URL_SMALL,
        # )

        st.markdown(f"""
                    <div style='text-align: center;'>
                        <a href="#">
                            <img src='http://localhost:8000/media/profiles/land_logo_dark.png' width='250'>
                        </a>
                    </div>
                """, unsafe_allow_html=True)

        st.markdown("<h2 style='text-align: center;'></h2>", unsafe_allow_html=True)

        if st.session_state.user:
            user_id = st.session_state.user['user_id']
            response = requests.get(f"http://localhost:8000/api/customers/{user_id}/")
            if response.status_code == 200:
                user = response.json()
                profile_pic = user['profile_pic'] if user[
                    'profile_pic'] else "https://cdn-icons-png.flaticon.com/512/219/219983.png"
                first_name = user['first_name']
            else:
                profile_pic = "https://cdn-icons-png.flaticon.com/512/219/219983.png"
                first_name = "User"
        else:
            profile_pic = "https://cdn-icons-png.flaticon.com/512/219/219983.png"
            first_name = "User"

        st.markdown(f"""
                    <div style='text-align: center;'>
                        <img src='{profile_pic}' style='width: 70px; height: 70px; border-radius: 50%;'><br><br>
                        <p><strong>Hey {first_name}!</strong></p>
                    </div>
                """, unsafe_allow_html=True)

        # Navigation buttons
        if st.button("🏠 Home"):
            st.session_state.page = "home"
            st.rerun()

        if st.button("🎂 Cakes"):
            st.session_state.page = "cakes"
            st.rerun()

        if st.button("🏪 Stores"):
            st.session_state.page = "store"
            st.rerun()

        if st.button("📞 Contact"):
            st.session_state.page = "contact"
            st.rerun()

        if st.session_state.user:
            if st.button("🛒 Cart"):
                st.session_state.page = "cart"
                st.rerun()

            if st.button("📦 Orders"):
                st.session_state.page = "orders"
                st.rerun()
            if st.button("👤 Profile"):
                st.session_state.page = "profile"
                st.rerun()
            if st.button("🔐 Logout"):
                st.session_state.user = None
                st.experimental_set_query_params(user=None)
                st.rerun()
        else:
            if st.button("🔐 Login / Register"):
                st.session_state.page = "auth"
                st.rerun()
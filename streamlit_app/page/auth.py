import streamlit as st
import requests
import time
from streamlit_cookies_controller import CookieController

cookies = CookieController()

base_url = "http://localhost:8000"

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap');

    body {
        font-family: 'Lato', sans-serif;
        background-color: #1E1E1E;
        color: #FFFFFF;
    }

    .stTabs {
        background-color: #1E1E1E;
        padding: 10px 10px 30px;
        border-radius: 15px;
        margin-bottom: 30px;
    }

    .stTabs [data-baseweb="tab-list"] {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        justify-content: center;
        padding: 7px;
    }

    .stTabs [data-baseweb="tab"] {
        flex-grow: 0;
        flex-shrink: 0;
        flex-basis: auto;
        height: auto;
        white-space: normal;
        border-radius: 5px;
        color: #FFFFFF;
        background-color: #2C2C2C;
        border: 1px solid #3A3A3A;
        padding: 10px 15px;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s ease;
        text-align: center;
        min-width: 100px;
    }

    .stTabs [data-baseweb="tab"]:hover {
        background-color: #3A3A3A;
    }

    .stTabs [aria-selected="true"] {
        background-color: #4A4A4A;
        color: #FFFFFF;
        border: 1px solid #5A5A5A;
    }

    .stTextInput > div > div > input {
        background-color: #2C2C2C;
        color: #FFFFFF;
    }

    .stForm {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
    }

    .stForm > div {
        margin-bottom: 20px;
    }

    .stButton > button,
    .stForm [data-testid="stFormSubmitButton"] > button {
        background-color: #FF4B4B;
        color: white;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        border-radius: 5px;
        transition: all 0.3s ease;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        width: 100%;
        margin-top: 10px;
        cursor: pointer;
    }

    .stButton > button:hover,
    .stForm [data-testid="stFormSubmitButton"] > button:hover {
        background-color: #FF6B6B;
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }

    .stButton > button:active,
    .stForm [data-testid="stFormSubmitButton"] > button:active {
        background-color: #FF3333;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transform: translateY(2px);
    }

    /* Ensure text is always visible */
    .stButton > button > div,
    .stForm [data-testid="stFormSubmitButton"] > button > div {
        color: white !important;
    }

    .success-message {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
        text-align: center;
        animation: fadeIn 0.5s;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .profile-pic {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        object-fit: cover;
        margin-bottom: 10px;
    }

    .sidebar .sidebar-content {
        background-color: #2C2C2C;
    }

    .sidebar .stButton > button {
        width: 100%;
        margin-bottom: 10px;
        background-color: #FF4B4B;
        color: white;
        border: none;
        padding: 10px 15px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .sidebar .stButton > button:hover {
        background-color: #FF6B6B;
    }
    </style>
""", unsafe_allow_html=True)

def show():
    _, center_col, _ = st.columns([1, 2, 1])

    with center_col:
        st.markdown("""
            <h1 style='text-align: center; font-family: "Montserrat", sans-serif; font-size: 2rem; color: #FFFFFF;'>
                🍰 Welcome to SweetSpot 🍰
            </h1>
            <br><br>
        """, unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs(["LOGIN", "SIGN UP", "GUEST️"])

        with tab1:
            login_tab()

        with tab2:
            signup_tab()

        with tab3:
            guest_tab()


def login_tab():
    st.markdown("<h4 style='text-align: center; color: #FF4B4B;'>Login to Existing Account</h4>", unsafe_allow_html=True)
    with st.form(key='login_form'):
        email = st.text_input("Enter your email")
        password = st.text_input("Enter your password", type="password")
        submit_button = st.form_submit_button(label="Login")

    if submit_button:
        login_data = {"email": email, "password": password}
        response = requests.post(f"{base_url}/api/customers/login/", json=login_data)
        if response.status_code == 200:
            user_data = response.json()
            st.session_state.user = user_data
            st.experimental_set_query_params(user=user_data['username'])
            st.success("Logged in successfully!")
            st.session_state.page = "home"
            # time.sleep(5)
            st.rerun()
        else:
            st.error(f"Login failed: {response.json().get('message', 'Invalid credentials')}")


def signup_tab():
    st.markdown("<h4 style='text-align: center; color: #FF4B4B;'>Create a New Account</h4>", unsafe_allow_html=True)
    with st.form(key='signup_form'):
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("First Name")
        with col2:
            last_name = st.text_input("Last Name")

        col3, col4 = st.columns(2)
        with col3:
            email = st.text_input("Email")
        with col4:
            username = st.text_input("Username")

        col5, col6 = st.columns(2)
        with col5:
            password = st.text_input(
                "Create your password",
                type="password",
                help="**Password must be:**\n"
                     "- **Between 8 and 20 characters long**\n"
                     "- **Contain at least one lowercase letter**\n"
                     "- **Contain at least one uppercase letter**\n"
                     "- **Contain at least one digit**\n"
                     "- **Contain at least one special character from [@$!%*?&]**"
            )
        with col6:
            confirm_password = st.text_input("Confirm password", type="password")

        address = st.text_input("Address")

        col7, col8 = st.columns(2)
        with col7:
            city = st.text_input("City")
        with col8:
            state = st.text_input("State")

        col9, col10 = st.columns(2)
        with col9:
            pincode = st.text_input("Pincode")
        with col10:
            mobile_no = st.text_input("Mobile Number")

        submit_button = st.form_submit_button(label="Sign Up")

    if submit_button:
        if password != confirm_password:
            st.error("Passwords do not match. Please try again.")
        else:
            signup_data = {
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "password": password,
                "mobile_no": mobile_no,
                "address": address,
                "city": city,
                "state": state,
                "pincode": pincode,
                "username": username
            }
            response = requests.post(f"{base_url}/api/customers/register/", json=signup_data)

            # Debug box to display the response
            with st.expander("Debug Response", expanded=False):
                st.write("Response Status Code:", response.status_code)
                st.write("Response Headers:")
                st.json(dict(response.headers))
                st.write("Response Content:")
                try:
                    st.json(response.json())
                except requests.exceptions.JSONDecodeError:
                    st.text(response.text)

            if response.status_code == 201:
                st.success("Account created successfully! Please login.")
            else:
                response_data = response.json()
                if response_data.get("status") == False:
                    error_messages = []
                    for field, errors in response_data.get("errors", {}).items():
                        for error in errors:
                            error_messages.append(f"{field.capitalize()}: {error}")

                    if error_messages:
                        st.error("Registration failed. Please correct the following errors:")
                        for message in error_messages:
                            st.error(message)
                    else:
                        st.error(f"Registration failed: {response_data.get('message', 'Unknown error')}")
                else:
                    st.error(f"Signup failed: {response.text}")


def guest_tab():
    st.markdown("<h4 style='text-align: center; color: #FF4B4B;'>Login as a guest</h4>", unsafe_allow_html=True)
    if st.button("Login as Guest", key="guest", help="Login as a guest", use_container_width=True):
        st.session_state.user = {"is_guest": True}
        st.query_params(user="guest")
        st.success("Logged in as guest!")
        st.rerun()

if __name__ == "__main__":
    show()
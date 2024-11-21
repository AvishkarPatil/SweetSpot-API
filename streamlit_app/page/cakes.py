
import streamlit as st
import requests

def show():
    # st.title("Our Cakes")
    user_name = ""
    if st.session_state.user:
        user_id = st.session_state.user['user_id']
        response = requests.get(f"http://localhost:8000/api/customers/{user_id}/")
        if response.status_code == 200:
            user_data = response.json()
            user_name = user_data.get('first_name', "")

    st.markdown(f"""
            <div style='text-align: left; font-size: 24px; font-weight: bold; margin-bottom: 20px;  color: #DDDDDD; text-shadow: 2px 2px 4px #000000;'><i>
                🫰🏽 What’s Your Sweet Pick Today, <span style='color:#FF69B4;'>{user_name}</span>?</i>
            </div>
        """, unsafe_allow_html=True)

    # st.markdown("<hr>", unsafe_allow_html=True)

    # st.markdown(f"#### *🫰🏽 What’s Your Sweet Pick Today, <span style='color:#FF69B4;'>{user_name}</span>?*",
    #             unsafe_allow_html=True)


    st.markdown("""
        <style>
        .cake-box {
            background-color: #2C2C2C;
            border-radius: 15px;
            padding-left: 15px;
            padding-right: 15px;
            padding-top: 15px;
            margin-bottom: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            text-align: center;
        }
        .cake-details {
            background-color: #2C2C2C;
            border-radius: 10px;
            padding: 5px;  
            margin-top: 2px;
            text-align: center;
            position: relative;
        }
        .cake-name {
            color: #FFFFFF;
            white-space: nowrap;
            font-size: 16px;
            overflow: hidden;
            text-overflow: ellipsis;
            margin-bottom: 0px;
        }

        .stButton button {
            font-size: 12px; 
            padding: 8px 12px;
        }
        </style>
    """, unsafe_allow_html=True)

    response = requests.get("http://localhost:8000/api/cakes/")
    if response.status_code == 200:
        cakes = response.json()
    else:
        st.error("Failed to fetch cakes data")
        return

    cols = st.columns(4)
    for index, cake in enumerate(cakes):
        with cols[index % 4]:
            st.markdown(f"""
                <div class="cake-box">
                    <img src="{cake['image']}" style="width: 100%; border-radius: 10px;">
                    <div class="cake-details">
                        <div class="cake-name">{cake['name']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Cart", key=f"add_to_cart_{cake['id']}", icon="🧺", use_container_width=True):
                    if st.session_state.user:
                        if 'user_id' in st.session_state.user:
                            add_to_cart(cake['id'])
                        else:
                            st.toast("User ID not found in session state.")
                    else:
                        st.toast("You need to be logged in to add items to the cart", icon="⚠️")
            with col2:
                if st.button("Customize", key=f"customize_{cake['id']}", icon="🍴", use_container_width=True):
                    st.session_state.page = "customize"
                    st.session_state.cake_id = cake['id']
                    st.rerun()

            if st.button("View Details", key=f"view_details_{cake['id']}", use_container_width=True):
                st.session_state.page = "cake_details"
                st.session_state.cake_id = cake['id']
                st.rerun()

def add_to_cart(cake_id):
    if not st.session_state.user or 'user_id' not in st.session_state.user:
        st.toast("You need to be logged in to add items to the cart.", icon="⚠️")
        return

    customer_id = st.session_state.user['user_id']
    data = {
        "customer": customer_id,
        "cake": cake_id,
        "quantity": 1,
        "customization": None
    }

    response = requests.post("http://localhost:8000/api/add-cake-to-cart/", json=data)

    if response.status_code in [200, 201]:
        st.toast("Added to cart!", icon="✅")
    else:
        st.toast("Failed to add to cart.", icon="❌")



if __name__ == "__main__":
    show()
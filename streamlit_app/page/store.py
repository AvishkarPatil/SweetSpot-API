import streamlit as st
import requests

def fetch_stores():
    response = requests.get("http://localhost:8000/api/stores/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch stores")
        return []

def fetch_cakes(store_id):
    response = requests.get(f"http://localhost:8000/api/stores/{store_id}/cakes/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch cakes")
        return []

def show():
    stores = fetch_stores()

    st.markdown("""
        <div style='text-align: center; font-size: 28px; font-weight: bold; color: #DDDDDD; text-shadow: 2px 2px 4px #000000;'>
            🎂 Cakes to Your Door: Find Stores 🏪
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)


    st.markdown("""
            <style>
            .store-image {
                border: 2px solid #2C2C2C;
                border-radius: 10px;
                width: 100px;
                height: 100px;
                display: block;
                margin: auto;
            }
            .store-details {
                font-family: 'Arial', sans-serif;
                background-color: #1d1d1de0;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 10px;
                color: #FFFFFF;
                height: 100px;
            }
            .store-name {
                font-size: 20px;
                font-weight: bold;
                color: #FFFFFF;
                margin-bottom: 5px;
            }
            .store-address {
                font-size: 14px;
                color: #CCCCCC;
            }
            </style>
        """, unsafe_allow_html=True)

    for store in stores:
        col1, col2, col3 = st.columns([1, 4, 1])
        with col1:
            st.markdown(f"""
                <div class="store-image">
                    <img src="{store['store_image']}" style="width: 100%; height: 100%; border-radius: 10px;">
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class="store-details">
                    <div class="store-name">{store['name']}</div>
                    <div class="store-address">{store['address']}, {store['city']} - Contact: {store['contact_number']}</div>
                </div>
            """, unsafe_allow_html=True)

            # st.subheader(store["name"])
            # st.write(f"{store['address']}, {store['city']} - Contact: {store['contact_number']}")
        with col3:
            if st.button("View Our Cakes", key=store["id"]):
                st.session_state.selected_store = store["id"]
                st.session_state.selected_store_name = store["name"]
                st.session_state.page = "store_cakes"
                st.rerun()

if __name__ == "__main__":
    show()
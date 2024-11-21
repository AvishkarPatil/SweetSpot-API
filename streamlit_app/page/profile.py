import streamlit as st
import requests


def show():
    # st.title("User Profile")
    #
    st.markdown(f"<div style='text-align: left; font-size: 25px;'><strong>Your Profile 👉🏽</strong></div>", unsafe_allow_html=True)


    if st.session_state.user:
        user_id = st.session_state.user['user_id']
        response = requests.get(f"http://localhost:8000/api/customers/{user_id}/")

        if response.status_code == 200:
            user = response.json()

            # Create 7 columns
            cols = st.columns(7)

            with cols[3]:
                if user['profile_pic']:
                    st.markdown(
                        f"<img src='{user['profile_pic']}' style='width:100px; height:100px; border-radius:50%;'>",
                        unsafe_allow_html=True)
                else:
                    st.markdown(
                        "<img src='https://cdn-icons-png.flaticon.com/512/219/219983.png' style='width:100px; height:100px; border-radius:50%;'>",
                        unsafe_allow_html=True)

            st.markdown("""
                <style>
                .text-box {
                    background-color: #2C2C2C;
                    padding: 10px;
                    border-radius: 5px;
                    margin-bottom: 10px;
                    color: #FFFFFF;
                }
                </style>
            """, unsafe_allow_html=True)

            col1, col2, col3 = st.columns([1, 2, 1])

            with col2:
                st.markdown(
                    f"<div class='text-box'><strong>Name:</strong> {user['first_name']} {user['last_name']}</div>",
                    unsafe_allow_html=True)
                st.markdown(f"<div class='text-box'><strong>Username:</strong> {user['username']}</div>",
                            unsafe_allow_html=True)
                st.markdown(f"<div class='text-box'><strong>Email:</strong> {user['email']}</div>",
                            unsafe_allow_html=True)
                st.markdown(f"<div class='text-box'><strong>Mobile Number:</strong> {user['mobile_no']}</div>",
                            unsafe_allow_html=True)
                st.markdown(f"<div class='text-box'><strong>Address:</strong> {user['address']}</div>",
                            unsafe_allow_html=True)
                st.markdown(f"<div class='text-box'><strong>City:</strong> {user['city']}</div>",
                            unsafe_allow_html=True)
                st.markdown(f"<div class='text-box'><strong>State:</strong> {user['state']}</div>",
                            unsafe_allow_html=True)
                st.markdown(f"<div class='text-box'><strong>Pincode:</strong> {user['pincode']}</div>",
                            unsafe_allow_html=True)

                if 'image_uploaded' not in st.session_state:
                    st.session_state.image_uploaded = False

                if not st.session_state.image_uploaded:
                    uploaded_file = st.file_uploader("Upload a new profile picture", type=["jpg", "jpeg", "png"])
                    if uploaded_file is not None:
                        files = {'profile_pic': uploaded_file}
                        response = requests.post(f"http://localhost:8000/api/customers/update_profile_picture/",
                                                 files=files, data={'customer_id': user_id})
                        if response.status_code == 200:
                            st.success("Profile picture updated successfully!")
                            st.session_state.image_uploaded = True
                            st.rerun()
                        else:
                            st.error("Failed to update profile picture.")
                else:
                    st.info("Profile picture already uploaded. Refresh the page to upload a new one.")
        else:
            st.error("Failed to fetch user details.")
    else:
        st.error("Please log in to view your profile.")

def __main__():
    show()
import streamlit as st
import requests
from datetime import datetime

def fetch_orders(user_id):
    response = requests.get(f"http://localhost:8000/api/orders/by-user/?user_id={user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch orders")
        return []

def show_orders():

    if 'user' not in st.session_state or not st.session_state.user:
        st.error("You need to be logged in to view orders.")
        return

    user_id = st.session_state.user['user_id']
    orders = fetch_orders(user_id)

    st.markdown("""
        <div style='text-align: center; font-size: 30px; font-weight: bold; color: #DDDDDD; text-shadow: 2px 2px 4px #000000;'>
            ORDER HISTORY 🛍️
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    <style>
        .orders-table {
            width: 100%;
            border-collapse: collapse;
            margin: 0 auto;
            border: 1px solid #666666;
            border-radius: 10px;
            overflow: hidden;
            background-color: rgba(255, 255, 255, 0.03);
        }
        .orders-table th {
            background-color: #4A4A4A;
            color: #FFFFFF;
            border: 1px solid #666666;
            padding: 8px;
            text-align: center;
        }
        .orders-table td {
            border: 1px solid #666666;
            padding: 8px;
            text-align: center;
            background-color: rgba(255, 255, 255, 0.05); 
        }
        .orders-table tr:nth-child(even) {
            background-color: rgba(255, 255, 255, 0.04);
        }
        .orders-table tr:hover {
            background-color: rgba(255, 255, 255, 0.07);
        }
        .header-order-id, .content-order-id {
            width: 60px;
        }
        .header-order-date, .content-order-date {
            width: 150px;
        }
        .header-total-quantity, .content-total-quantity {
            width: 80px;
        }
        .header-total-price, .content-total-price {
            width: 80px;
        }
        .header-delivery-address, .content-delivery-address {
            width: 300px;
        }
        .header-status, .content-status {
            width: 100px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <table class="orders-table">
        <tr>
            <th class="header-order-id">Order ID</th>
            <th class="header-order-date">Order Date</th>
            <th class="header-total-quantity">Quantity</th>
            <th class="header-total-price">Price</th>
            <th class="header-delivery-address">Delivery Address</th>
            <th class="header-status">Status</th>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    for order in orders:
        order_date = datetime.strptime(order['order_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        formatted_date = order_date.strftime("%d %b %Y, %I:%M %p")
        status_class = f"status-{order['order_status']}"

        st.markdown(f"""
        <table class="orders-table">
        <tr>
            <td class="content-order-id">#{order['id']}</td>
            <td class="content-order-date">{formatted_date}</td>
            <td class="content-total-quantity">{order['total_quantity']}</td>
            <td class="content-total-price">₹{order['total_price']}</td>
            <td class="content-delivery-address">{order['delivery_address']}</td>
            <td class="content-status {status_class}">{order['order_status'].capitalize()}</td>
        </tr>
        </table>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_orders()
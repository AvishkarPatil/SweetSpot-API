import streamlit as st

def show():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css?family=Montserrat:400,700');

            .contact-container {
                display: flex;
                justify-content: space-between;
                padding: 20px;
                border-radius: 10px;
            }
            .contact-form {
                width: 45%;
                background-color: #2C2C2C;
                padding: 20px;
                border-radius: 10px;
            }
            .contact-details {
                width: 45%;
                background-color: #2C2C2C;
                padding: 20px;
                border-radius: 10px;
            }
            .contact-form input, .contact-form textarea {
                width: 100%;
                padding: 10px;
                margin-bottom: 10px;
                border: none;
                border-radius: 5px;
                background-color: #3C3C3C;
                color: white;
            }
            .contact-form button {
                width: 100%;
                padding: 10px;
                border: none;
                border-radius: 5px;
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                cursor: pointer;
            }
            .contact-form button:hover {
                background-color: #45A049;
            }
            .contact-details h3, .contact-details p {
                color: white;
            }
            .map-container {
                width: 100%;
                height: 300px;
                border-radius: 10px;
                overflow: hidden;
            }
            .contact-form h3, .contact-details h3 {
                font-family: 'Montserrat', sans-serif;
                font-size: 20px;
                color: #FFFFFF;
                margin-bottom: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
            <div style='text-align: center; font-size: 28px; font-weight: bold; color: #DDDDDD; text-shadow: 2px 2px 4px #000000;'>
                Contact Us 📞
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("""
        <div class="contact-container">
            <div class="contact-form">
                <h3>Get in Touch</h3>
                <form action="https://formspree.io/f/xnnqzoyq" method="POST">
                    <input type="text" name="name" placeholder="Your Name" required>
                    <input type="email" name="email" placeholder="Your Email" required>
                    <input type="text" name="subject" placeholder="Subject" required>
                    <textarea name="message" placeholder="Your Message" rows="5" required></textarea>
                    <button type="submit">Send Message</button>
                </form>
            </div>
            <div class="contact-details">
                <h3>Contact Information</h3>
                <p><strong>Address:</strong> 123 SweetSpot Lane, TKIET, Warananagar, 416113</p>
                <p><strong>Phone:</strong> (123) 456-6969</p>
                <p><strong>Email:</strong> contact@sweetspot.com</p>
                <div class="map-container">
                    <iframe
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d932.8943457485794!2d74.19776685903155!3d16.85540785856762!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc1a80a7c8a6b7b%3A0x2a6e33b9af5d4171!2sTatyasaheb%20Kore%20Institute%20of%20Engineering%20%26%20Technology%20(An%20Autonomous%20Institute)!5e1!3m2!1sen!2sin!4v1732187803796!5m2!1sen!2sin"
                        width="100%" height="100%" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0">
                    </iframe>
                   </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    show()
import streamlit as st
import httpx

# Get the user-agent string
@st.cache_data()
def get_user_agent():
    try:
        user_agent = httpx.get("https://httpbin.org/user-agent").json()["user-agent"]
    except Exception as e:
        user_agent = "Unknown"
    return user_agent

# Detect if the user is on a mobile device
def is_mobile(user_agent):
    mobile_keywords = ["Mobile", "iPhone", "iPad", "Android"]
    for keyword in mobile_keywords:
        if keyword in user_agent:
            return True
    return False

# Setting the page configuration with a background image
st.set_page_config(
    page_title="Normal Community High School After Prom",
    page_icon=":tada:",
    layout="wide",
)

# Set the background image
def set_bg_image(img_binary):
    with open("background.jpg", "wb") as f:
        f.write(img_binary)
    st.beta_set_background_image("background.jpg")

# Get the user-agent string
user_agent = get_user_agent()

is_mobile = is_mobile(user_agent)

col1, col2 = st.columns([1,6])


if not is_mobile:
    with col1:
        st.image('nchslogo.jpg', width=100)  # Adjust width as needed

    with col2:
        # Title with a marquee effect
        st.markdown(
            """<marquee behavior="scroll" direction="left" loop="-1" scrollamount="5">"""
            + """<h1>✨Normal Community High School After Prom✨</h1>"""
            + "</marquee>",
            unsafe_allow_html=True,
        )
else:
        st.markdown(
            """<marquee behavior="scroll" direction="left" loop="-1" scrollamount="5">"""
            + """<h1>✨Normal Community High School After Prom✨</h1>"""
            + "</marquee>",
            unsafe_allow_html=True,
        )

# Text block about the event details
st.subheader("Join us for an unforgettable night!")
event_details = """
The After Prom party is a safe and fun way to celebrate the end of prom night with your friends. 
This year's theme is **Met Gala Vegas Style**. Get ready for a night of glitz, glamour, and excitement!

**Date:** Saturday, April 27th, 2024
**Time:** 11:00 PM - 3:00 AM
**Location:** Normal Community High School

**Activities:**

* DJ Lights, Music & Lasers
* Amazing Laser Tag
* Interactive Games
* Food Fiesta...and much more!

**Prizes:**

* Grand Prize: Macbook 15
* Over $4000 in giveaways!

**Tickets:** $14 (Tickets can be purchased through the school's GoFan app)
"""
st.markdown(event_details)

st.image(
    "NCHSAfterPromFlyer.jpg",  # Replace with appropriate image
    width=700,
    caption="Vegas Style After Prom!",
)

# Contact information
contact_info = """
For more information, please contact:

* [Normal Community High School](https://www.unit5.org/NCHS)

We hope to see you there!
"""
st.subheader("Contact Us")
st.markdown(contact_info)

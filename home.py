import streamlit as st
def detect_browser():
    if st.config.get_option("browser.gatherUsageStats"):
        return True
    else:
        return  False

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

is_desktop = detect_browser()

col1, col2 = st.columns([1,6])


if is_desktop:
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

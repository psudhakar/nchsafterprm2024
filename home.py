import streamlit as st

# Setting the page configuration with a background image
st.set_page_config(
    page_title="Normal Community High School After Prom",
    page_icon=":tada:",
    layout="wide",
)

st.markdown("""
    <style>
    .block-container {
        padding-top: 0rem;
    }
    .main {
       font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; align: center;
    }
    h1 {
        color: #ff6347;
        text-align: center;
    }
    
    h5 {
        color: dark;
        text-align: center;
    }
    .font {
        font-size:16px;
        font-weight: 400;
    }
    .table-style {
        margin-left: auto; 
        margin-right: auto;
    }
            
    @media screen and (max-width: 768px) {
            .responsive-image {
                display: none;
            }
    }
    @media screen and (min-width: 768px) {
        .responsive-image2 {
            display: none;
        }
    }
            

    </style>
    """, unsafe_allow_html=True)

# Set the background image
def set_bg_image(img_binary):
    with open("background.jpg", "wb") as f:
        f.write(img_binary)
    st.beta_set_background_image("background.jpg")

col1, col2 = st.columns([1,6])

with col1:
        st.markdown(f"""<div style="text-align: center;">
            <img src="https://lh3.googleusercontent.com/d/1gG1iQtiO7Lfl_ZElvqBhfJ0_A0QCu6NE" alt="Image"  style="margin-top: 25px;" >
            </div>""", unsafe_allow_html=True)

        #st.markdown(f"""<div style="text-align: center;">
        #    <img src="https://lh3.googleusercontent.com/d/1KAHfNo580cBk7mh-h7FAkcO1N-csAeAa" alt="Image"  style="margin-top: 25px;" class="responsive-image2">
        #    </div>""", unsafe_allow_html=True)

with col2:
        st.markdown(" ")
        st.markdown(
            #"""<marquee behavior="scroll" direction="left" loop="-1" scrollamount="15">"""
            #+ """<h1>✨Normal Community High School After Prom✨</h1>"""
            #+ "</marquee>"
             "<h1>✨Normal Community High School After Prom - 2024✨</h1>",
            unsafe_allow_html=True,
        )

sub_header = "Join us for an unforgettable night!"

# Wrap the text in markdown with center alignment style
centered_text = f"<h3 style='text-align: center;'>{sub_header}</h2>"

# Display the centered markdown
st.markdown(centered_text, unsafe_allow_html=True)


event_details = """
The After Prom party is a safe and fun way to celebrate the end of prom night with your friends. 
This year's theme is **Met Gala Vegas Style**. Get ready for a night of glitz, glamour, and excitement!

**Date:** Saturday, April 27th, 2024
**Time:** 11:00 PM - 3:00 AM
**Location:** Normal Community High School
"""
with st.container(border=True):
      st.markdown(event_details)

event_details2 = """
**Activities:**

* DJ Lights, Music & Lasers
* Amazing Laser Tag
* Interactive Games
* Food Fiesta...and much more!

**Prizes:**

* Grand Prize: Macbook 15
* Over $4000 in giveaways!

"""

event_details3 = """
**Special Promo - 12 Days of Afterprom:**

- Buy Afterprom tickets early, and increase your chances to win a $15 gift card, each day for 12-days.
- Winners will be announced daily on AfterProm Instagram page & at school!

**Tickets:** $14 ( Tickets can be purchased through the school's [GoFan](https://gofan.co/app/school/IL21465) page )
"""

col1, col2 = st.columns([1,3])

with st.container(border=True):
    with col1:
        st.markdown(event_details2, unsafe_allow_html=True)
    with col2:
        st.markdown(event_details3, unsafe_allow_html=True)


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

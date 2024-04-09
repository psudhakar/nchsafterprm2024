import streamlit as st
from random import choice

# Define flashy text options
flashy_styles = [
    "font-size: 3em; color: #f012be;",  # Large, bright blue
    "font-weight: bold; text-shadow: 2px 2px 5px #fffa00;",  # Bold with yellow shadow
    "font-family: 'Courier New'; color: #8a2be2; animation: blink 1s step-end infinite alternate;",  # Courier font, purple, blinking
]

def flashy_text(text):
  """Returns the text with a randomly chosen flashy style."""
  style = choice(flashy_styles)
  return f"<span style='{style}'>{text}</span>"


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
        st.markdown("<h1>✨Normal Community High School After Prom - 2024✨</h1>",unsafe_allow_html=True)


#col1, col2 = st.columns(2)

#with col1:
#     st.markdown("")
#with col2:
#    st.markdown("")
#    with st.container(border=True): 
#        col1, col2, col3 = st.columns(3)
#        with col1:
#            st.markdown("[Normal Community High School](https://www.unit5.org/NCHS)")
#        with col2:
#            st.markdown("[Buy Tickets](https://gofan.co/app/school/IL21465)")
#        with col3:
#            st.markdown("[Directions](https://nchsafterprom.ticketspice.com/preview/abc58282cedf4ab2829ee2ff7ceca18d#directions)")

  
col1, col2 = st.columns([4,3])

with col1:
    event_details = """
    ## Prom night ends, After Prom adventure begins !
    
    :blue[**The Amazing Laser Tag**]: Strategize your squad and gear up for an unforgettable battle royale between multiple teams. An adrenaline pumping experience in a 50 ft by 50 ft maze

    :orange[**Interactive games**]: Challenge your friends to classic Inflatable competitive fun. Putt your way to victory with "Indoor Mini Golf" with 9 hole course. Work together in a thrilling "Light-Up Cones match" and much much more. Win amazing prizes for some of the interactive games.

    :green[**Food Fiesta**]: Fuel up with an explosion of delicious finger foods, snacks, soft drinks & party treats to keep you hydrated & charged up throughout the night

    :red[**The Main Event**]: Electrify the night with our Celebrity guests from Chicago, the Z-LED Bots, all under the dazzling display of DJ lights, pulsing sounds & heart-pumping music

    :blue[**Grand Finale**]: Get ready for college by gearing up for an epic giveaway, with the chance to win over $6000 in prizes. Create memories that will last long after the music & Afterprom fades away!

    :green[**Street Challenges**]: Non-stop fun with tons of on-the-spot prizes. Afterprom committee will test your brain and body for a chance to win a bucketload of awesome prizes! We'll have you thinking fast with trivia questions and then get you moving with fun physical challenges.
    """
    with st.container(border=True):
        st.markdown(event_details, unsafe_allow_html=True )

with col2:
    event_details3 = """
    #### :blue[Upcoming Schedule]: Special Promo - 12 Days of Afterprom:

    - Buy Afterprom tickets early, and increase your chances to win a $15 gift card, each day for 12-days.
    - Winners will be announced daily on AfterProm Instagram page & at school!

    **Tickets:** $14 ( Tickets can be purchased through the school's [GoFan](https://gofan.co/app/school/IL21465) page )
    """
     
    with st.container(border=True):
        st.markdown(event_details3, unsafe_allow_html=True )

        col1, col2 = st.columns([1,4])
       
        with col1:
             st.markdown("**School web site:**")
        with col2: 
            st.markdown("[Normal Community High School](https://www.unit5.org/NCHS)")

        with col1:
             st.markdown("**Buy Tickets:**")
        with col2:
            st.markdown("[School GoFan site](https://gofan.co/app/school/IL21465) (Only **$14** for AfterProm tickets from GoFan. Use Access Code: :green[PROM24])")

        with col1:
             st.markdown("**Location:**")
        with col2: 
            st.markdown("3900 E Raab Rd, Normal, IL 61761, USA, Normal, IL, 61761 US")

        with col1:       
            st.markdown("**Directions:**")
        with col2:
             st.markdown("[Google](https://maps.google.com/?daddr=3900%20E%20Raab%20Rd%2C%20Normal%2C%20IL%2061761%2C%20USA%2C%20Normal%20IL%2061761%20US) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Bing](https://www.bing.com/maps/default.aspx?rtp=~adr.3900%20E%20Raab%20Rd%2C%20Normal%2C%20IL%2061761%2C%20USA%2C%20Normal%20IL%2061761%20US) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [MapQuest](http://mapq.st/directions?saddr=&daddr=3900%20E%20Raab%20Rd%2C%20Normal%2C%20IL%2061761%2C%20USA%2C%20Normal%20IL%2061761%20US)")

    with st.container(border=True):
        st.markdown(flashy_text("✨ Join us for an epic After Prom Party, an unforgettable journey beyond the ballroom. ✨"), unsafe_allow_html=True)

st.image(
    "NCHSAfterPromFlyer.jpg",  # Replace with appropriate image
    use_column_width=True
)

#sub_header = "Join us for an unforgettable night!"
# Wrap the text in markdown with center alignment style
#centered_text = f"<h3 style='text-align: center;'>{sub_header}</h2>"
# Display the centered markdown
#st.markdown(centered_text, unsafe_allow_html=True)

        



#st.image(
#    "NCHSAfterPromFlyer.jpg",  # Replace with appropriate image
#    width=700,
#    caption="Vegas Style After Prom!",
#)

from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Website", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

#  Load session

lottie_coding = load_lottieurl(
    "https://assets7.lottiefiles.com/packages/lf20_4kx2q32n.json")
img_webpage_form = Image.open("Images/website1.png")
img_webcontact_form = Image.open("Images/ContactForm.png")
# Header session

st.subheader("Hello, I am Abdul Nasir :wave:")
st.title("A Software Engineer from India ")
st.write("I am passionate about learning new Skill set and working on it")
st.write("[Learn More >](https://abdulnasir-nuz.github.io/)")

# What i Do

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
with left_column:
    st.header("What I Do")
    st.write("##")
    st.write(
        """
    Experienced software engineer with a passion for developing innovative programs
    that expedite the efficiency and effectiveness of organizational success.
    Well-versed in technology and writing code to create systems that are reliable and user-friendly.
    Skilled leader who has the proven ability to motivate, educate, and manage a team of professionals 
    to build software programs and effectively track changes. Confident communicator, strategic thinker,
    and innovative creator to develop software that is customized to meet a company’s organizational needs,
    highlight their core competencies, and further their success.
    """
    )
    st.write("[LinkedIn >](https://www.linkedin.com/in/abdul-NasirV)")

with right_column:
    st_lottie(lottie_coding, height=400, key="coding")

# Projects

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

with image_column:
    st.image(img_webpage_form)


with text_column:
    st.subheader("Integrate Lottie Animation Inside streamlit App")
    st.write(
        """
    Learn how to use Lottie file in Streamlit
    Animations make the website app more eangaging and fun, 
    and Lottie Files are the easiest way to do,
    
    """
    )
    st.write("[LottieWebapp >> ]( http://192.168.117.147:8501 )")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_webcontact_form)

with text_column:
    st.subheader("Contact Form in Streamlit App")
    st.write(
        """
    Learn how to use form and its functionality in Streamlit
    Animations make the website app more eangaging and fun,
    and Lottie Files are the easiest way to do,
    
    """
    )
    st.write("[LottieWebapp >> ]( http://192.168.117.147:8501 )")


# Contact Form

with st.container():
    st.write("---")
    st.header("Get In Touch with Me!")
    st.write("##")
contact_form = """
<form action="https://formsubmit.co/coderfile06@gmail.com" method="POST">
     <input type ="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder= "Your Name" required>
     <input type="email" name="email" placeholder ="Your Email-id" required>
     <textarea name="message" placeholder="Your message here" required ></textarea>
     <button type="submit">Send </button>
</form>
"""

left_column, right_column = st. columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()

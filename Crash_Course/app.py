import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
# Title
st.title("A Crash Course of Streamlit")

# Header or Sub-header
st.header("This is a header")
st.subheader("This is a sub-header")

# Text
st.text("Hello! Streamlit")

# Markdown
st.markdown("### Markdown Header")

# Flash Message
st.success("Succesful")
st.info("Informations!")
st.warning("WARNING")
st.error("Error!")
st.exception("NameError('Name three not defined')")

# Get Help About Python
st.help(range)

# Writinig Text
st.write("Hello World!")
st.write(range(10))

# Images
from PIL import Image
img = Image.open("./img/Word Art.png")
st.image(img, width=300, caption="Simple Image")

# Videos / Audion
vid = open("./video/intro.mkv", "rb")
# vid_bytes = vid.read()
st.video(vid)
# st.audio()

# Widgets: Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widgets")

# Widgets: Radio
status = st.radio("What is your status?", ("Active", "Inactive"))
if status == 'Active':
    st.success("You are active!")
else:
    st.warning("Inactive, Activate")

# Widgets: Selectbox
occupation = st.selectbox("Your occupation", ["Programmer", "Data Scientist", "Data Analyst"])
st.write("You are selected this option", occupation)


# Widgets: Multiple Selection
locations = st.multiselect("Where do you work?", ("London", "New York", "India", "Bangladesh"))
st.write("You sleected", len(locations), "locations")

# Widgets: Slider
level = st.slider("What is your level?", 1,5)

# Widgets: Buttons
st.button("Simple Button")
if st.button("About"):
    st.text("Streamlit is cool!")

# Text Input
firstname = st.text_input("Enter your firstname", "John")
if st.button("Submit"):
    result = firstname.title()
    st.success(result)

# Text Area
message = st.text_area("Enter your message", "Type here...")
if st.button("BoxSubmit"):
    result = message.title()
    st.success(result)


# Date Input
import datetime
today = st.date_input("Today is", datetime.datetime.now())

# Time
time = st.time_input("The time is", datetime.time())

# Display JSON Object
st.text("Display JSON")
st.json({"name":"John", "Gender": 23})

# Display Code
st.text("Display Code")
st.code("import numpy as np")

# Display Raw Code
with st.echo():
    # This will show as a comment
    import numpy as np
    import pandas as pd

# Progressbar
import time
bar = st.progress(0)
for p in range(10):
    bar.progress(p+1)


# Spiner
with st.spinner("Waiting..."):
    time.sleep(5)
st.success("Finished!")

# Balloons
st.balloons()

# Sidebar Widgets
st.sidebar.header("Sidebar")
st.sidebar.text("A Crash Course of Streamlit")

# Functions
@st.cache # Makes ir faster
def run_fun():
    return range(100)

st.write(run_fun)

# Plots
st.pyplot()

# DataFrame
st.dataframe(df)

# Table
st.table(df)

class MySeq:
    """"A Class for a Sequence"""

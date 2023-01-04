import streamlit as st
#Text/Title
st.title("Streamlit Tutorials")
#Header/Subheader
st.header("This is header")
st.subheader("This is dubheader")

#text
st.text("Helo Streamlit")
#MArkdown
st.markdown("### This is markdown")
 
#Error/Colorful Text
st.success("Successful")

st.info("information!")
st.warning("This is warning!")
st.error("This is error danger!")
st.exception("Name Error('name three not defined')")

#Get help about Python
st.help(range)

#Writing Text

st.write("Text with Write")

st.write(range(10))

#Images
from PIL import Image 
img=Image.open("example.jpeg")
st.image(img,width=300,caption="Simple İmage")

#videos
vid_file=open("example.mp4","rb").read()

#vid_bytes=vid_file.read()
st.video(vid_file)
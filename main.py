import streamlit as st
from PIL import Image
#Start the camera
with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if camera_image:      # If the permission for camera usage is allowed then do next
    #Create a pillow image instance
    img = Image.open(camera_image)

    #Convert into Gray Scale using a Algorithm denoted by 'L'
    grey_img = img.convert("L")

    #Render the grayscale on the webpage
    st.image(grey_img)

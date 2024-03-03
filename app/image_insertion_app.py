import streamlit as st
import image_insertion_lib as glib

# Set page configuration
st.set_page_config(layout="wide", page_title="Friend Gen")

# Set page title
st.title("Friend Gen")

# Create columns for layout
col1, col2, col3 = st.columns(3)

# Column 1: Image upload
with col1:
    st.subheader("Friendless image")
    
    uploaded_file = st.file_uploader("Select an image (must be 512x512)", type=['png', 'jpg'])
    
    if uploaded_file:
        uploaded_image_preview = glib.get_bytesio_from_bytes(uploaded_file.getvalue())
        st.image(uploaded_image_preview)
    else:
        st.image("images/desk.jpg")
        
# Column 2: Insertion parameters
with col2:
    st.subheader("Insertion parameters")
        
    with st.expander("Mask Input:", expanded=True):
        
        mask_dimensions = (0,0,0,0)
    
        mask_x = st.number_input("Mask x position", value=mask_dimensions[0])
        mask_y = st.number_input("Mask y position", value=mask_dimensions[1])
        mask_width = st.number_input("Mask width", value=mask_dimensions[2])
        mask_height = st.number_input("Mask height", value=mask_dimensions[3])
    
    generate_button = st.button("Generate")
    
# Column 3: Generated image display
with col3:
    st.subheader("Friends generated here.")

    if generate_button:
        with st.spinner("Drawing friends..."):
            if uploaded_file:
                image_bytes = uploaded_file.getvalue()
            else:
                image_bytes = None
            
            generated_image = glib.get_image_from_model(
                image_bytes=image_bytes, 
                insertion_position=(mask_x, mask_y),
                insertion_dimensions=(mask_width, mask_height),
            )
        
        st.image(generated_image)

# Load CSS
with open('styles.css') as f:
        css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
# End load CSS
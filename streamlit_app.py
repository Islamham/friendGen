import streamlit as st
import time as time

def main():
    # Register your pages
    pages = {
        "Home page": page_home,
        "Photos page": page_photos,
    }

    st.set_page_config(layout="wide", page_title="Friend Gen")
    st.title("Friend Gen")

    pages["Home page"](pages)

    # Load CSS
    with open('styles.css') as f:
        css = f.read()

    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


def page_home(pages):
    st.write("Generate new friends for your images!")

    # TODO: AI generate friend related quotes
    friend_quote = "_'Cause you got a friend in me!_"
    st.markdown(friend_quote)

    # Upload image widget
    uploaded_file = st.file_uploader("Upload friendless image", 
                     type=['png', 'jpg'], 
                     accept_multiple_files=False,
                     help="Upload an image into which you want extra people added!")
    
    # Display uploaded file
    if uploaded_file:
        st.image(uploaded_file, width=500)
    else:
        st.image("img/input/pug.jpeg", width=500)   # Default

    # Button
    if st.button("Click for friends!", key="click-for-friends"):
        pages["Photos page"]()


def page_photos():
    # Load CSS (don't touch this)
    with open('styles.css') as f:
        css = f.read()

    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    # End load CSS

    
    # Output 
    with st.spinner("Making friends..."):
        # GENERATE IMAGE HERE




        st.write("Here are your new friends!")

        # TODO: change this to result photo
        st.image("img/output/pug.jpeg", width=500)

    # Download resultant image TODO: fix
    # st.download_button("Download friendly image", 
    #                    data="output/pug.jpeg",
    #                    mime="image/jpeg")


if __name__ == "__main__":
    main()

